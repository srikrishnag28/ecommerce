from .models import Category


def category_memu(request):
    links = Category.objects.all()
    return dict(links=links)
