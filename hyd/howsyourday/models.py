from django.db import models

class ColorDecision(models.Model):
    userText = models.CharField(max_length=100, null=False, blank=True, default=" ")
    publishDate = models.DateTimeField('date published')
    userColor = models.CharField(max_length=6)
    userName = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.publishDate} | {self.userName} #{self.userColor}"