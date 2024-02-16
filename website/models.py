from django.db import models
from ckeditor.fields import RichTextField



"""
==================
    TECHNOLOGY
==================
-Name
-Created At
-Updated At
"""
class Technology(models.Model):
    #Text
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated on"
    )

    # Functions
    def __str__(self) -> str:
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ["name"]


"""
===============
    LANGUAGE
===============
-Name
-Created At
-Updated At
"""
class Language(models.Model):
    #Text
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated on"
    )

    # Functions
    def __str__(self) -> str:
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        ordering = ["name"]


"""
==================
    FRAMEWORK
==================
-Name
-Created At
-Updated At
"""
class Framework(models.Model):
    #Text
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated on"
    )

    # Functions
    def __str__(self) -> str:
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Framework"
        verbose_name_plural = "Frameworks"
        ordering = ["name"]


"""
================
    LIBRARY
================
-Name
-Created At
-Updated At
"""
class Library(models.Model):
    #Text
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated on"
    )

    # Functions
    def __str__(self) -> str:
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"
        ordering = ["name"]


"""
==================
    SOFTWARE
==================
-Name
-Created At
-Updated At
"""
class Software(models.Model):
    #Text
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated on"
    )

    # Functions
    def __str__(self) -> str:
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Softwares"
        ordering = ["name"]


"""
===========
    USER
===========
- Full name
- Username
- Email
- Password
- Interests (Related to Interest MODEL)
"""
class User(models.Model):
    # Text
    full_name = models.CharField(
        max_length = 150,
        verbose_name="Full name",
        blank = False,
        null = False,
    )
    username = models.CharField(
        max_length = 50,
        verbose_name="Username",
        unique = True,
        blank = False,
        null = False,
    )
    email = models.EmailField(
        unique = True,
        verbose_name="Email address",
        blank = False,
        null = False,
    )
    password = models.CharField(
        max_length = 50,
        verbose_name="Password",
        blank = False,
        null = False,
    )
    technologies = models.ManyToManyField(
        Technology,
        verbose_name="Liked Technologies",
        blank = True,
    )
    languages = models.ManyToManyField(
        Language,
        verbose_name="Liked Languages",
        blank = True,
    )
    framework = models.ManyToManyField(
        Framework,
        verbose_name="Liked Frameworks",
        blank = True,
    )
    # Datetime
    created_at = models.DateTimeField(
        verbose_name = "Created on",
        auto_now_add = True,
    )
    updated_at = models.DateTimeField(
        verbose_name = "Updated on",
        auto_now = True,
    )

    # Functions
    def __str__(self) -> str:
        return self.full_name
    
    # Meta Class
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]


"""
===============
    Project
===============
- Title
- Brief Description (For thumbnail purposes)
- Description
- Image (Thumbnail)
- Technologies (Associated)
- Created At
- Updated At
"""
class Project(models.Model):
    # Text
    title = models.CharField(
        max_length = 150,
        verbose_name= "Title",
        blank = False,
        null = False,
        editable = True
    )
    short_description = models.CharField(
        max_length = 200,
        verbose_name= "Short description",
        blank = False,
        null = False,
        editable = True
    )
    description = RichTextField(
        verbose_name= "Description",
        blank = False,
        null = False,
        editable = True
    )
    thumbnail = models.ImageField(
        verbose_name="Thumbnail",
        upload_to="ProjectThumbnails/",
        null = True,
        blank= True
    )

    # FK's
    technologies = models.ManyToManyField(
        Technology,
        verbose_name="Used Technologies",
        blank = True,
    )
    languages = models.ManyToManyField(
        Language,
        verbose_name="Used Languages",
        blank = True,
    )
    framework = models.ManyToManyField(
        Framework,
        verbose_name="Used Frameworks",
        blank = True,
    )
    libraries = models.ManyToManyField(
        Library,
        verbose_name="Used Libraries",
        blank = True,
    )
    softwares = models.ManyToManyField(
        Software,
        verbose_name="Used Softwares",
        blank = True,
    )

    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Updated on"
    )

    # Functions
    def __str__(self) -> str:
        return self.title
    
    # Meta Class
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["title"]


"""
=========================
    COMMENT ON PROJECT
=========================
- Author FK
- Content
- Project FK
- Created At
- NON-Editable
"""
class CommentProject(models.Model):
    # Info
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        verbose_name = "Author",
        blank = False,
        null = False,
    )
    content = models.TextField(
        max_length = 250,
        verbose_name = "Content",
        blank = False,
        null = False,
        editable = False
    )
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
        verbose_name = "Project",
        null = False,
    )
    # Datetime
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )

    # Functions
    def __str__(self) -> str:
        return (f"{self.author.username} comment on {self.project.title}")
    
    # Meta Class
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created_at"]


