from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_image = models.ImageField(upload_to="blogs")
    blog_name = models.CharField(max_length=50, default='')
    blog_date = models.CharField(max_length=50)
    blog_content = models.TextField()

    def __str__(self):
        return self.blog_name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
    
