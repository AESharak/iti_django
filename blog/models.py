from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_post_count(self):
        return self.posts.count()
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.get_full_name()


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"
    
    class Meta:
        ordering = ['-created_at']