from django.contrib import admin
from posts.models import Post, Category, Tag

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "rate", "created_at")
    list_filter = ("category", "tag")
    search_fields = ("title", "description", "tags__name")

admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
