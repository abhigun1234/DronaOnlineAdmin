from  django.db import models

class Course(models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    fees=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    imageUrl=models.ImageField(default='defoult.png',blank=True)
    videoUrl=models.FileField()

    def __str__(self):
        return self.name + '' +self.fees

class Faculty(models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    imageUrl=models.CharField(max_length=30)
    videoUrl=models.CharField(max_length=30)
    def __str__(self):
        return self.name + '' +self.fees

class user(models.Model):
    Id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_no=models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birth_date = models.DateField(max_length=30)


class dronauser(models.Model):
    Id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_no=models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birth_date = models.DateField(max_length=30)
    password=models.CharField(max_length=20)
    token=models.CharField(max_length=30)

