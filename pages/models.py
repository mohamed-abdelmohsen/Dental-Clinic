from django.db import models

# Create your models here.


class patient(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    patient_id=models.BigIntegerField(null=True)
    patient_number=models.BigIntegerField(null=True)
    email=models.EmailField()
    Doctor=models.CharField(max_length=50,null=True)
    Registeration_date=models.DateTimeField()
    appointment=models.DateTimeField(null=True)
    medical_history=models.TextField(null=True)
    session=models.TextField(null=True)

    def __str__(self):
        return self.name
    

class searchModel(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()

    def __str__(self):
        return self.name


