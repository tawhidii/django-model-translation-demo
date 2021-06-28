from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Posts
from django.http import HttpResponseRedirect
from django.conf import settings


# Create your views here.
def post_index(request):
    context = {
        'a': Posts.objects.all()
    }
    print(context)

    template = 'post.html'
    return render(request, template, context)


def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]
            redirect_path = f'/{language}'

        elif language == settings.LANGUAGE_CODE:
            redirect_path = '/'
        else:
            return response
        from django.utils import translation
        translation.activate(language)
        response = HttpResponseRedirect(redirect_path)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
