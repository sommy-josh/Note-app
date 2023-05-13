from django.db import models

# Create your models here.
class NoteBook(models.Model):
    title =models.CharField(max_length=100)
    notes = models.TextField()
    
  
    def __str__(self):
        return self.title

