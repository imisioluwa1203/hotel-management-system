from django.db import models

# Create your models here.
class Biodata(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class Item(models.Model):
    name = models.CharField(max_length=50)
    bio = models.ForeignKey(Biodata,on_delete=models.CASCADE)
    
class Cart(models.Model):
    bio = models.ForeignKey(Biodata,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.CharField(max_length=10)
    price = models.CharField(max_length=20)


class Nysc_bio(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    batch = models.CharField(max_length=20)


class Nysc_bank_account(models.Model):
    nysc_bio = models.ForeignKey(Nysc_bio,on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50) 
    account_type = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

class Social_handles(models.Model):
    nysc_bio = models.ForeignKey(Nysc_bio,on_delete=models.CASCADE)
    twitter_handle = models.CharField(max_length=50)
    facebook_handle = models.CharField(max_length=50)
    instagram_handle = models.CharField(max_length=50)

class Nysc_project(models.Model):
    nysc_bio = models.ForeignKey(Nysc_bio,on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    supervisor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)


class Educational_qualification(models.Model):
    nysc_bio = models.ForeignKey(Nysc_bio,on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    degree_obtained = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    grade = models.CharField(max_length=10)


class Batch_details(models.Model):
    batch_name = models.CharField(max_length=50)
    nysc_bio = models.ForeignKey(Nysc_bio,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

