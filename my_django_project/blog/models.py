from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Class inheritance 
class Post(models.Model):
    # CharField (short for character field) is the max number of characters allowed to be typed.
    # In this case, it's for our post titles
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # We don't include parenthesis because we don't want to execute the function. Only to pass
    # in the function itself as our default value.

    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail",kwargs={"pk":self.pk})
    



