from django.urls import path,include



# from django.contrib import admin



from . import views

urlpatterns=[
  # path('/',view.,name=),
    path('addnote/',views.add_note,name='add_note'),
    path('getnote/', views.get_note, name='get_note'),
    path('delete/',views.delete_note,name='delete_note'),
    path('edit/', views.edit_note, name='edit_note'),
]