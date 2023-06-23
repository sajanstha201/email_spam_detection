from django.db import models
class emails(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    text=models.TextField()
    choice=models.CharField()
    link=models.URLField()
    image=models.ImageField()
    def __str__(self):
        return self.username
