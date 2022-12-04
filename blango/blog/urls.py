from django.urls import path

from .views import index, post_detail

urlpatterns = [
    path("<slug:slug>", post_detail.as_view(), name="post_detail"),
    path("", index.as_view(), name="post_list"),
]