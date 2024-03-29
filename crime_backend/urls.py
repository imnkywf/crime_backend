"""crime_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from App.models import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App.views.user_views import *
from App.views.profile_views import *
from App.views.avatar_views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', User_Profile.as_view()),
    path('update-profile/', Update_Profile.as_view()),
    path('avatar/', Avatar.as_view()),
    path('upload-avatar/', Upload_Avatar.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.AVATAR_URL, document_root=settings.MEDIA_ROOT)

