from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Author, Comment
from django.contrib import messages

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Handle comment submission
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        
        if author_name and content:
            Comment.objects.create(
                post=post,
                author_name=author_name,
                content=content
            )
            messages.success(request, 'Your comment has been posted!')
            return redirect('post_detail', slug=post.slug)
    
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    posts = author.posts.all()
    return render(request, 'blog/author_detail.html', {
        'author': author,
        'posts': posts
    })

def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, f'Post "{post.title}" has been deleted!')
        return redirect('post_list')
    
    return render(request, 'blog/delete_post.html', {'post': post})

def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    
    if request.method == 'POST':
        author_name = author.get_full_name()
        author.delete()  # This will cascade to delete related posts and comments
        messages.success(request, f'Author "{author_name}" and all related posts have been deleted!')
        return redirect('post_list')
    
    return render(request, 'blog/delete_author.html', {'author': author})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
        return redirect('post_detail', slug=post.slug)
    
    return render(request, 'blog/delete_comment.html', {'comment': comment})