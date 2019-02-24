from django.db import models

class NotesInfo(models.Model):
    datetime=models.DateTimeField(auto_now_add=True)
    subject=models.CharField(max_length=255)
    discription=models.CharField(max_length=500)
    