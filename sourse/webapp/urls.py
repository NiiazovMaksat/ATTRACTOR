from django.urls import path

from webapp.views import view_index, create_articles_view

urlpatterns = [
    path('', view_index),
    path('articles/add/', create_articles_view),
]