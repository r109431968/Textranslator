from django.contrib import admin
from django.urls import path

import TextranslatorApp.views
from TextranslatorApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', translator, name='translator'),
    path('translated/', translated, name='translated')
]

