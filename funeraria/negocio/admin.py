from django.contrib import admin
from .models import servicos

class servicosAdmin(admin.ModelAdmin):
    list_display = ('nome_do_cliente', 'servico', 'valor_cobrado', 'pagamento', 'cemiterio')

admin.site.register(servicos, servicosAdmin)
