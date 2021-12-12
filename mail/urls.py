from django.urls import path
from  mail import views
app_name = 'mail'

urlpatterns = [
  path('',views.EmailList.as_view(), name = 'home'),
  path('add/',views.EmailCreate.as_view(), name = 'create'),
  path('edit/<pk>',views.EmailUpdate.as_view(), name = 'update'),
  path('remove/<pk>',views.EmailDelete.as_view(), name = 'delete'),
  path('send/',views.send_email, name = 'send'),
  path('emails/',views.base, name = 'emails'),
  path('about/',views.about, name = 'about'),
  

]