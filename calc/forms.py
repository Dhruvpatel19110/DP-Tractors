from telnetlib import RCP
from django import forms
from calc import models
from calc.models import Gallery_image, OldTractor


class OldTracktorForm(forms.ModelForm):
    upload = forms.ImageField(required = True)
    name =forms.CharField()
    HP = forms.IntegerField()
    Manufacturingyear =forms.IntegerField()
    Regno =forms.CharField()
    RC = forms.CharField()
    price = forms.IntegerField()
    Hours = forms.IntegerField()
    Registeryear =forms.IntegerField()
    Detail = forms.CharField()
    RTOName = forms.CharField()
    OwnerNumber =forms.IntegerField()
    VehicalMake =forms.CharField()
    # Color = forms.CharField(max_length=6, blank=True, null=True)
    ChassisNo =forms.CharField()
    EngineNo = forms.CharField()
    RCStatus = forms.CharField()
    Capacity =  forms.IntegerField()
    Trollyhook =forms.CharField()
    # color1 = forms.CharField(max_length=10, blank=True, null=True)
    Rightside_Photo = forms.ImageField()
    Leftside_Photo =  forms.ImageField()
    Meter_Photo =  forms.ImageField()
    # Front_Photo = forms.ImageField(, blank=True, null=True)
    Back_Photo =  forms.ImageField()
    Tyare1_Photo =  forms.ImageField()
    TyareLife1 =forms.IntegerField()
    Tyare2_Photo =   forms.ImageField()
    TyareLife2 = forms.IntegerField()
    Tyare3_Photo =   forms.ImageField()
    TyareLife3 =  forms.IntegerField()
    Tyare4_Photo =   forms.ImageField()
    TyareLife4 =  forms.IntegerField()
    Engine1_Photo =   forms.ImageField()
    Video = forms.FileField()
    # Min_Prize =  forms.IntegerField()
    
    class Meta:
        model = OldTractor
    
        fields = '__all__'
    #     business_name = forms.CharField()
    # tax_id = forms.CharField()
    # store = forms.CharField()
    # email = forms.EmailField()
    # confirm_email = forms.EmailField()
    # password = forms.CharField()
    # confirm_password = forms.CharField()
    # phone_number = forms.CharField(max_length=13)
    # zipcode = forms.CharField()

class AddGalleryForm(forms.ModelForm):
    upload1 = forms.ImageField(required = True)

    
    class Meta:
        model = Gallery_image
    
        fields = '__all__'

