from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientesapp.urls')),
    path('clients/metrics/', include('django_prometheus.urls'))

]
