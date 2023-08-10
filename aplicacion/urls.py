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

    #_________________________busqueda carpinteros por localidad

    path('carpinteros_list/', buscarCarpinterosZona, name='carpinteros_list'),
    path('carpinteros/buscar2/', buscar2, name='carpinteros/buscar2'),


# _____________________________________________________urls electricistas_______________________________________

    path('electricistas/', ElectricistasList.as_view(), name='electricistas' ),
    path('create_electricista/',ElectricistasCreate.as_view(), name='create_electricista' ),
    path('detail_electricista/<int:pk>/',ElectricistasDetail.as_view(), name='detail_electricista' ),
    path('update_electricista/<int:pk>/',ElectricistasUpdate.as_view(), name='update_electricista' ),
    path('delete_electricista/<int:pk>/',ElectricistasDelete.as_view(), name='delete_electricista' ),

#_________________________busqueda electricistas por localidad

    path('electricistas_list/', buscarElectricistasZona, name='electricistas_list'),
    path('electricistas/buscar3/', buscar3, name='electricistas/buscar3'),


# _____________________________________________________urls plomeros_______________________________________

    path('plomeros/', PlomerosList.as_view(), name='plomeros' ),
    path('create_plomero/',PlomerosCreate.as_view(), name='create_plomero' ),
    path('detail_plomero/<int:pk>/',PlomerosDetail.as_view(), name='detail_plomero' ),
    path('update_plomero/<int:pk>/',PlomerosUpdate.as_view(), name='update_plomero' ),
    path('delete_plomero/<int:pk>/',PlomerosDelete.as_view(), name='delete_plomero' ),

#_________________________busqueda plomeros por localidad

    path('plomeros_list/', buscarPlomerosZona, name='plomeros_list'),
    path('plomeros/buscar4/', buscar4, name='plomeros/buscar4'),


# _____________________________________________________urls gasistas_______________________________________

    path('gasistas/', GasistasList.as_view(), name='gasistas' ),
    path('create_gasista/',GasistasCreate.as_view(), name='create_gasista' ),
    path('detail_gasista/<int:pk>/',GasistasDetail.as_view(), name='detail_gasista' ),
    path('update_gasista/<int:pk>/',GasistasUpdate.as_view(), name='update_gasista' ),
    path('delete_gasista/<int:pk>/',GasistasDelete.as_view(), name='delete_gasista' ),

#_________________________busqueda gasistas por localidad

    path('gasistas_list/', buscarGasistasZona, name='gasistas_list'),
    path('gasistas/buscar5/', buscar5, name='gasistas/buscar5'),


# _____________________________________________________urls pintores_______________________________________

    path('pintores/', PintoresList.as_view(), name='pintores' ),
    path('create_pintor/',PintoresCreate.as_view(), name='create_pintor' ),
    path('detail_pintor/<int:pk>/',PintoresDetail.as_view(), name='detail_pintor' ),
    path('update_pintor/<int:pk>/',PintoresUpdate.as_view(), name='update_pintor' ),
    path('delete_pintor/<int:pk>/',PintoresDelete.as_view(), name='delete_pintor' ),

#_________________________busqueda pintores por localidad

    path('pintores_list/', buscarPintoresZona, name='pintores_list'),
    path('pintores/buscar6/', buscar6, name='pintores/buscar6'),


    
# _________________________login

    path('login/',login_request, name='login' ),
    path('logout/',LogoutView.as_view(template_name="aplicacion/logout.html"), name='logout' ),

# _________________________Registro

    path('register/', register, name="register"),


# _________________________acerca de mi

    path('acercaDeMi/', acercaDeMi, name="acercaDeMi"),


]