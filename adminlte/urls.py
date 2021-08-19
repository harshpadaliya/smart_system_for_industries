from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('adminpanel', views.adminpanel, name="adminpanel"),
    path('personcount_data', views.personcount_data, name="personcount_data"),
    path('smoke_data', views.smoke_data, name="smoke_data"),
    path('flame_data', views.flame_data, name="flame_data"),
    path('temperature_data', views.temperature_data, name="temperature_data"),
    path('gas_data', views.gas_data, name="gas_data"),
    path('pirmovement_data', views.pirmovement_data, name="pirmovement_data"),
    path('add_admin', views.add_admin, name="add_admin"),
    path('profile', views.profile, name="profile"),
]
