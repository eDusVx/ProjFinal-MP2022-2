from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name="index"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('funcionarios/', views.home, name="home"),
    path('mesa/<str:pk_test>/', views.numero_mesa, name="customer"),
    path('chose_table/', views.chose_table, name="chose_table"),
    path('chose_table/<str:pk>/', views.chose_table, name="chose_table"),
    path('update_order/<str:pk>/', views.atualizar_pedido, name="update_order"),
    path('registrar_pedido/', views.registrar_pedido, name="registrar_pedido"),
    path('fechar_pedido/', views.fechar_pedido, name="fechar_pedido"),
    path('delete_order/<str:pk>/', views.deletar_pedido, name="delete_order"),
    # path('api/', include((router.urls, 'app_name'))),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
