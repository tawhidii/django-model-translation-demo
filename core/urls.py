
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from django.utils.translation import gettext_lazy as _
from posts.views import change_language


urlpatterns = [
    path('change-language/',change_language,name='change_language'),
    path('i18n/',include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    prefix_default_language=False
)
