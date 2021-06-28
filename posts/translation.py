from modeltranslation.translator import (
    translator,
    register,
    TranslationOptions

)

from .models import Posts


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(Posts, PostTranslationOptions)
