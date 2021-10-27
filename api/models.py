from django.db import models

# Create your models here.
class Assignment(models.Model):
  subject=models.CharField(max_length=50)
  finished=models.BooleanField(default=False,blank=True,null=True)

  def __str__(self):
    return self.subject