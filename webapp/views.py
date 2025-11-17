from django.shortcuts import render,redirect
from adminApp.models import CategoryDb,BookDb
from webapp.models import SignUpDb
# Create your views here.
def home_page(request):
    categories = CategoryDb.objects.all()
    return render(request,"Home.html",{'categories':categories})

def about_page(request):
    categories = CategoryDb.objects.all()
    return render(request,"About.html",{'categories':categories})

def contact_page(request):
    categories = CategoryDb.objects.all()
    return render(request,"Contact.html",{'categories':categories})

def popular_books_page(request):
    categories = CategoryDb.objects.all()
    books = BookDb.objects.all()
    return render(request,"Popular_Books.html",{'categories':categories,'books':books})

def checkout_page(request):
    categories = CategoryDb.objects.all()
    return render(request,"Checkout.html",{'categories':categories})

def filtered_Books(request,book_category):
    categories = CategoryDb.objects.all()
    books = BookDb.objects.filter(category=book_category)
    return render(request,"Filter_Books.html",{'books':books,'book_category':book_category,'categories':categories})

def single_book(request,book_id):
    book = BookDb.objects.get(id=book_id)
    return render(request,"Single_Book.html",{'book':book})

def login_page(request):
    return render(request,"Login.html")

def signup_page(request):
    return render(request,"SignUp.html")

def save_signup_data(request):
    if request.method=="POST":
        username = request.POST.get('name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        obj  = SignUpDb(Name=username,email=user_email,password=user_password,confirm_password=confirm_password)
        if SignUpDb.objects.filter(Name=username).exists():
            # Alert Username already exists
            return redirect(signup_page)
        elif SignUpDb.objects.filter(email=user_email).exists():
            return redirect(signup_page)

        else:
            obj.save()
            return redirect(login_page)

def user_login(request):
    if request.method=="POST":
        un = request.POST.get('name')
        pswd = request.POST.get('password')
        if SignUpDb.objects.filter(Name=un,password=pswd).exists():
            request.session['Name']=un
            request.session['password']=pswd
            return redirect(home_page)
        else:
            return redirect(login_page)
    else:
        return redirect(login_page)

def user_logout(request):
    del request.session['Name']
    del request.session['password']
    return redirect(login_page)

def cart_page(request):
    return render(request,"Cart_page.html")