"""
URL configuration for django_senai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import re_path, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from mycontacts import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.show),
    re_path(r'^add/', views.add),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('delete/<int:contact_id>/', views.delete, name='delete_contact'),
    path('edit/<int:id>/', views.editar, name='edit_contact'),
    path('update/<int:id>/', views.update, name='update_contact'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
