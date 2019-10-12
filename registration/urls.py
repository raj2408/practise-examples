from django.contrib import admin
from django.urls import path
from reg.views import *
from bmicalc.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('student/', student_list),
    path('teacher/', teacher_list),
    path('institute/', institute_list),
    path('studentform/', createstudent),
    path('student_edit/<int:id>/', editstudent),
    path('studentdelete/<int:id>/', deletestudent),
    path('bmicalc/', bmi),
    path('teacherform/', createteacher),
    path('teacherformM/', createteacher_M),
    path('teacher_edit/<int:id>/', editteacher),
    path('instituteformM/', createinstituteM),
    path('instituteformC/', createinstituteC),
    path('institutedelete/<int:id>/', deleteinstitute),
    path('t_downloadcsv/', t_downloadcsv),
    path('s_downloadxls/', s_downloadxls),
    path('i_downloadxlsx/', i_downloadxlsx),
    path('signup/', signup),
    path('auth/', auth_view),
    path('login/', login),
    path('loggedout/', logout),
    path('loggedin/', loggedin),
    path('invalid/', invalid_login),
    #
    # path('accounts/login/', django_test.views.login),
    # path('accounts/auth/', django_test.views.auth_view),
    # path('accounts/logout/', django_test.views.logout),
    # path('accounts/loggedin/', django_test.views.loggedin),
    # path('accounts/invalid/', django_test.views.invalid_login),
]