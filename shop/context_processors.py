from .models import Category

def categories(request):
    """Возвращает все категории для использования в шаблонах"""
    categories = Category.objects.filter(parent=None)
    return {'categories': categories}
