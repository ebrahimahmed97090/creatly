from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=264, blank=False)
    upassword = models.CharField(max_length=500, blank=False)
    ucountry = models.CharField(max_length=256, blank=False)
    ucity = models.CharField(max_length=256, blank=False)
    ustreetAddress = models.CharField(max_length=256, blank=False)
    ufname = models.CharField(max_length=256, blank=False)
    ulname = models.CharField(max_length=256, blank=False)
    umembership = models.CharField(max_length=25, blank=False)


class PaymentMethods(models.Model):
    userpayment = models.ForeignKey(User, on_delete=models.CASCADE)
    paymethod = models.CharField(max_length=200, blank=True)


class WebSites(models.Model):
    wid = models.AutoField(primary_key=True)
    wname = models.CharField(max_length=255, blank=False)
    wpath = models.CharField(max_length=255)
    USERSITE = models.ForeignKey(User, on_delete=models.PROTECT)


class WebsiteOptions(models.Model):
    SITEOPT = models.ForeignKey(WebSites, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)


class Pages(models.Model):
    PID = models.AutoField(models.UniqueConstraint,primary_key=True)
    pname = models.CharField(max_length=255)
    ppath = models.CharField(max_length=500)
    SITEPAGE = models.ForeignKey(WebSites, on_delete=models.PROTECT)


class Elements(models.Model):
    eid = models.CharField(models.UniqueConstraint, max_length=100, primary_key=True)
    PPATH = models.ForeignKey(Pages, on_delete=models.PROTECT)
    index = models.IntegerField()


class ElementOfElement:
    PARENT = models.ForeignKey(Elements, on_delete=models.PROTECT)
    CHILD = models.ForeignKey(Elements, on_delete=models.PROTECT)


class ElementClasses:
    CLASSELEMENT = models.ForeignKey(Elements, on_delete=models.PROTECT)
    classes = models.CharField(max_length=500)


class ElementAttributes:
    ATTRIELEMENT = models.ForeignKey(Elements, on_delete=models.PROTECT)
    attributes = models.CharField(max_length=500)
