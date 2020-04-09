"""
admin decorator 대신
admin.site.register(Bookmark, BookmarkAdmin)
을 지정해 줄 수 있습니다.
"""
from django.contrib import admin
from bookmark.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
