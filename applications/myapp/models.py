from django.db import models

class Person(models.Model):
  id = models.AutoField(primary_key = True)
  firstname = models.CharField(max_length = 100)
  lastname = models.CharField(max_length = 120)
  email = models.EmailField(max_length = 200)

  def __str__(self):
    return self.firstname