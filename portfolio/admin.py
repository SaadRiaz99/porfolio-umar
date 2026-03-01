from django.contrib import admin
from .models import Contact_message
from django.contrib import admin


admin.site.site_header = "Umar Bin Riaz Portfolio Admin"


admin.site.site_title = "Portfolio Admin"


admin.site.index_title = "Welcome to My Portfolio Admin"

admin.site.register(Contact_message)
















