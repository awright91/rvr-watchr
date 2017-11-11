from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView
from web_pages import forms
from locations.models import State
# Create your views here.


def Home(request):
    states = State.objects.all()
    va = State.objects.get(id=1)
    rvrs = va.river.all()
    print(rvrs)
    for state in states:
        rvr_count = state.river.all().count()
        state.count = rvr_count
    return render(request, 'web_pages/home.html', {'states': states})

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('user_admin')

            else:
                return HttpResponse('Accounts Not Active')
        else:
            print('someone tried to login and failed! Username: {}, PW: {}'.format(username, password))
            return HttpResponse("invalid Login Details")
    else:
        if request.user.is_authenticated:
            return redirect('user_admin')
        else:
            return render(request, 'web_pages/login.html')

class UserSignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('user_admin')
    template_name= 'web_pages/signup.html'


    def form_valid(self, form):
        valid = super(UserSignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class TestPage(TemplateView):
    template_name ='test.html'

class ThanksPage(TemplateView):
    template_name = "web_pages/thanks.html"
