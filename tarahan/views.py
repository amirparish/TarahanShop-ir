from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Slider, Brand, Product, Blog, About
# SiteBase

def index(request):

    categories = Category.objects.all()

    sliders = Slider.objects.all().order_by('order')

    brands = Brand.objects.all()

    amazing_products = Product.objects.filter(is_amazing=True).order_by('-id')[:5]

    blogs = Blog.objects.order_by('-id')[:4]

    context = {
        'categories': categories,
        'sliders': sliders,
        'amazing_products': amazing_products,
        'brands': brands,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_detail.html', context)

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    featured_products = Product.objects.filter(is_featured=True).order_by('-id')[:8]

    if query:
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    first_pages = range(1, min(5, paginator.num_pages + 1))

    context = {
        'page_obj': page_obj,
        'first_pages': first_pages,
        'featured_products': featured_products,
        'query': query,
    }
    return render(request, 'product-list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    keywords = product.name.split()

    related_products = Product.objects.none()
    for word in keywords:
        related_products |= Product.objects.filter(name__icontains=word)

    related_products = related_products.exclude(id=product.id).distinct()[:3]

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'single-product.html', context)


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    first_pages = range(1, min(4, paginator.num_pages + 1))

    context = {
        "page_obj": page_obj,
        "first_pages": first_pages,
    }
    return render(request, "blog-list.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    keywords = blog.title.split()

    related_blogs = Blog.objects.none()
    for word in keywords:
        related_blogs |= Blog.objects.filter(title__icontains=word)

    related_blogs = related_blogs.exclude(id=blog.id).distinct()[:3]

    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }

    return render(request, 'single-blog.html', context)

# def slider(request):
#     sliders = Slider.objects.all()
#     return render(request, 'index.html', {
#         'sliders': sliders,
# })

def about_detail(request):
    members = About.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'about-us.html', context)

def call_detail(request):
    return render(request, 'call-us.html')