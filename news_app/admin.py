from django.contrib import admin
from news_app.models import News, Category, Contact

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_time', 'status']
    list_filter = ['status', 'created_time', 'published_time']
    prepopulated_fields = {"slug": ("title",)}