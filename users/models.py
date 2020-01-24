from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=264, blank=False)
    upassword = models.CharField(max_length=500, blank=False)
    country = models.CharField(max_length=256, blank=False)
    city = models.CharField(max_length=256, blank=False)
    streetAddress = models.CharField(max_length=256, blank=False)
    FName = models.CharField(max_length=256, blank=False)
    LName = models.CharField(max_length=256, blank=False)
    memberShip = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.uname


class PaymentMethods(models.Model):
    userpayment = models.ForeignKey(User, on_delete=models.CASCADE)
    payMethod = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user


class WebSites(models.Model):
    wid = models.AutoField(primary_key=True)
    wname = models.CharField(max_length=255, blank=False)
    wpath = models.CharField(max_length=255)
    usersite = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.wname


class WebsiteOptions(models.Model)
    siteoption = models.ForeignKey(WebSites, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)


class Pages(models.Model)
    PID = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=255)
    ppath = models.CharField(max_length=500)
    sitepage = models.ForeignKey(WebSites, on_delete=models.PROTECT)
   