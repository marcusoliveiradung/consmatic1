from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    #url(r'^$', 'teste.views.home', name='home'),
    #url(r'^teste/', include('teste.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
# ... your normal urlpatterns here
# Uncomment the next two lines to enable the admin:

######
from django.conf import settings
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


#url(r'^comments/', include('django.contrib.comments.urls')),