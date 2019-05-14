from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#title
#url
#pub_date
#votes_total
#image
#icon
#body
#pub_date pretty
#hunter (user)

class Product(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    url=models.TextField()
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
