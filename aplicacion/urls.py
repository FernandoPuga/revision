from django.urls import path, include
from.views import *

urlpatterns = [
    path('', index, name='inicio' ) ,
    path('carpinteros/', CarpinteroList.as_view(), name='carpinteros' ),
    path('create_carpintero/',CarpinteroCreate.as_view(), name='create_carpintero' ),
    path('detail_carpintero/<int:pk>/',CarpinteroDetail.as_view(), name='detail_carpintero' ),
]