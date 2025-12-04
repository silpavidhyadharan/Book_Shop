import datetime
from django.shortcuts import render,redirect
from adminApp.models import CategoryDb,BookDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from webapp.models import ContactDb

# Create your views here.
def index_page(request):
    books = BookDb.objects.count()
    categories = CategoryDb.objects.count()
    return render(request,"index.html",{'books':books,'categories':categories})

# -----------------------------------------CATEGORY-----------------------------------------------------

def add_category(request):
    return render(request,"Add_category.html")

def save_category_data(request):
    if request.method == "POST":
        category_name = request.POST.get('c_name')
        category_description = request.POST.get('c_description')
        image = request.FILES['c_image']
        obj = CategoryDb(name=category_name,description=category_description,cover_image=image)
        obj.save()
        messages.success(request,"Category saved successfully..!")
        return redirect(add_category)
def display_category(request):
    data = CategoryDb.objects.all()
    return render(request,"Display_category.html",{'data':data})
def edit_category(request,c_id):
    category = CategoryDb.objects.get(id=c_id)
    return render(request,"Edit_category.html",{'category':category})
def delete_category(request,cat_id):
    data = CategoryDb.objects.filter(id=cat_id)
    data.delete()
    messages.error(request,"Category deleted successfully..!")
    return redirect(display_category)

def update_category(request,category_id):
    if request.method=="POST":
        category_name = request.POST.get('c_name')
        category_description = request.POST.get('c_description')
        try:
            cover_image = request.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(cover_image.name,cover_image)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=category_id).cover_image
        CategoryDb.objects.filter(id=category_id).update(name=category_name,description=category_description,cover_image=file)
        messages.success(request,"Category Updated successfully..!")
        return redirect(display_category)


# ---------------------------------------------------BOOK---------------------------------------------------------------

def add_book(request):
    categories=CategoryDb.objects.all()
    return render(request,"Add_book.html",{'categories':categories})

def save_book_data(request):
    if request.method == "POST":
        book_title = request.POST.get('b_title')
        book_author = request.POST.get('b_author')
        book_category = request.POST.get('b_category')
        book_price = request.POST.get('b_price')
        book_publisher = request.POST.get('b_publisher')
        book_description = request.POST.get('b_description')
        book_image = request.FILES['b_image']
        obj = BookDb(title=book_title,author=book_author,category=book_category,price=book_price,publisher=book_publisher,
                     description=book_description,cover_image=book_image)
        obj.save()
        messages.success(request,"Book Added successfully..!")
        return redirect(add_book)

def display_Book(request):
    data = BookDb.objects.all()
    return render(request,"Display_Book.html",{'data':data})

def edit_book(request,book_id):
    book = BookDb.objects.get(id=book_id)
    categories = CategoryDb.objects.all()
    return render(request,"Edit_books.html",{'book':book,'categories':categories})

def delete_book(request,b_id):
    data = BookDb.objects.filter(id=b_id)
    data.delete()
    messages.error(request,"Book Details Deleted..!")
    return redirect(display_Book)

def update_book_data(request,Book_id):
    book_title = request.POST.get('b_title')
    book_author = request.POST.get('b_author')
    book_category = request.POST.get('b_category')
    book_price = request.POST.get('b_price')
    book_publisher = request.POST.get('b_publisher')
    book_description = request.POST.get('b_description')
    try:
        cover_image = request.FILES['b_image']
        fs = FileSystemStorage()
        file = fs.save(cover_image.name,cover_image)
    except MultiValueDictKeyError:
        file=BookDb.objects.get(id=Book_id).cover_image
    BookDb.objects.filter(id=Book_id).update(title=book_title,author=book_author,category=book_category,price=book_price,publisher=book_publisher,
                     description=book_description,cover_image=file)
    messages.success(request,"Book Details Updated Succesfully..!")
    return redirect(display_Book)


def admin_login_page(request):
    return render(request,"Admin_login.html")

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data = authenticate(username=un,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username'] = un
                request.session['password'] = pswd
                return redirect(index_page)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def view_messages(request):
    data = ContactDb.objects.all()
    return render(request,"view_messages.html",{'data':data})

def delete_message(request,message_id):
    data = ContactDb.objects.filter(id=message_id)
    data.delete()
    messages.error(request,"Message Deleted Successfully..!")
    return redirect(view_messages)
