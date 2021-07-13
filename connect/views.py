from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    photos=Image.objects.all()
    user=request.user
    
    context= { 'photos':photos,'user':user}
    return render (request,'home.html',context)

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

def search_results(request):
    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def uploadImage(request):
    if request.method == "POST":

        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
        return redirect('welcome')
    else:
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html",{"form":form})