from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from academy.views import make_admin_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academy.urls')), # This connects your app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)