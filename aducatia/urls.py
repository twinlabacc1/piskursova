from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('course/', include('courses.urls')),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('', HomePageView.as_view(), name='home'),
    path('students/', include('students.urls')),
    #path('signup/', auth_views.SignUpView.as_view(), name='signup'),
    path('accounts/', include("allauth.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
