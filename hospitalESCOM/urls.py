from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("core.urls")),
    path('operation/', include("operation.urls")),
    path('admin/', admin.site.urls),
]
