from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Post(models.Model):
    post_status = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    )

    post_category = (
        ('Web Development', 'Web Development'),
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Flask', 'Flask'),
        ('Pyramid', 'Pyramid'),
        ('REST Framework', 'REST Framework'),
        ('Javascript', 'Javascript'),
        ('Angular', 'Angular'),
        ('REACT', 'REACT'),
        ('Node', 'Node'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Bootstrap', 'Bootstrap'),
        ('Java', 'Java'),
        ('Databases', 'Databases'),

    )

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    about_article = models.CharField(max_length=255, blank=True, null=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    post_category = models.CharField(max_length=30, choices=post_category, default='Web Development')
    status = models.CharField(max_length=30, choices=post_status, default='Draft')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    pinned = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # approved_comment = models.BooleanField(default=False)


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
