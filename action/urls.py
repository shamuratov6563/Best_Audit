from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.message, name='home'),
    path('upload/', views.upload_video, name='upload'),
    path('create/', views.RateCreateView.as_view(), name='rate_new'),
    path('<int:pk>/', views.RateDetailView.as_view(), name='rate_detail'),
    path('<int:pk>/edit/', views.RateUpdateView.as_view(), name='rate_edit'),
    path('<int:pk>/delete/', views.RateDeleteView.as_view(), name='rate_delete'),
]





