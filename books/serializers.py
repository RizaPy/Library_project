from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():

            raise ValidationError(
                {
                    'status':False,
                    'message':'Kitobning sarlavhasi harflardan tashkil topgan bo\'lishi kerak'
                }
            )

        if Books.objects.filter(title='title', author=author).exists():
            raise ValidationError(
                {
                    'status':   False,
                    'message':'Kitob sarlavhasi va muallifi bir xil bo\'lgan ikkita kitobni saqlay olmaysiz'
                }
            )

        return data
