from blog.models import Post, Author

# Check if there's an existing author
author = Author.objects.first()
if not author:
    # Create a default author
    author = Author.objects.create(
        first_name='Default',
        last_name='Author',
        email='default@example.com',
        phone_number='123-456-7890'
    )
    print(f"Created default author: {author}")

# Update existing posts
posts_without_author = Post.objects.filter(author=None)
for post in posts_without_author:
    post.author = author
    post.save()
    print(f"Updated post: {post.title}")

print(f"Updated {posts_without_author.count()} posts.")
