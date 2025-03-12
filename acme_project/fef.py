'http://www.acme.not/nice/'

 # urls.py
 ...
 urlpatterns = [
     ...
     path('nice/', views.nice_page), 
     ...
 ]
 
  # views.py
 ...
 def nice_page(request):
     ...
     return HttpResponse(
         'Это nice page, прекраснейшая страница в глобальной сети!'
     )
 