from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.views.static import serve
import lin_lout
from  lin_lout import urls
import dashboard.urls
import allinone
import allinone.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(lin_lout.urls) ),
    path("dashboard/", include(dashboard.urls)),
    path("allinone/", include(allinone.urls)),
]

