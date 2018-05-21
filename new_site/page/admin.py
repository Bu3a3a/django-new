from django.contrib import admin
from .models import Article, Firm
from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget


class FirmAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }

admin.site.register(Firm, FirmAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
