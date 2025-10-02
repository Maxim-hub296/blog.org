from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListView.as_view(), name="list"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="detail"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("excerpts/", views.ExcerptsListView.as_view(), name="excerpts"),
]