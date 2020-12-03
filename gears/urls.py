from django.urls import path

from gears.views import landing_page

urlpatterns = [
    path('', landing_page),
]
