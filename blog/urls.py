from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    UserPostListView,
    about,
    contact,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"),
    path('post/new/', PostCreateView.as_view(), name="blog-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path("about/", about, name="blog-about"),
    path("contact/", contact, name="blog-contact"),
]
