from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/lead/', views.LeadListCreate.as_view()),
]