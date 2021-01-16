from django.db import models

# Create your models here.

class TodoNote(models.Model):
    subject=models.CharField(max_length=1000)
    description=models.TextField()
    deadline=models.DateTimeField()

    timestamp=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("{0} {1}".format(self.subject,self.timestamp))