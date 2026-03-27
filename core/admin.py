from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import MenuItem, BlogPost, Reservation



@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'time', 'guests')
    list_filter = ('date',)
    search_fields = ('full_name', 'email')
    ordering = ('-date',)
    date_hierarchy = 'date'



admin.site.site_header = "AUREVO Administration"