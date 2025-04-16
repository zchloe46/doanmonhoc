"""
URL configuration for doanmonhoc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from dashboard.views import dashboard_view, result_view, classify_view, tokenize_view, pos_tag_view, about_view, test_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('contact/', contact_view, name='contact'),
    path('ketqua/', result_view, name='ketqua'),
    path('about/', about_view, name='about'),
    path('classify/', classify_view, name='classify'),
    path('tokenize/', tokenize_view, name='tokenize'),
    path('pos_tag/', pos_tag_view, name='pos_tag'),
    path('test/', test_view, name='test'),
]
