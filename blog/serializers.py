from rest_framework import serializers
from .models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'image']

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'slug', 'author', 'author_name', 'image']
        read_only_fields = ['slug', 'created_at']
    
    def get_author_name(self, obj):
        if obj.author:
            return obj.author.get_full_name()
        return None 