
from django.urls import path

from . import views

urlpatterns = [

    path('',views.index,name='index'),
    # path('calc/',views.calc,name='calc')
    # path('about/',views.about,name='about'),
# path('contact/',views.contact,name='contact'),
# path('details/',views.details,name='details'),
# path('thanks/',views.thanks,name='thanks')

]
