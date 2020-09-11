from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from rest_framework import routers

from result.views import CompanyViewSet


router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)  # basename='company'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('result.urls')),

    path('', RedirectView.as_view(pattern_name='company:index')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
