from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="blog/", default="blog/default.png")
    title = models.CharField(max_length=255)
    content = QuillField()
    url = models.URLField(max_length=500, null=True, blank=True)
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    creat_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creat_date"]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[str(self.id)])


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.email
