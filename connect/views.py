from django.shortcuts import render

# Create your views here.
def home(request):
    render(request, home.html)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account for ' + user + ' successfully created')
        return redirect(reverse('loginpage'))
    context={'form':form}
    
    return render(request,'register.html')