from django.db import models

# Create your models here.
class Article(models.Model):
    #article id
    article_id = models.AutoField(primary_key=True)
    #article title
    title = models.TextField()
    #article brief_content
    brief_content=models.TextField()
    #article content
    content=models.TextField()
    #publish date
    publish_date=models.DateField(auto_now=True)


    def __str__(self):
        return self.title