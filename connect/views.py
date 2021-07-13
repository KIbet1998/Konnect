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

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=  request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('welcome'))
        else:
            messages.info(request,'Username or password is incorrect')
       
    context={}
    return render(request,'login.html',context)

def profilepage(request,username):
    user=User.objects.filter(username=username)
    if user:
    # current_user = request.user
        profile = Profile.objects.get(user=user)
        bio=profile.bio
        
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return redirect(reverse("profile.html",{"obj":obj}))
        else:
            form=ImageForm()
        img=Image.objects.all()
        return render(request,'profile.html', {'img':img,'form':form})
    

    context={'u_form':u_form,'p_form':p_form,'current_user':current_user,'profile':profile}

    return render(request,'profile.html',context=context)