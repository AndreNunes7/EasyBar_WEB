from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Api.Views import cadastrar, get_cadastros_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Api.urls'), name='api_rest_urls'),
    # login:
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     # Cadastro: 
    path('api/cadastrar/', cadastrar, name='signup'),  
    path('api/cadastrosAll/', get_cadastros_all, name='secure_data'), 
]
