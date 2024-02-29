from django.contrib import admin
from .models import User, Project, ProjectImage, Technology, Language, Framework, Software, Library, CommentProject, Certification
from .forms import ProjectImageForm


class AdminUser(admin.ModelAdmin):
    model = User
    readonly_fields = ('created_at','updated_at')
    list_display = ('username', 'email')
    search_fields = ('name','username','email', 'languages')
    ordering = ('username',)

class AdminInlineImages(admin.TabularInline):
    readonly_fields=['project']
    model = ProjectImage
    form = ProjectImageForm

class AdminProject(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('title', 'created_at')
    search_fields = ('languages','framework','softwares',)
    ordering = ('-created_at',)
    inlines = [AdminInlineImages,]


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

class AdminFramework(admin.ModelAdmin):
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

class AdminCertification(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('institution', 'course', 'year',)
    search_fields = ('course', 'institution',)
    ordering = ('-year',)

# Register your models here.
#admin.site.unregister(UserBase)
admin.site.register(User, AdminUser)
admin.site.register(Project, AdminProject)
admin.site.register(CommentProject, AdminCommentOnProject)
admin.site.register(Technology, AdminTechnology)
admin.site.register(Language, AdminLanguage)
admin.site.register(Framework, AdminFramework)
admin.site.register(Software, AdminSoftware)
admin.site.register(Library, AdminLibrary)
admin.site.register(Certification, AdminCertification)

