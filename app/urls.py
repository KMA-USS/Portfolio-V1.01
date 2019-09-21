from django.urls import path, include
from .views import HomeView, ProjectDetail


urlpatterns = [
    path('', HomeView.as_view(), name='portfolio'),
    path('project/<str:slug>/details/', ProjectDetail.as_view(), name='projectdetail'),
]
