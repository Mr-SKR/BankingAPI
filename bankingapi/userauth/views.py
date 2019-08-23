from django.shortcuts import render
from .forms import SignUpForm
from .models import SignUp
from django.http import HttpResponse, HttpResponseRedirect


def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            username = form.cleaned_data['user_id']
            password = form.cleaned_data['password']

            if SignUp.objects.filter(username=username).first():
                return HttpResponse("username already exists.")
            sign_up_instance = SignUp(username=username)
            sign_up_instance.set_password(raw_password=password)
            sign_up_instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/api/token/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
