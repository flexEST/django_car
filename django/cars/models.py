
from django.db import models


class Car(models.Model):

    STATUS_CHOICES = [
        ('available', 'Satışda'),
        ('reserved', 'Rezerv edilib'),
        ('sold', 'Satılıb'),
    ]

    # Əsas avtomobil məlumatları
    brand = models.CharField(
        max_length=100,
        verbose_name='Marka'
    )

    model = models.CharField(
        max_length=100,
        verbose_name='Model'
    )

    year = models.IntegerField(
        verbose_name='Buraxılış ili'
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Qiymət'
    )

    description = models.TextField(
        verbose_name='Təsvir'
    )

    image = models.ImageField(
        upload_to='cars/',
        verbose_name='Əsas şəkil'
    )

    mileage = models.IntegerField(
        default=0,
        verbose_name='Yürüş (km)'
    )

    fuel = models.CharField(
        max_length=50,
        verbose_name='Yanacaq növü'
    )

    transmission = models.CharField(
        max_length=50,
        verbose_name='Sürətlər qutusu'
    )

    # Satış statusu
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name='Satış statusu'
    )

    # Seçilmiş avtomobil
    is_featured = models.BooleanField(
        default=False,
        verbose_name='Seçilmiş elan'
    )

    # Stok sayı
    stock_quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Stok sayı'
    )

    # Tarixlər
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Əlavə olunma tarixi'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Son yenilənmə'
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillər'
        ordering = ['-created_at']


# Əlavə avtomobil şəkilləri
class CarImage(models.Model):

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='gallery',
        verbose_name='Avtomobil'
    )

    image = models.ImageField(
        upload_to='cars/gallery/',
        verbose_name='Şəkil'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Əlavə olunma tarixi'
    )

    def __str__(self):
        return f"{self.car.brand} {self.car.model} - Şəkil"

    class Meta:
        verbose_name = 'Avtomobil şəkli'
        verbose_name_plural = 'Avtomobil şəkilləri'
        ordering = ['id']
