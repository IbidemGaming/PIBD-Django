"""
PIBD URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from PIBD.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('clienti', ClientPageView.as_view(), name='clienti'),
    path('proiecte', ProiectPageView.as_view(), name='proiecte'),
    path('contracte', ContractPageView.as_view(), name='contracte'),
]