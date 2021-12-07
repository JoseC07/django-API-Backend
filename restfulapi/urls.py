from rest_framework.urlpatterns import format_suffix_patterns
#

from django.conf import settings
from django.conf.urls.static import static

from usersapi import views as views

#login views
from django.contrib.auth import views as auth_views

#import media
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


from usersapi.views import ListUsers, CustomAuthToken


urlpatterns = [
    path('api/users',ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('api/workouts/',views.workoutapi.as_view()),
    path('api/workouts/<int:id>/', views.workoutapi.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)