"""QAsite URL Configuration

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

from django.contrib import admin
from django.urls import include, path
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.views.generic import CreateView , TemplateView
import QA
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls , name = "admin"),
    path('', include('QA.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True ) , name="user-login" ),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page = "user-login") , name= "logout"),
    path('accounts/profile/', QA.views.profile , name= "profile"),
    
    path('accounts/register/', CreateView.as_view(model = User ,
                                                 form_class = auth_forms.UserCreationForm ,
                                                 success_url = "/accounts/welcome" , 
                                                 template_name = "registration\\register.html" ) , name= "register"),

    path('accounts/welcome', TemplateView.as_view(template_name = "registration\\welcome.html") , name="welcome")

]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
