from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from artes.forms import PublicacaoForm
from artes.models import Publicacao




class HomeView(generic.ListView):
    model = Publicacao
    template_name = "index.html"


class PublicacaoCreateView(generic.CreateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = reverse_lazy('index')
    template_name = 'criar_plub.html'
    def form_valid(self, form):
        # Antes de salvar, defina o autor como o usuário autenticado
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PublicacaoDeleteView(generic.DeleteView):
    model = Publicacao
    success_url = reverse_lazy('index')
    template_name = 'publicacao_confirm_delete.html'



class PublicacaoUpdate(generic.UpdateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = reverse_lazy('index')
    template_name = 'criar_plub.html'
#   model = Reserva
#   form_class = ReservaForm
#   success_url = reverse_lazy("stands:reservas-list")
#   template_name = "reservas_form.html"

#class ReservaDeleteView(generic.DeleteView):
#   model = Reserva
#   success_url = reverse_lazy("stands:reservas-list")




# class ReservaCreateView(generic.CreateView):
#   model = Reserva
#   form_class = ReservaForm
#   success_url = reverse_lazy("stands:reservas-list")
#   template_name = "reservas_form.html"