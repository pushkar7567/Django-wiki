from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.new_page, name="newpage"),
    path("<str:TITLE>", views.load_title, name="title")
]

