from django.db import models

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100,null=True,blank=False)
    age = models.IntegerField(default=20)
    image = models.ImageField(upload_to='image',null=True, blank=True)
    address = models.CharField(max_length=200,null=True,blank=False)
    city = models.CharField(max_length=50,default='kerala')
    state = models.CharField(max_length=50,default='kereala')
    country = models.CharField(max_length=50,default='india')
    zip_code = models.CharField(max_length=12,default='pincode')
    code = models.IntegerField(default=20)
    mobile = models.IntegerField(default=1234567890)
    email = models.EmailField(default='123@gmail.com',null=True,blank=False)


    def __str__(self):
        return '{}'.format(self.name)
