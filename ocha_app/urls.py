from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name ='index'),
    path('add',views.Add_note, name='add'),
    path('delete_note/<str:pk>', views.Delete_note, name='delete_note'),
    
    
    

]