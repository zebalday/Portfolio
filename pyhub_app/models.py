from django.db import models

class GithubUser(models.Model):
    username = models.CharField(
        verbose_name = "Username",
        max_length = 150,
        blank = False,
        null = False,
        editable = False
    )
    github_url = models.URLField(
        verbose_name = "Github Profile",
        max_length = 250,
        blank = False,
        null = False,
        editable = False
    )
    github_thumbnail = models.URLField(
        verbose_name = "Github Thumbnail",
        max_length = 250,
        blank = False,
        null = False,
        editable = False
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Created on"
    )
    
    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name = "Github User"
        verbose_name_plural = "Github Users"
        ordering = ["-created_at"]