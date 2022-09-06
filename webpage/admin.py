from django.contrib import admin
from .models import Garcon, Pedido, Mesa, Prato, Ingrediente, Estoque, prato_has_ingrediente, pedido_has_prato, pratoIAdmin, pedidoAdmin

admin.site.register(Garcon)
# admin.site.register(Pedido)
admin.site.register(Mesa)
# admin.site.register(Prato)
admin.site.register(Ingrediente)
admin.site.register(Estoque)

admin.site.register(Prato, pratoIAdmin)
admin.site.register(Pedido, pedidoAdmin)
admin.site.register(prato_has_ingrediente)
admin.site.register(pedido_has_prato)