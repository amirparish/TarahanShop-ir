from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='categories/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order'] 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='slider/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else f"Slider {self.id}"


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="brands/")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="دسته‌بندی"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    is_amazing = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    features = models.TextField(
        "ویژگی‌ها",
        blank=True,
        help_text="ویژگی‌ها را با '|' جدا کنید. حداکثر ۹ ویژگی."
    )

    class Meta:
        ordering = ["-created_at"]

    def get_features_list(self):
        """لیست ویژگی‌ها به صورت array"""
        if not self.features:
            return []
        return [f.strip() for f in self.features.split("|") if f.strip()][:9]

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="تیتر")
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    image = models.ImageField(upload_to="blogs/", verbose_name="تصویر")
    content = models.TextField(verbose_name="متن")
    author = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        default="تیم محتوای طراحان", 
        verbose_name="نویسنده"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ‌ها"

    def __str__(self):
        return self.title



# class SiteBase(models.Model):
#     site_name = models.CharField(max_length=100)
#     address = models.TextField(blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     whatsapp_link = models.URLField(blank=True, null=True)
#     instagram_link = models.URLField(blank=True, null=True)
#     fast_call = models.URLField(blank=True, null=True)
#     order_help_text = models.TextField(blank=True, null=True)
#     logo = models.ImageField(upload_to='sitebase/', blank=True, null=True)

#     class Meta:
#         verbose_name = "Site Base"
#         verbose_name_plural = "Site Base"

#     def __str__(self):
#         return self.site_name