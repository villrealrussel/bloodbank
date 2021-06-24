from django.contrib import admin
from .models import donor, blooddetails, bloodbank, hospital, employee, bloodrequest
# Register your models here.
admin.site.register(donor)
admin.site.register(blooddetails)
admin.site.register(bloodbank)
admin.site.register(hospital)
admin.site.register(employee)
admin.site.register(bloodrequest)