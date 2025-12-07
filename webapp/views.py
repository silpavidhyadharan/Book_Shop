from django.shortcuts import render,redirect
from django.template.defaultfilters import first

from adminApp.models import CategoryDb,BookDb
from webapp.models import SignUpDb,ContactDb,CartDb,CheckoutDb
from django.contrib import messages

# Create your views here.
def home_page(request):
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
    return render(request,"Home.html",{'categories':categories,'cart_total':cart_total})

def about_page(request):
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
    return render(request,"About.html",{'categories':categories,'cart_total':cart_total})

def contact_page(request):
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
    return render(request,"Contact.html",{'categories':categories,'cart_total':cart_total})

def popular_books_page(request):
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
    books = BookDb.objects.all()
    return render(request,"Popular_Books.html",{'categories':categories,'books':books,'cart_total':cart_total})

def checkout_page(request):
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
        books = CartDb.objects.filter(username=request.session['Name'])
        # Calculating total Amount
        sub_total = 0
        delivery_charge = 0
        total_amount = 0
        for i in books:
            sub_total += i.total_price
            if sub_total > 500:
                delivery_charge = 50
            elif sub_total > 1000:
                delivery_charge = 0
            else:
                delivery_charge = 100
            total_amount = sub_total + delivery_charge
    return render(request,"Checkout.html",{'categories':categories,'cart_total':cart_total,
                                           'sub_total':sub_total,
                                           'delivery_charge':delivery_charge,
                                           'total_amount':total_amount})

def filtered_Books(request,book_category):
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
    books = BookDb.objects.filter(category=book_category)
    return render(request,"Filter_Books.html",{'books':books,'book_category':book_category,'categories':categories
                                               ,'cart_total':cart_total})

def single_book(request,book_id):
    book = BookDb.objects.get(id=book_id)
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(username=uname).count()
    return render(request,"Single_Book.html",{'book':book,'cart_total':cart_total})

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
            messages.error(request,"User Already Exist..!")
            return redirect(signup_page)
        elif SignUpDb.objects.filter(email=user_email).exists():
            messages.warning(request,"User Already Exist..!")
            return redirect(signup_page)

        else:
            obj.save()
            messages.success(request,"Login Successful..!")
            return redirect(login_page)

def user_login(request):
    if request.method=="POST":
        un = request.POST.get('name')
        pswd = request.POST.get('password')
        if SignUpDb.objects.filter(Name=un,password=pswd).exists():
            request.session['Name']=un
            request.session['password']=pswd
            messages.success(request,"Login Successful...!")
            return redirect(home_page)
        else:
            messages.warning(request,"Login Failed")
            return redirect(login_page)
    else:
        messages.warning(request, "Login Failed")
        return redirect(login_page)

def save_contact(request):
    if request.method == "POST":
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_subject = request.POST.get('subject')
        user_message = request.POST.get('message')
        obj = ContactDb(name=user_name,email=user_email,subject=user_subject,message=user_message)
        obj.save()
        messages.success(request,"Sent Message Successfully...!..!")
        return redirect(contact_page)

def display_messages(request):
    data = ContactDb.objects.all()
    return render(request,"View_messages.html",{'data':data})

def user_logout(request):
    request.session.pop('Name', None)
    request.session.pop('password', None)
    messages.success(request, "Logout Successful...!")
    return redirect(home_page)


def cart_page(request):
    books = CartDb.objects.filter(username=request.session['Name'])
    # Calculating total Amount
    sub_total = 0
    delivery_charge = 0
    total_amount = 0
    for i in books:
        sub_total += i.total_price
        if sub_total>500:
            delivery_charge = 50
        elif sub_total>1000:
            delivery_charge = 0
        else:
            delivery_charge = 100
        total_amount = sub_total + delivery_charge

    return render(request,"Cart_page.html",{'books':books,
                                            'sub_total':sub_total,
                                            'delivery_charge':delivery_charge,
                                            'total_amount':total_amount})

def save_to_cart(request):
    book_name = request.POST.get('Book_name')
    quantity = int(request.POST.get('quantity'))
    price = int(request.POST.get('price'))
    total = int(request.POST.get('Total'))
    username = request.POST.get('username')
    book = BookDb.objects.filter(title=book_name).first()
    img = book.cover_image if book else None
    obj = CartDb(bookname=book_name,quantity=quantity,price=price,total_price=total,book_image=img,username=username)
    obj.save()
    messages.success(request,"Book Added To Cart..!")
    return redirect(home_page)

def delete_cart(request,c_id):
    data = CartDb.objects.filter(id=c_id)
    data.delete()
    messages.success(request,"Product Removed From Cart Successfully..!")
    return redirect(cart_page)

def save_checkout_data(request):
    f_name =  request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    user_email =  request.POST.get('c_email')
    user_phone = request.POST.get('c_phone')
    user_address = request.POST.get('c_address')
    user_city = request.POST.get('c_address')
    user_pincode =  request.POST.get('c_pincode')
    total_amount = request.POST.get('c_total')
    obj = CheckoutDb(first_name=f_name,last_name=l_name,email=user_email,phone=user_phone,address=user_address,city=user_city,
                    pincode = user_pincode,total=total_amount)
    obj.save()
    return redirect(payment_page)

def payment_page(request):
    return render(request,"Payment.html")