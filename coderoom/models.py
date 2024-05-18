from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

# Create your models here.


class CodeRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coderoom")
    name = models.CharField(max_length=50)
    description = models.TextField()
    github_repo = models.CharField(max_length=500)
    primary_programming_language = models.CharField(max_length=500)
    slug = models.SlugField(default="", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    # def __str__(self):
    #     self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CodeRoom, self).save(*args, **kwargs)
