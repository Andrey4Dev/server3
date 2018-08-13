from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.
class Customer(models.Model):
    """
    Customer model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Customer across whole app")
    externalID = models.CharField(max_length=100, help_text="Customer ID is uniq identifier")
    lastname = models.CharField(max_length=200, help_text="Customer Last Name")
    firstname = models.CharField(max_length=200, help_text="Customer First Name")
    regdate = models.DateTimeField(null=True, blank=True, auto_now=True)
    updatedate = models.DateTimeField(null=True, blank=True, auto_now=True)
    kyc = models.CharField(null=True, blank=True, max_length=200, help_text="KYC Data")
    comment = models.CharField(null=True, blank=True, max_length=1000, help_text="Customer comments")
    
    def __str__(self):
        return '%s %s (%s)' % (self.lastname,self.firstname,self.externalID) 

    def display_fullname(self):
        return '%s %s' % (self.lastname,self.firstname)
    display_fullname.short_description = 'Customer fullname'

    class Meta:
        ordering = ["lastname"]

class Blockchain(models.Model):
    """
    Blockchain model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Object across whole app")
    name = models.CharField(max_length=100, help_text="Blochchain name")
    connection = models.CharField(null=True, blank=True, max_length=100, help_text="Blochchain connectoin")
    interval = models.IntegerField(null=True, blank=True, help_text="Blochchain refresh interval")

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('blockchain-detail', args=[str(self.id)])


class Address(models.Model):
    """
    Address model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Address")
    key = models.CharField(max_length=100, help_text="Wallet number max length is 100 chars")
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    blockchain = models.ForeignKey('Blockchain', on_delete=models.SET_NULL, null=True)
    ADDR_STATUS = (
        ('a', 'Approved'),
        ('w', 'Wait approval'),
        ('u', 'Unassigned'),
        ('r', 'Reserved'),
    )
    addrstatus = models.CharField(max_length=1, choices=ADDR_STATUS, blank=True, default='u', help_text='Address current status')

    def __str__(self):
        return '%s(%s)' % (self.key,self.blockchain.name)

    def display_customer(self):
        if self.customer is not None:
            return '%s %s' % (self.customer.lastname,self.customer.firstname)
        else:
            return None
    display_customer.short_description = 'Customer'

    def display_blockchain(self):
        return self.blockchain.name
    display_blockchain.short_description = 'Blochchain'

    class Meta:
        ordering = ["key"]

    def get_absolute_url(self):
        return reverse('address-detail', args=[str(self.id)])


class Watchlist(models.Model):
    """
    Watchlist model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the WatchList")
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    createdate = models.DateTimeField(auto_now=True)
    startdate = models.DateTimeField(null=True, blank=True)
    completedate = models.DateField(null=True, blank=True)
    result = models.CharField(null=True, blank=True, max_length=100, help_text="Result")
    WATCH_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=WATCH_STATUS, blank=True, default='a', help_text='Watch list record status')

    def __str__(self):
        return '%s(%s)-%s' % (self.address.key,self.address.token.name,self.status)


class Log(models.Model):
    """
    Log model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Log")
    createdate = models.DateField(auto_now=True)
    msg = models.CharField(max_length=100, help_text="Message")
    userlogin = models.CharField(max_length=100, help_text="UserLogin")
    objectname = models.CharField(null=True, blank=True, max_length=100, help_text="ObjectName")
    fieldname = models.CharField(null=True, blank=True, max_length=100, help_text="FieldName")
    oldvalue = models.CharField(null=True, blank=True, max_length=250, help_text="OldValue")
    newvalue = models.CharField(null=True, blank=True, max_length=250, help_text="NewValue")

    def __str__(self):
        return '%s(%s)-%s' % (self.createdate,self.userlogin,self.msg) 

    class Meta:
        ordering = ["createdate"]

class Operations(models.Model):
    """
    Operation model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Operations")
    createdate = models.DateField(null=True, blank=True, auto_now=True)
    completedate = models.DateField(null=True, blank=True)
    action = models.CharField(max_length=250, help_text="Action")
    parameter = models.CharField(max_length=250, help_text="FieldName")
    result = models.CharField(max_length=250, help_text="Result")

    def __str__(self):
        return '%s(%s)-%s' % (self.createdate,self.action,self.result) 

    class Meta:
        ordering = ["createdate"]
