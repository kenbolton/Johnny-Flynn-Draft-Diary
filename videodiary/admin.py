from django.contrib import admin
from videodiary.models import Ad, Post, Category#, GalleryUpload, ConvertVideo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'video_count', 'is_header', 'is_public', )
    list_filter = ['date_added', 'is_public', 'is_header']
    date_hierarchy = 'date_added'
    list_editable = ('is_public', 'is_header')
    prepopulated_fields = {'title_slug': ('title',)}
    filter_horizontal = ('videos',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'is_public', 'tags', 'duration', 'h264_video', 'admin_thumbnail', )
    list_filter = ['date_added', 'is_public']
    list_editable = ('is_public', 'date_added', )
    list_per_page = 10
    prepopulated_fields = {'title_slug': ('title',)}
    exclude = ('crop_from', 'effect', 'image', 'duration', 'flv_video', 'podcast_video', 'h264_video')

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'date_taken', 'date_added', 'is_public', 'tags', 'view_count', 'flv_video', 'admin_thumbnail', )
    list_filter = ['date_added', 'is_public']
    list_editable = ('is_public',)
    list_per_page = 10
    prepopulated_fields = {'title_slug': ('title',)}
    exclude = ('crop_from', 'effect', 'image', 'duration', 'flv_video', 'podcast_video', 'h264_video')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Ad, AdAdmin)