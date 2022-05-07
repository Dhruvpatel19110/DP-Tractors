from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class Stoke(models.Model):
    No = models.CharField(max_length=2, blank=True, null=True)
    TractorName = models.CharField(max_length=50, blank=True, null=True)
    HP = models.CharField(max_length=2, blank=True, null=True)
    Model = models.CharField(max_length=4, blank=True, null=True)
    RTO = models.CharField(max_length=2, blank=True, null=True)
    RegistrationNO = models.CharField(max_length=20, blank=True, null=True)
    RCBook = models.CharField(max_length=3, blank=True, null=True)
    KMDriven = models.CharField(max_length=4, blank=True, null=True)
    ChassisNumber = models.CharField(max_length=20, blank=True, null=True)
    Details = models.CharField(max_length=20, blank=True, null=True)

    # class Meta:
    #     db_table=""

    def __str__(self):
        return str(self.TractorName)


class Index(models.Model):
    upload = models.ImageField(upload_to='images', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    HP = models.CharField(max_length=2, blank=True, null=True)
    dest = models.CharField(max_length=100, blank=True, null=True)
    urls = models.CharField(max_length=200, blank=True, null=True)

    # RC = models.CharField(max_length=3, blank=True, null=True)
    # KMDriven = models.CharField(max_length=4, blank=True, null=True)
    # ChassisNumber = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class OldTractor(models.Model):
    # objects = None
    is_sold_out = models.BooleanField(default=False)
    upload = models.ImageField()
    name = models.CharField(max_length=50, blank=True, null=True)
    HP = models.IntegerField(blank=True, null=True)
    Manufacturingyear = models.IntegerField(blank=True, null=True)
    Regno = models.CharField(max_length=10, blank=True, null=True)
    RC = models.CharField(max_length=3, blank=True, null=True)
    price = models.CharField(max_length=6, blank=True, null=True)
    Hours = models.IntegerField(blank=True, null=True)
    Registeryear = models.IntegerField(blank=True, null=True)
    Detail = models.CharField(max_length=100, blank=True, null=True)
    RTOName = models.CharField(max_length=20, blank=True, null=True)
    OwnerNumber = models.IntegerField(blank=True, null=True)
    VehicalMake = models.CharField(max_length=10, blank=True, null=True)
    # Color = models.CharField(max_length=6, blank=True, null=True)
    ChassisNo = models.CharField(max_length=20, blank=True, null=True)
    EngineNo = models.CharField(max_length=20, blank=True, null=True)
    RCStatus = models.CharField(max_length=3, blank=True, null=True)
    Capacity = models.IntegerField(blank=True, null=True)
    Trollyhook = models.CharField(max_length=10, blank=True, null=True)
    color1 = models.CharField(max_length=10, blank=True, null=True)
    Rightside_Photo = models.ImageField()
    Leftside_Photo = models.ImageField()
    Meter_Photo = models.ImageField()
    # Front_Photo = models.ImageField(upload_to='images', blank=True, null=True)
    Back_Photo = models.ImageField()
    Tyare1_Photo = models.ImageField()
    TyareLife1 = models.IntegerField(blank=True, null=True)
    Tyare2_Photo = models.ImageField()
    TyareLife2 = models.IntegerField(blank=True, null=True)
    Tyare3_Photo = models.ImageField()
    TyareLife3 = models.IntegerField(blank=True, null=True)
    Tyare4_Photo = models.ImageField()
    TyareLife4 = models.IntegerField(blank=True, null=True)
    Engine1_Photo = models.ImageField()
    Video = models.FileField(upload_to='videos_uploaded')

    # Min_Prize = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Inspection(models.Model):
    name1 = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return str(self.name1)


class stokedata:
    No: int
    TractorName: str
    HP: int
    Model: int
    RTO: str
    RegistrationNo: str
    RCBook: str
    KMDriven: int
    ChassisNumber: str
    Details: str
    image: str


class NewUserForm(UserCreationForm):
    email = models.EmailField(max_length=70, blank=True, unique=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def save(self, commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user




class ContactEnquiry(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    Phone_number = models.IntegerField(blank=True, null=True)
    Village_name = models.CharField(max_length=50, blank=True, null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Gallery_image(models.Model):
    upload1 = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return str(self.upload1)
