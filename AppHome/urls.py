from django.urls import path

from .views import *

urlpatterns = [
    path('',pageHome,name="pageAcceuil"),
    path('dowload/',dowload_cv,name="dowload_cv"),
]
