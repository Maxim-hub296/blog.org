from django.urls import path

from . import views

app_name = "stories"

urlpatterns = [
    path("", views.StoriesListView.as_view(), name="list"),
    path("<int:pk>/", views.StoriesDetailView.as_view(), name="detail"),
]
