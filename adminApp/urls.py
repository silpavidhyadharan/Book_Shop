from django.urls import path
from adminApp import views
urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),

    path('add_category/',views.add_category,name="add_category"),
    path('save_category_data/',views.save_category_data,name="save_category_data"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:c_id>/',views.edit_category,name="edit_category"),
    path('delete_category/<int:cat_id>',views.delete_category,name="delete_category"),
    path('update_category/<int:category_id>/',views.update_category,name="update_category"),

    path('add_book/', views.add_book, name="add_book"),
    path('save_book_data/',views.save_book_data,name="save_book_data"),
    path('display_Book/',views.display_Book,name="display_Book"),
    path('delete_book/<int:b_id>/',views.delete_book,name="delete_book"),
    path('edit_book/<int:book_id>/',views.edit_book,name="edit_book"),
    path('update_book_data/<int:Book_id>/',views.update_book_data,name="update_book_data"),

    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout")
]


