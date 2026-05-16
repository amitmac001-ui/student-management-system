from django.contrib import admin
from django.urls import path
from accounts.views import login_page, dashboard, firstmbbs

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_page),

    path('dashboard/', dashboard),

    path('firstmbbs/', firstmbbs),
]
