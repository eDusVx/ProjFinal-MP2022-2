from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('funcionarios/', views.home, name="home"),
    path('mesa/<str:pk_test>/', views.numero_mesa, name="customer"),
    path('update_order/<str:pk>/', views.atualizar_pedido, name="update_order"),
    path('registrar_mesa/', views.registrar_mesa, name="registrar_mesa"),
    path('delete_order/<str:pk>/', views.deletar_pedido, name="delete_order"),
    # path('api/', include((router.urls, 'app_name'))),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
