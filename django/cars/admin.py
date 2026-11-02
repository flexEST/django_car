
from django.contrib import admin
from .models import Car, CarImage


# Avtomobil şəkilləri
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 5
    max_num = 10


# Sürətli əməliyyatlar
@admin.action(description="Seçilmiş elanları satışa çıxar")
def mark_available(modeladmin, request, queryset):
    queryset.update(status='available')


@admin.action(description="Seçilmiş elanları rezerv et")
def mark_reserved(modeladmin, request, queryset):
    queryset.update(status='reserved')


@admin.action(description="Seçilmiş elanları satılmış et")
def mark_sold(modeladmin, request, queryset):
    queryset.update(status='sold')


@admin.action(description="Seçilmiş elanları ön plana çıxar")
def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)


@admin.action(description="Seçilmiş elanları ön plandan çıxar")
def remove_featured(modeladmin, request, queryset):
    queryset.update(is_featured=False)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    # Cədvəldə görünəcək sütunlar
    list_display = (
        'brand',
        'model',
        'year',
        'price',
        'mileage',
        'status',
        'is_featured',
        'stock_quantity',
        'created_at',
    )

    # Cədvəldə birbaşa dəyişdirilə bilən sahələr
    list_editable = (
        'status',
        'is_featured',
        'stock_quantity',
    )

    # Axtarış
    search_fields = (
        'brand',
        'model',
        'description',
    )

    # Filtrlər
    list_filter = (
        'status',
        'is_featured',
        'brand',
        'year',
        'fuel',
        'transmission',
        'created_at',
    )

    # Sürətli əməliyyatlar
    actions = [
        mark_available,
        mark_reserved,
        mark_sold,
        make_featured,
        remove_featured,
    ]

    # Avtomobil şəkilləri
    inlines = [CarImageInline]

    # Tarix üzrə naviqasiya
    date_hierarchy = 'created_at'

    # Sıralama
    ordering = ('-created_at',)

    # Səhifədə elan sayı
    list_per_page = 25

    # Tarix sahələri
    readonly_fields = (
        'created_at',
        'updated_at',
    )

    # Form bölmələri
    fieldsets = (
        ('Avtomobil məlumatları', {
            'fields': (
                'brand',
                'model',
                'year',
                'price',
                'mileage',
                'fuel',
                'transmission',
            )
        }),

        ('Şəkil və təsvir', {
            'fields': (
                'image',
                'description',
            )
        }),

        ('Satış və inventar idarəetməsi', {
            'fields': (
                'status',
                'is_featured',
                'stock_quantity',
            )
        }),

        ('Tarix məlumatları', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',),
        }),
    )
