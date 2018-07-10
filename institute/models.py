from  django.db import models

class Course(models.Model):
    Id=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    fees=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    imageUrl=models.ImageField(default='defoult.png',blank=True)
    videoUrl=models.CharField(max_length=30)

    def __str__(self):
        return self.name + '' +self.fees

class Faculty(models.Model):
    Id=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    imageUrl=models.CharField(max_length=30)
    videoUrl=models.CharField(max_length=30)
    def __str__(self):
        return self.name + '' +self.fees