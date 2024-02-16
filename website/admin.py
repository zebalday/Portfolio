from django.contrib import admin
from .models import User, Project, Technology, Language, Framework, Software, Library, CommentProject

class AdminUser(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('username', 'email')
    search_fields = ('name','username','email', 'languages')
    ordering = ('username',)

class AdminProject(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('title', 'created_at')
    search_fields = ('languages','framework','softwares',)
    ordering = ('-created_at',)

class AdminCommentOnProject(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('author', 'project')
    search_fields = ('author','project',)
    ordering = ('-created_at',)

class AdminTechnology(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class AdminLanguage(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class AdminFramwork(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class AdminSoftware(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class AdminLibrary(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# Register your models here.
admin.site.register(User, AdminUser)
admin.site.register(Project, AdminProject)
admin.site.register(CommentProject, AdminCommentOnProject)
admin.site.register(Technology, AdminTechnology)
admin.site.register(Language, AdminLanguage)
admin.site.register(Framework, AdminFramwork)
admin.site.register(Software, AdminSoftware)
admin.site.register(Library, AdminLibrary)

