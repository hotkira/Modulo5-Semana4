from django import forms
from reserva.models import ReservaDeBanho
from datetime import date


class ReservaDeBanhoForm(forms.ModelForm):
  class Meta:
    model = ReservaDeBanho
    fields = ['nome_pet', 'telefone', 'email', 'dia_reserva', 'turno', 'tamanho', 'observacoes']
    widgets = {
        'dia_reserva': forms.DateInput(attrs={'type':'date'}),
    }
  
  def clean_dia_reserva(self):
    dia_reserva_selecionado = self.cleaned_data['dia_reserva']
    hoje = date.today()
      
    if dia_reserva_selecionado < hoje:
        raise forms.ValidationError('Não é possível reservar para uma data do passado')
    
    # Verificar a quantidade de reservas para o dia selecionado
    reservas_no_dia = ReservaDeBanho.objects.filter(dia_reserva=dia_reserva_selecionado).count()
    
    if reservas_no_dia >= 4:
        raise forms.ValidationError('Já existem 4 reservas para este dia, escolha outro dia!')
    
    return dia_reserva_selecionado

       
   