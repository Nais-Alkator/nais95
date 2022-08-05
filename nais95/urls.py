from django.contrib import admin
from django.urls import path
from input.views import get_main, get_inputs
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_main),
    path('inputs', get_inputs),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
