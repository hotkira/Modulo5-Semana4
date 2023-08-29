from django.contrib import admin
from reserva.models import ReservaDeBanho

# Register your models here.
@admin.register(ReservaDeBanho)
class ReservaDeBanhoAdmin(admin.ModelAdmin):
    list_display=['nome_pet','email', 'dia_reserva','observacoes', 'turno', 'tamanho']
    search_fields=['nome_pet', 'email']
    list_filter=['dia_reserva','turno','tamanho']
    