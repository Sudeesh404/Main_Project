from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-index/', views.admin_index,name='admin-index'),
    path('admin-login/',views.admin_login,name='admin-login'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),
    path('admin-view-FIR/',views.admin_view_FIR,name='admin-view-FIR'),
    path('admin-view-one-FIR/<int:pk>',views.admin_view_one_FIR,name='admin-view-one-FIR'),
    path('admin-station/',views.admin_station,name='admin-station'),
    path('admin-one-station/<int:pk>',views.admin_one_station,name='admin-one-station'),
    path('admin-user/',views.admin_user,name='admin-user'),
    path('admin-one-user/<int:pk>',views.admin_one_user,name='admin-one-user'),
    path('admin-policestation/',views.admin_policestation,name='admin-policestation'),
    path('admin-one-ins/<int:pk>',views.admin_one_ins,name='admin-one-ins'),
    path('admin-subins/',views.admin_subins,name='admin-subins'),
    path('admin-one-sub/<int:pk>',views.admin_one_sub,name='admin-one-sub'),
    path('admin-feedback/',views.admin_feedback,name='admin-feedback'),
    path('admin-efeedback/<int:pk>',views.admin_efeed,name='admin-efeedback'),
    path('admin-emergency/',views.admin_emegency,name='admin-emergency'),
    path('admin-rules/',views.admin_rules,name='admin-rules'),
    path('admin-edit-profile/',views.admin_edit_profile,name='admin-edit-profile'),
    path('admin-view-profile/',views.admin_view_profile,name='admin-view-profile'),
    path('admin-change-password/',views.admin_password,name='admin-change-password'),
    path('admin-category/', views.category,name='category'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-mostwanted/', views.most_wanted_view, name='admin_mostwanted'),
    path('admin_one_mostwanted/<int:pk>/', views.most_wanted_one, name='admin_one_mostwanted'),
    path('complaints/', views.view_all_complaints, name='view_all_complaints'),
    path('add_post/', views.add_post, name='add_post'),
    
]