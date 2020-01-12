from django.urls import path
from .views import HomePageView

urlpatterns = [
    ('', HomePageView.as_view(), name='home'),
]
