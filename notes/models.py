from django.db import models

# Create your models here.
class Note(models.Model):
    # here we are creating the feilds we want to be appear in the admin page 
    titel = models.CharField(max_length=30 ,default="", blank=True)
    summary = models.TextField()
    created_day = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str: 
        # the str will display the titel and the date in the admin page 
        return f"{self.titel}, Created: {self.created_day}"