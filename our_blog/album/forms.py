from ckeditor.widgets import CKEditorWidget
from django import forms

from album.models import Album


class AlbumForm(forms.ModelForm):
    title = forms.CharField(
        label="Nombre del album",
        max_length=60,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-name",
                "placeholder": "Nombre de album",
                "required": "True",
            }
        ),
    )

    performer = forms.CharField(
        label="Interprete del album",
        max_length=60,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "performer-name",
                "placeholder": "Nombre de Interprete",
                "required": "True",
            }
        ),
    )

    release = forms.IntegerField(
        label="Lanzamiento:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-release",
                "placeholder": "Año de lanzamiento",
                "required": "True",
            }
        ),
    )

    genre = forms.IntegerField(
        label="Género:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-genre",
                "placeholder": "Género",
                "required": "True",
            }
        ),
    )
    
    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField()

    class Meta:
        model = Album
        fields = ["title", "performer", "release", "genre", "description", "image"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )