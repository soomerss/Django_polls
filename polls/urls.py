from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.PollsListView.as_view(), name="index"),
    path("<int:pk>/", views.PollsDetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.results, name="results"),
    path("<int:pk>/vote", views.vote, name="vote"),
]
