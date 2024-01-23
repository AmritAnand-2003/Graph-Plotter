from django.urls import path
from . import views

urlpatterns = [
    path("", views.front, name="front"),
    path("q21/", views.matchq1, name="q21"),
    path("q11/", views.schoolq1, name="q11"),
    path("q12/", views.schoolq2, name="q12"),
    path("q13/", views.schoolq3, name="q13"),
    path("q22/", views.matchq2, name="q22")
    # path("<int:match_id>/", views.detail, name="detail"),
    # path("<int:match_id>/results", views.results, name="results")
]