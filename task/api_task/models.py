from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=264)
    owner = models.ForeignKey(
        'auth.User',
        related_name='projects',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    owner = models.ForeignKey(
        'auth.User',
        related_name='tasks',
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(
        default=timezone.now
    )
    edit_date = models.DateTimeField(
        default=timezone.now
    )
    deadline = models.DateTimeField()
    done = models.BooleanField(
        default=False
    )
    project = models.ForeignKey(
        Project,
        null=True,
        blank=True,
        related_name='tasks',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('created_date', 'deadline')

    def __str__(self):
        return self.title



