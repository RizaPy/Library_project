from django.urls import path, include
from .views import BookListApiView, BookDetailApiView, BookUpdateDeleteApiView, BookApiViewset
from rest_framework.routers import SimpleRouter
from books import views
router = SimpleRouter()
router.register('books', views.BookApiViewset, basename='books')

urlpatterns = [
    # path('', BookListApiView.as_view()),
    # path('<int:pk>/', BookDetailApiView.as_view()),
    # path('<int:pk>/update-delete/', BookUpdateDeleteApiView.as_view()),
    # path('create/', BookListApiView.as_view()),
    path('', include(router.urls)),
]

