from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError


"""
===============
    LANGUAGE
===============
-Name
-Created At
-Updated At
"""
class Language(models.Model):
    # Info
    name = models.CharField(
        verbose_name = "Name",
        max_length = 100,
        unique = True,
        blank = False,
        null = False,
    )
    # Backend & Frontend
    is_backend = models.BooleanField(
        verbose_name = "Is Backend?",
        default = False,
        null = True,
        blank = True,
    )
    is_frontend = models.BooleanField(
        verbose_name = "Is Frontend?",
        default = False,
        null = True,
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
    # Info
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Backend & Frontend
    is_backend = models.BooleanField(
        verbose_name = "Is Backend?",
        default = False,
        null = True,
        blank = True,
    )
    is_frontend = models.BooleanField(
        verbose_name = "Is Frontend?",
        default = False,
        null = True,
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
    # Info
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Backend & Frontend
    is_backend = models.BooleanField(
        verbose_name = "Is Backend?",
        default = False,
        null = True,
        blank = True,
    )
    is_frontend = models.BooleanField(
        verbose_name = "Is Frontend?",
        default = False,
        null = True,
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
    # Info
    name = models.CharField(
        max_length = 100,
        verbose_name = "Name",
        unique = True,
        blank = False,
        null = False,
    )
    # Backend & Frontend
    is_backend = models.BooleanField(
        verbose_name = "Is Backend?",
        default = False,
        null = True,
        blank = True,
    )
    is_frontend = models.BooleanField(
        verbose_name = "Is Frontend?",
        default = False,
        null = True,
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
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Software"
        verbose_name_plural = "Softwares"
        ordering = ["name"]


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
    # Backend & Frontend
    is_backend = models.BooleanField(
        verbose_name = "Is Backend?",
        default = False,
        null = True,
        blank = True,
    )
    is_frontend = models.BooleanField(
        verbose_name = "Is Frontend?",
        default = False,
        null = True,
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
        return self.name
    
    #Meta Class
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
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
    # Info
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
    libraries = models.ManyToManyField(
        Library,
        verbose_name="Liked Libraries",
        blank = True,
    )
    softwares = models.ManyToManyField(
        Software,
        verbose_name="Liked Softwares",
        blank = True,
    )
    technologies = models.ManyToManyField(
        Technology,
        verbose_name="Liked Technologies",
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
        #ordering = ["username"]


"""
===============
    Project
===============
- Title
- Brief Description (For thumbnail purposes)
- Description
- Image (Thumbnail)
- Languages
- Frameworks
- Libraries
- Software
- Technologies
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
        upload_to="Portfolio/projectsthumbnails/",
        null = True,
        blank= True
    )

    # Links
    github_url = models.URLField(
        verbose_name = "GitHub Repository",
        max_length = 250,
        editable = True,
        blank = True,
        null = True
    )
    project_url = models.URLField(
        verbose_name = "Project Link",
        max_length = 250,
        editable = True,
        blank = True,
        null = True
    )

    # FK's
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
    technologies = models.ManyToManyField(
        Technology,
        verbose_name="Used Technologies",
        blank = True,
    )
    
    # Public / Visible
    is_public = models.BooleanField(
        verbose_name = "Show this project?",
        default = False,
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


# Creates different folder for each created project
def get_image_upload_path(instance, filename):
    # Define the upload path based on the property_id
    upload_path = f"Portfolio/projectimages/project{instance.project.id}/{filename}"
    return upload_path

# Validates image max size (3MB)
def validate_image_size(value):
    if value.size > 1024 * 1024 * 3:
        raise ValidationError("Image's too big (Max. 3 mb). Compress it.")
    

"""
=================================
    PROJECT IMAGE CLASS MODEL
=================================
- Project FK
- Image
"""
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        verbose_name = "Project Images",
        on_delete = models.CASCADE,
        blank=False,
        null=False
    )
    image = models.ImageField(
        upload_to= get_image_upload_path,
        validators=[validate_image_size],
        null = True,
        blank= True
    )
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


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
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
        verbose_name = "Project",
        null = False,
    )
    content = models.TextField(
        max_length = 250,
        verbose_name = "Content",
        blank = False,
        null = False,
        editable = False
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


"""
======================
    CERTIFICATION
======================
- Institution
- Course
- Year
- Link
- Language
- Framework

"""
class Certification(models.Model):
    
    institution = models.CharField(
        verbose_name = "Institution",
        max_length = 100,
        blank = False,
        editable = True
    )
    course = models.CharField(
        verbose_name = "Course name",
        max_length = 150,
        blank = False,
        editable = True
    )
    year = models.PositiveIntegerField(
        verbose_name = "Year issued",
        blank = False,
        editable = True
    )
    link = models.URLField(
        verbose_name = "Certificate / Course link",
        max_length = 250,
        blank = False,
        editable = True
    )

    # FK's
    languages = models.ManyToManyField(
        Language,
        verbose_name="Used Languages",
        blank = True,
    )
    frameworks = models.ManyToManyField(
        Framework,
        verbose_name="Used Frameworks",
        blank = True,
    )
    libraries = models.ManyToManyField(
        Library,
        verbose_name="Used libraries",
        blank = True,
    )
    
    # Public / Visible
    is_public = models.BooleanField(
        verbose_name = "Show this certificate?",
        default = False,
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

    def __str__(self) -> str:
        return (f"{self.course} - {self.institution} - [{self.year}]")

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ["-year"]