from django.contrib.auth.models import User
from django.db import models

class Personal(models.Model):
  user = models.OneToOneField( User, on_delete=models.CASCADE, null = True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=30)
  zipcode = models.CharField(max_length=6)
  country = models.CharField(max_length=50)
  email = models.EmailField(max_length=25)
  phone = models.CharField(max_length=10)

  def __str__(self):
    return self.first_name + self.last_name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    school_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    field_of_study = models.CharField(max_length=40)
    graduation_date = models.IntegerField(default = 0)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()

    def __str__(self):
      return self.school_name


class Skill(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)  
  skill = models.CharField(max_length=50)
  level = models.IntegerField()

  def __str__(self):
    return self.skill

class Project(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)  
  name = models.CharField(max_length=100)
  tech_used = models.CharField(max_length=50)
  started_date = models.DateField()
  end_date = models.DateField()
  description = models.TextField()

  def __str__(self):
    return self.name

class Experience(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)  
  company_name = models.CharField(max_length=50)
  started_date = models.DateField()
  end_date = models.DateField()
  position = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.company_name

