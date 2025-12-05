from django.urls import path
from webapp import views
urlpatterns = [
    path('home_page/',views.home_page,name="home_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('popular_books_page/',views.popular_books_page,name="popular_books_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('filtered_Books/<book_category>/',views.filtered_Books,name="filtered_Books"),
    path('single_book/<int:book_id>/',views.single_book,name="single_book"),
    path('login_page/',views.login_page,name="login_page"),
    path('signup_page/',views.signup_page,name="signup_page"),
    path('save_signup_data/',views.save_signup_data,name="save_signup_data"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('save_to_cart/',views.save_to_cart,name="save_to_cart"),
]