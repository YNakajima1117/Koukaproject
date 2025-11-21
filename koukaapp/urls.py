from django.urls import path
from . import views

app_name="koukaapp"
urlpatterns = [
    path("",views.MainView.as_view(),name="main"),
    path("content/",views.ContentView.as_view(),name="content"),
    path("detail/<int:pk>/",views.ChildDetailView.as_view(),name="detail"),
    ]