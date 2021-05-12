from django.contrib import admin
from SWE573_Project.models import TagModel, ArticleModel

admin.site.register(TagModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'publish_date'
    )

admin.site.register(ArticleModel, ArticleAdmin)