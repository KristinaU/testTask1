from django.urls import include, path
from rest_framework import routers
from myapp import views
from myapp.views import RegistrationAPIView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('registration/', RegistrationAPIView.as_view(), name='registration')
]