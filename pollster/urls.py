from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages_app.urls')),
    path('polls/', include('polls_app.urls')),
    path('admin/', admin.site.urls),
]
