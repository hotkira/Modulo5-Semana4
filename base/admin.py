from django.contrib import admin
from django.contrib import messages
from base.models import Contato

@admin.action(description='Marcar formulários de contato selecionados como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Os formulários de contato foram marcados como lido', messages.SUCCESS)

admin.action(description='Marcar formulários de contato selecionados como Não lido')
def marcar_como_nao_lido(modeladmin, request, queryset):
    queryset.update(lido=False)
    modeladmin.message_user(request, 'Os formulários de contato foram marcados como não lido', messages.SUCCESS)



@admin.register(Contato)  # Especifique o modelo que deseja registrar aqui
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'mensagem','data', 'lido']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]
    
