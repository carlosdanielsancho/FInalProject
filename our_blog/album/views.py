from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from album.forms import CommentForm
from album.forms import AlbumForm
from album.models import Comment
from album.models import Album

class AlbumListView(ListView):
    model = Album
    paginate_by = 3


class AlbumDetailView(DetailView):
    model = Album
    template_name = "album/album_detail.html"
    fields = ["title", "performer", "release", "genre", "description", "image"]

    def get(self, request, pk):
        album = Album.objects.get(id=pk)
        comments = Comment.objects.filter(album=album).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "album": album,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    success_url = reverse_lazy("album:album-list")

    form_class = AlbumForm
    # fields = ["title", "performer", "release", "genre", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate albums"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Album.objects.filter(
            title=data["title"], performer=data["performer"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El disco {data['title']} - de {data['performer']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Album {data['title']} - de {data['performer']} creado exitosamente!",
            )
            return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ["title", "performer", "release", "genre", "description", "image"]

    def get_success_url(self):
        album_id = self.kwargs["pk"]
        return reverse_lazy("album:album-detail", kwargs={"pk": album_id})

    def post(self):
        pass


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy("album:album-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        album = get_object_or_404(Album, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, album=album
        )
        comment.save()
        return redirect(reverse("album:album-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        album = self.object.album
        return reverse("album:album-detail", kwargs={"pk": album.id})