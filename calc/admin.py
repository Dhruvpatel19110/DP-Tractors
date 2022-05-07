from django.contrib import admin

# Register your models here
from django.contrib import admin

from calc.models import Inspection, OldTractor, Stoke, Index, ContactEnquiry, Gallery_image

# Register your models here.


admin.site.register(Stoke)
admin.site.register(Index)
admin.site.register(OldTractor)
admin.site.register(Inspection)
admin.site.register(ContactEnquiry)
admin.site.register(Gallery_image)
