"""cheatsheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# we are importing the func we created in our app from the views section
from notes.views import get_notes 
from notes.views import get_id_note

urlpatterns = [ 
    # thses urls connect with the views 
    # so whenever we clic on it, it will take us to the assigend url
    path('admin/', admin.site.urls),
    path('MYnotes/',get_notes),
    path("MYnote_detail/<int:note_id>",get_id_note),
    path('home/', TemplateView.as_view(template_name = "base.html")),
]
