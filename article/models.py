from django.db import models


class Article(models.Model):
    todo = models.CharField(max_length=255)
    regDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)