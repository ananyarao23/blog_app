from django.db import models
from froala_editor.fields import FroalaField
from myapp.helpers import *
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=124)
    phone = models.CharField(max_length=124)
    concern = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
class BlogModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    pub_date = models.DateField()
    category = models.CharField(max_length=100)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
         self.slug = generate_slug(self.title)
         super(BlogModel, self).save(*args, **kwargs)



