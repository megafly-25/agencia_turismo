from django.urls import path
from .views import index,nosotros,paquetes_turisticos,paquete,registro_user
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('',index,name="index"),
    path('nosotros',nosotros, name="nosotros"),
    path('paquetes-turisticos',paquetes_turisticos,name="paquetes_turisticos"),
    path('paquete/<slug>',paquete,name="paquete"),
    path('registro/',registro_user,name="registro")

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)