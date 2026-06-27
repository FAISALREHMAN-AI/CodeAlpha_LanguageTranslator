from django.contrib import admin
from django.urls import path, include  # 'include' lazmi import hona chahiye

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('translator_api.urls')),  # Yeh line API app ko connect karti hai
]