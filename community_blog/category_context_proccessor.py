from .models import Category


def get_context_data(self, *args, **kwargs):
    categories_menu = Category.objects.all()

    return {'categories_menu': categories_menu}
