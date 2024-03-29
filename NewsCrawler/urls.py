from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        '',
        include('dashboard.urls')),
    path(
        'trangWeb/',
        include('trangWeb.urls')),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='base/login.html'),
        name='login'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='base/logout.html'),
        name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
