from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name="Author")
    title = models.CharField(max_length=50, verbose_name="Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Published date")
    article_image = models.FileField(blank=True, null=True, verbose_name="Add image to article")
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,verbose_name="Article", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Comment Author")
    comment_content = models.TextField(max_length=250, verbose_name="Content")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Published date")
    
    class Meta:
        ordering = ['-comment_date']
    def __str__(self):
        return self.comment_content