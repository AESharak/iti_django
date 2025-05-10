from blog.models import Post, Author

# Check authors
authors = Author.objects.all()
print(f"Number of authors: {authors.count()}")
for author in authors:
    print(f"- {author.get_full_name()} (ID: {author.id})")

# Check for posts without authors
posts_without_author = Post.objects.filter(author__isnull=True)
print(f"\nNumber of posts without an author: {posts_without_author.count()}")

if posts_without_author.count() > 0:
    print("Posts without an author:")
    for post in posts_without_author:
        print(f"- {post.title} (ID: {post.id})")

# Check all posts
all_posts = Post.objects.all()
print(f"\nTotal number of posts: {all_posts.count()}")

# Print all posts with their authors
print("\nAll posts with their authors:")
for post in all_posts:
    author_info = post.author.get_full_name() if post.author else "No Author"
    print(f"- {post.title} by {author_info}")
