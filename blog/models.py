from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# CodeInstitute I Think Therefore I Blog was used as insperation for the blog
# This is so the Admin can save blogs in draft with out being public
STATUS = ((0, "Draft"), (1, "Published"))

# This model collects all the details required to be inputed to create a blog post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()

# This model shows the admin the details of the user that submitted the comment.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
