from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SludField()
    date = models.DateTimeField(auto_now_add = True)
    banner = models.ImagField(default = '', blank = True)

    def __str__(self) -> str:
        return self.title