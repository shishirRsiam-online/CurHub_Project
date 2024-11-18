from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


from . import views as Project_Views
from Authenticator_App import views as Authenticator_App_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Brand_App.urls')),
    path('', include('CurHub_App.urls')),

    path('profile/', Authenticator_App_Views.profile, name='profile'),
    path('edit/profile/', Authenticator_App_Views.edit_profile, name='edit_profile'),
    path('edit/password/', Authenticator_App_Views.change_password, name='change_password'),
    path('login/', Authenticator_App_Views.login_page, name='login'),
    path('logout/', Authenticator_App_Views.logout_page, name='logout'),
    path('signup/', Authenticator_App_Views.signup_page, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)