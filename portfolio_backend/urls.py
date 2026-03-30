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

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'achievements', AchievementViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/contact/', ContactSubmitView.as_view(), name='contact-submit'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('projects.html', TemplateView.as_view(template_name='projects.html'), name='projects'),
    path('contact.html', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('achievements.html', TemplateView.as_view(template_name='achievements.html'), name='achievements'),
]

# Serve static files from root during development
if settings.DEBUG:
    urlpatterns += static('/', document_root=settings.BASE_DIR)
