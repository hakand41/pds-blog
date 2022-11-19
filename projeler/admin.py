from django.contrib import admin
from .models import Projeler
# Register your models here.

@admin.register(Projeler)
class ProjelerAdmin(admin.ModelAdmin):
    list_display = ["author", "release_date"]
    list_display_links = ["release_date"]
    search_fields = ["title"]
    list_filter = ["release_date"]
    class Meta:
        model = Projeler
