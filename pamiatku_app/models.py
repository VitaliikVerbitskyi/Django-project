from django.db import models

class PamTitle(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

