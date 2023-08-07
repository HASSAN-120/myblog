from django.contrib import admin
from .models import Post, ContactMessage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ['name', 'email', 'message']
    readonly_fields = ('created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)

