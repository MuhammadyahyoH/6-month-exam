from django.db import models
from django.db.models import CharField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        permissions = [
            ("can_change_status", "Can change contact status"),
        ]


class BannerType(models.TextChoices):
    CATEGORY = 'CATEGORY', 'Category'
    INTRO = 'INTRO', 'Intro'

class BannerModel(BaseModel):
    image = models.ImageField(upload_to='banners/')
    title = CharField(max_length=256)
    subtitle = models.CharField(max_length=128, blank=True)
    description = models.TextField()
    text = CharField(max_length=128)
    url = models.URLField(max_length=500, blank=True, null=True)
    banner_type = models.CharField(
        max_length=20,
        choices=BannerType.choices,
        default=BannerType.CATEGORY
    )
    is_active = models.BooleanField(default=True)


class SliderModel(BaseModel):
    image = models.ImageField(upload_to='sliders/')
    image_small = models.ImageField(upload_to='sliders/', null=True, blank=True)
    subtitle = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
        ordering = ['order']