from django.contrib import admin
from models import Page, PageClass, LANGUAGE_LIST


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    first_fields = ['title', ]
    markdown_fields = []
    for lang in LANGUAGE_LIST:
        first_fields.append('content_' + lang)
        markdown_fields.append('markdown_content_' + lang)

    fieldsets = (
        (None, {'fields': first_fields}),
        ('Markdown', {
            'fields': markdown_fields,
            'classes': ('collapse',)
        }),
    )


class PageClassAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Page, PageAdmin)
admin.site.register(PageClass, PageClassAdmin)
