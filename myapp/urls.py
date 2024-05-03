from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('citizen/', views.citizen, name='citizen'),
    path('otp/', views.otp, name='otp'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.password, name='password'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('view-profile/', views.view_profile, name='view-profile'),
    path('add-FIR/', views.add_FIR, name='add-FIR'),
    path('view-FIR/', views.view_FIR, name='view-FIR'),
    path('view-one-FIR/<int:pk>', views.view_one_FIR, name='view-one-FIR'),
    path('search-station/', views.search_station, name='search-station'),
    path('add-com/', views.add_com, name='add-com'),
    path('feedback/', views.feedback, name='feedback'),
    path('view-com/', views.view_com, name='view-com'),
    path('view-one-com/<int:pk>', views.view_one_com, name='view-one-com'),
    path('emergency/', views.emergency, name='emergency'),
    path('rules/', views.rules, name='rules'),
    path('missing/', views.missing, name='missing'),
    path('missing-one/<int:pk>', views.missing_one, name='missing-one'),
    path('add_missing/', views.add_missing, name='add-missing'),
    path('success/', views.success_view, name='success_view'),
    path('most-wanted/', views.most_wanted, name='most_wanted'),
    path('most-wanted/<int:pk>/', views.one_most_wanted, name='one_most_wanted'),
    path('generate_pdf/<int:complaint_id>/', views.generate_pdf, name='generate_pdf'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),


]
