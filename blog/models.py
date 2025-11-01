from django.db import models
import os
from django.urls import reverse
from ckeditor.fields import RichTextField

def get_blog_image_path(instance, filename):
    return os.path.join('blog', f'{'thumbnail'}_{instance.id}')

class Tag(models.Model):
    tag = models.CharField(max_length=15)

    def __str__(self):
        return self.tag

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    tags = models.ManyToManyField(Tag)
    thumbnail = models.ImageField(upload_to=get_blog_image_path)
    view = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"id": self.id})