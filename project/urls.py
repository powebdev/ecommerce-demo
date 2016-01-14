from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ecommerce/', include('ecommerce.urls')),
    url(r'^admin/', admin.site.urls),
]
