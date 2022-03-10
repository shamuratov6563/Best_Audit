from django.urls import path
from . import views

urlpatterns = [
    path('', views.message, name='home'),
    path('upload/', views.upload_video, name='upload'),
    path('<int:pk>/edit/', views.RateUpdateView.as_view(), name='rate_edit'),
]









