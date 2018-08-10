"""project URL Configuration"""


from django.contrib import admin

from atlas import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import include, path

'''Here we have imported (include)-: this allows us to add the gram url pattern
as done below this is to avoid filling up all our urls in this page'''

''' End Of Import'''
#-------------------------------#


urlpatterns = [
    #url for registration
    path('accounts/', include('registration.backends.simple.urls')),

    path('', include('atlas.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()