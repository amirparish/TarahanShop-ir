from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category
# , Slider, Brand, SiteBase

def index(request):

    categories = Category.objects.all()

    # sliders = Slider.objects.filter(is_active=True).order_by('order')

    # brands = Brand.objects.filter(is_active=True).order_by('order')

    # site_base = SiteBase.objects.first()

    context = {
        'categories': categories,
        # 'sliders': sliders,
        # 'brands': brands,
        # 'site_base': site_base,
    }
    return render(request, 'index.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category_detail.html', {'category': category})