from django import forms
from base.models import Contato
from base.models import ReservaDeBanho

#class ContatoForm(forms.Form):
 # nome = forms.CharField()
 # email = forms.EmailField()
 # mensagem = forms.CharField(widget=forms.Textarea)

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']  


class ReservaDeBanhoForm(forms.ModelForm):
  class Meta:
    model = ReservaDeBanho
    fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']
    #nomeDoPet = forms.CharField(label="Nome do PET")
    #telefone = forms.CharField(label="Telefone")
   # diaDaReserva = forms.DateField(label="Dia da reserva", 
                                 #widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    #observacoes = forms.CharField(label="Obsevações",
                                #widget=forms.Textarea)