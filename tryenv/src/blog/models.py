from django.db import models

class Article(models.Model):
    title =models.CharField(max_length=120)
    content =models.TextField()
    active =models.BooleanField(default=True)
# Create your models here.
    def get_absolute_url(self):
        return reverse("articles:article-detail",kwargs={"id":self.id}) #f"/products/{self.id}"