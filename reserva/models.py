from django.db import models

class ReservaDeBanho(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande')
    )
    TURNO_OPCOES =(
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    )
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=20)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    dia_reserva = models.DateField(verbose_name='Dia da reserva')
    turno = models.CharField(verbose_name='Turno', choices=TURNO_OPCOES, max_length=5) 
    observacoes = models.TextField(verbose_name='Observações')
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    
   # def __str__(self):
   #     return f'{self.nome}: {self.data} - {self.turno}'
    
    class Meta:
        verbose_name= 'Formulário de Reserva de Banho'
        verbose_name_plural = 'Formulários de Reservas de Banhos'
