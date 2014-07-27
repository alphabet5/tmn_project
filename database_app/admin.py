from django.contrib import admin
from database_app.models import tmn

class tmnAdmin(admin.ModelAdmin):
    list_display = ("Structure", "Metal", "Lattice_Constant", "Bulk_Modulus", "C11_elastic_constant", "C12_elastic_constant", "C44_elastic_constant", "Experimental", "Stable", "Is_with_spin", "Potential", "Wave_function", "Code_Package", "Reference_DOI", "Comment", "Verified")
    list_filter = ["Structure", "Metal", "Experimental", "Stable", "Is_with_spin", "Potential", "Verified"]
admin.site.register(tmn, tmnAdmin)