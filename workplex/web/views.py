# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='web:login')
def index(request):
    context={}
    return render(request,'web/index.html',context)

def blog_detail (request):
    context={}
    return render(request,'web/blog-detail.html',context)

def blog (request):
    context={
        "Blog":Blog.objects.all(),
    }
    return render(request,'web/blog.html',context)

def browse_category (request):
    context={
    }
    return render(request,'web/browse-category.html',context)


def browse_employers_list(request):
    context={}
    return render(request,'web/browse-employers-list.html',context)

def browse_employers (request):
    context={}
    return render(request,'web/browse-employers.html',context)

def browse_jobs(request):
    context={}
    return render(request,'web/browse-jobs.html',context)

def browse_resumes_list (request):
    context={}
    return render(request,'web/browse-resumes-list.html',context)

def browse_resumes (request):
    context={}
    return render(request,'web/browse-resumes.html',context)

def candidate_dashboard(request):
    context={}
    return render(request,'web/candidate-dashboard.html',context)

def candidate_detail(request):
    context={}
    return render(request,'web/candidate-detail.html',context)


def contact(request):
    context = {}
    return render(request, 'web/contact.html', context)


def job_search_v1 (request):
    context={}
    return render(request,'web/job-search-v1.html',context)

def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:signup')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:signup')
            else:
                customer = User.objects.create_user(username=username,email=email,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/register.html")
            
    # return render(request,'web/register.html',context)

def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        # user = User.objects.filter(username=username,password=password).first()
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:login')
    return render(request,"web/login.html")
        
    # return render(request,'web/login.html',context)
    

def employer_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        # user = User.objects.filter(username=username,password=password).first()
        if user is not None:
            login(request,user)
            return redirect('web:post_job')
        else:  
            print('hi')
            return redirect('web:employer_login')
    return render(request,"web/employer_login.html")
    # return render(request,'web/employer_login.html',context)

def employer_register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:employer_login')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:employer_login')
            else:
                customer = User.objects.create_user(username=username,email=email,password=pass1)
                return redirect('web:employer_login')
           

    return render(request,"web/employer_register.html")
    # return render(request,'web/employer_register.html',context)



def post_job(request):
    context={}
    return render(request,'web/dashboard-post-job.html',context)

def logout_1(request):
    logout(request)
    return redirect('web:index')

