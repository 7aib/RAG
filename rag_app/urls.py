# rag_app/urls.py

from django.urls import path

from rag_app.views import home

urlpatterns = [
    path('', home, name='home'),
]