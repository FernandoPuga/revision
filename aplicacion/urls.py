from django.urls import path, include
from.views import *

# ____________________importamos la vista de logout

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='inicio' ) ,
# _____________________________________________________urls carpinteros_______________________________________

    path('carpinteros/', CarpinteroList.as_view(), name='carpinteros' ),
    path('create_carpintero/',CarpinteroCreate.as_view(), name='create_carpintero' ),
    path('detail_carpintero/<int:pk>/',CarpinteroDetail.as_view(), name='detail_carpintero' ),
    path('update_carpintero/<int:pk>/',CarpinteroUpdate.as_view(), name='update_carpintero' ),
    path('delete_carpintero/<int:pk>/',CarpinteroDelete.as_view(), name='delete_carpintero' ),

# _____________________________________________________urls carpinteros_______________________________________

    path('electricistas/', ElectricistasList.as_view(), name='electricistas' ),
    path('create_electricista/',ElectricistasCreate.as_view(), name='create_electricista' ),
    path('detail_electricista/<int:pk>/',ElectricistasDetail.as_view(), name='detail_electricista' ),
    path('update_electricista/<int:pk>/',ElectricistasUpdate.as_view(), name='update_electricista' ),
    path('delete_electricista/<int:pk>/',ElectricistasDelete.as_view(), name='delete_electricista' ),


# _________________________login

    path('login/',login_request, name='login' ),
    path('logout/',LogoutView.as_view(template_name="aplicacion/logout.html"), name='logout' ),

# _________________________login

    path('register/', register, name="register"),

]