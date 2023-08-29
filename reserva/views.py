from django.shortcuts import render
from reserva.forms import ReservaDeBanhoForm




def criar_reserva_banho(request):
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