from django.db import models

# Create your models here.
class donor(models.Model):
    donor_name=models.CharField(max_length=40, default="")
    phone_number=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    date_of_birth=models.DateField(auto_now_add=False, auto_now=False)
    address=models.CharField(max_length=100, default="")
    gender_choices=(
        ('F', 'Female'),
        ('M','Male'),
        )
    gender= models.CharField(choices=gender_choices, max_length=6, default="")

    def __str__(self):
        return self.donor_name

class blooddetails(models.Model):
    donor_id=models.ForeignKey(donor, null=True, on_delete= models.SET_NULL)
    blood_type=(
        ('O+', 'O+'), 
        ('O-', 'O-'), 
        ('A+', 'A+'), 
        ('A-', 'A-'), 
        ('B+', 'B+'), 
        ('B-', 'B-'), 
        ('AB+', 'AB+'), 
        ('AB-', 'AB-')
        )
    bb_blood= models.CharField(choices=blood_type, max_length=3, default="")
    blood_bag_number= models.IntegerField(default=0)
    date_extracted= models.DateTimeField(auto_now_add=False, auto_now=False)
    remarks=models.CharField(max_length=100, default="")

    def __str__(self):
      return self.remarks

class bloodbank(models.Model):
    blood_id=models.ForeignKey(blooddetails, null=True, on_delete= models.SET_NULL)
    name=models.CharField(max_length=100, default="")
    telephone_number=models.IntegerField(default=0)
    blood_bank_address=models.CharField(max_length=100, default="")
    quantity_received=models.IntegerField(default=0)
    description=models.CharField(max_length=40, default="")
    


    def __str__(self):
      return self.name

class hospital(models.Model):
    hospital_name= models.CharField(max_length=100, default="")
    hospital_address=models.CharField(max_length=100, default="")
    phone_number=models.IntegerField(default=0)


    def __str__(self):
      return self.hospital_name

class employee(models.Model):
    hospital_id=models.ForeignKey(hospital, null=True, on_delete= models.SET_NULL)
    employee_name = models.CharField(max_length=30, default="")
    employee_phone_number=models.IntegerField(default=0)
    employee_Address=models.CharField(max_length=100, default="" )
    employee_position=models.CharField(max_length=20, default="")

    def __str__(self):
      return self.employee_name

class bloodrequest(models.Model):
    hospital_id = models.ForeignKey(hospital, null=True, on_delete= models.SET_NULL)
    employee_id = models.ForeignKey(employee, null=True, on_delete= models.SET_NULL)
    date = models.DateField(auto_now_add=False, auto_now=False)
    quantity=models.IntegerField(default=0)
    bld_typ_req=models.CharField(max_length=3, default="")
    recipient_name=models.CharField(max_length=20, default="")

    def __str__(self):
        return self.bld_typ_req

