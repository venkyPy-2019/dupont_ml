from django.contrib import admin
from .models import researchUpdate, MachineLearningModelReference, Contact

# Register your models here.
admin.site.site_header = "DUPONT"
admin.site.index_title = "DUPONT ADMINISTRATION"
admin.site.site_title = "DUPONT"

admin.site.register(researchUpdate)
admin.site.register(MachineLearningModelReference)
admin.site.register(Contact)
