from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True) 
    lido = models.BooleanField(default=False)
    def __str__(self):
        return f'Nome: {self.nome} - Email: {self.email}'
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['data']

class ReservaDeBanho(models.Model):
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    telefone = models.CharField(verbose_name='Telefone', max_length=20)
    dia_reserva = models.DateField(verbose_name='Dia da reserva')
    observacoes = models.TextField(verbose_name='Observações')