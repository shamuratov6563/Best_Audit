from django.urls import path
from . import views

urlpatterns = [
    path('', views.message, name='home'),
    path('<int:pk>/edit/', views.RateUpdateView.as_view(), name='rate_edit'),
]









