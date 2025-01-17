from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class UserProfileInfo(models.Model):
    MEMBER_CHOICES = (('free', 'Free'), ('minimal', 'Minimal'), ('premium', 'Premium'))
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    profile_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    ucountry = CountryField()
    ucity = models.CharField(max_length=256, blank=False)
    ustreetAddress = models.CharField(max_length=256, blank=False)
    umembership = models.CharField(max_length=225, choices=MEMBER_CHOICES)

    def __str__(self):
        return self.user.username


class PaymentMethods(models.Model):
    PAYMENT_CHOICES = [('FAW', 'fawry'), ('VFC', 'vodafone cash'), ('CC', 'Credit card'), ('C', 'Cash')]
    userp = models.ForeignKey(User, on_delete=models.CASCADE)
    pmthid = models.AutoField(primary_key=True)
    paymethod = models.CharField(max_length=200, choices=PAYMENT_CHOICES)


class WebSites(models.Model):
    userw = models.ForeignKey(User, on_delete=models.CASCADE)
    wid = models.AutoField(primary_key=True)
    wname = models.CharField(max_length=255, blank=False)
    wpath = models.CharField(max_length=255)


class WebsiteOptions(models.Model):
    SITEOPT = models.ForeignKey(WebSites, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)


class Pages(models.Model):
    PID = models.AutoField(models.UniqueConstraint, primary_key=True)
    pname = models.CharField(max_length=255)
    ppath = models.CharField(max_length=500)
    SITEPAGE = models.ForeignKey(WebSites, on_delete=models.PROTECT)


class Elements(models.Model):
    eid = models.CharField(models.UniqueConstraint, max_length=100, primary_key=True)
    PPATH = models.ForeignKey(Pages, on_delete=models.PROTECT)
    index = models.IntegerField()


class ElementClasses(models.Model):
    CLASSELEMENT = models.ForeignKey(Elements, on_delete=models.PROTECT)
    classes = models.CharField(max_length=500)


class ElementAttributes(models.Model):
    ATTRIELEMENT = models.ForeignKey(Elements, on_delete=models.PROTECT)
    attributes = models.CharField(max_length=500)
