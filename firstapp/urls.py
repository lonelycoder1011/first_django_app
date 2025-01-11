from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Reference index view
    path('date', views.get_date, name='date'),  # Reference get_date view
]






# for Direct this link http://127.0.0.1:8000/date
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('firstapp.urls')),  # Includes all firstapp routes
#     path('date', get_date, name='date'),  # Directly maps /date to the get_date view
# ]