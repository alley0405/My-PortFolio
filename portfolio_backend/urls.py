"""
URL configuration for portfolio_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact_form.views import ContactSubmitView
from portfolio_core.views import AchievementViewSet, ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register(r'achievements', AchievementViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/contact/', ContactSubmitView.as_view(), name='contact-submit'),
]
