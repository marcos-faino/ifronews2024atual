from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView


from usuario.forms import UsuarioCreationForm


class UsuarioCreateView(CreateView):
    template_name = 'usuario/cadusuario.html'
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('loginuser')

    def form_valid(self, form):
        form.cleaned_data
        usuario = form.save(commit=False)
        usuario.is_staff = True
        form.save()
        messages.success(self.request, f"Usuário Cadastrado!!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Usuário não pôde ser cadastrado!")
        return super().form_invalid(form)
