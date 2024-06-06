from django.urls import path
from .views import *
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('user-home/', UserHome.as_view(), name='user-home'), 
    path('machines/', MachineListCreate.as_view(), name='machine-list-create'),
    path('logs/', ProductionLogListCreate.as_view(), name='productionlog-list-create'),
    path('oee/', OEEView.as_view(), name='get-oee'),
    path('oee/filter/', FilterOEEView.as_view(), name='filter-oee'),
]