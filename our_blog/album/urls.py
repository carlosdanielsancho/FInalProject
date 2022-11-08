from django.urls import path

from album import views

app_name = "album"
urlpatterns = [
    path("albums/", views.AlbumListView.as_view(), name="album-list"),
    path("album/add/", views.AlbumCreateView.as_view(), name="album-add"),
    path("album/<int:pk>/detail/", views.AlbumDetailView.as_view(), name="album-detail"),
    path("album/<int:pk>/update/", views.AlbumUpdateView.as_view(), name="album-update"),
    path("album/<int:pk>/delete/", views.AlbumDeleteView.as_view(), name="album-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),    
]
