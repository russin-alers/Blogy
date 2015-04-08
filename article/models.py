# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Article(models.Model):

    class Meta():
        db_table = "article"

    def __str__(self):
        return self.article_title

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_pub_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comments(models.Model):

    class Meta():
        db_table = "comments"

    comments_text = models.TextField(verbose_name="Комментарий")
    comments_acticle = models.ForeignKey(Article)