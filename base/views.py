from django.shortcuts import render
from base.forms import ContatoForm
from base.forms import ReservaDeBanhoForm


# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')


def contato(request):
  print('método: ',request.method)
  sucesso = False

  if request.method == 'GET':
    form = ContatoForm()
  else:
    form = ContatoForm(request.POST)
    if form.is_valid():
      sucesso = True
      form.save()
           # nome = form.cleaned_data['nome']
      #email = form.cleaned_data['email']
      #mensagem = form.cleaned_data['mensagem']
      #Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
#salvando no banco
  context = {  
    "form": form,
    "sucesso": sucesso
  }
  return render(request, 'contato.html', context)

def reservaDeBanho(request):
  sucesso = False

  if request.method == 'GET':
    form = ReservaDeBanhoForm()
  else:
    form = ReservaDeBanhoForm(request.POST)
    if form.is_valid():
      sucesso = True
      form.save()

  context = {
    "form": form,
    "sucesso": sucesso
  }

  return render(request, 'reserva_de_banho.html', context)