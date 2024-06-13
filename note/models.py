from django.db import models

class Note(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default='备忘')
    note = models.TextField()
    summary = models.TextField()
    time = models.CharField(max_length=50)

class Image(models.Model):
    note = models.ForeignKey(Note, related_name='images', on_delete=models.CASCADE)
    start = models.IntegerField()
    base64 = models.TextField()
    
class Vocal(models.Model):
    note = models.ForeignKey(Note, related_name='vocals', on_delete=models.CASCADE)
    start = models.IntegerField()
    base64 = models.TextField()
