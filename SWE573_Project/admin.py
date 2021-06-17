from django.contrib import admin
from SWE573_Project.models import TagModel, ArticleModel, ReportModel



class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(TagModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body')
    list_display = (
        'title', 'publish_date'
    )
    list_filter = ('publish_date',)

admin.site.register(ArticleModel, ArticleAdmin)

class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = ('name', 'email', 'date',)



admin.site.register(ReportModel)