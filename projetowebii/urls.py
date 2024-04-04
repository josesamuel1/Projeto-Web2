from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from appEstoque.api.router import post_router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appEstoque.urls')),
    path('api/', include(post_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
