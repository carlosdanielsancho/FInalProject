from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False)
    performer = models.CharField(max_length=60, null=False, blank=False)
    release = models.IntegerField()
    genre = models.CharField(max_length=15)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='album', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "title",
            "performer",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Album: {self.title} | performer: {self.performer}"


class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)