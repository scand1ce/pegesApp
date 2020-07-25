from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),  # new 25.07.2020 /*/ 20:47
    path('', HomePageView.as_view(), name='home'),
]
