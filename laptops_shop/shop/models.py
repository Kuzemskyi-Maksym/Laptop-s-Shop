from django.db import models
from multiselectfield import MultiSelectField
from . import choises


def upload_files(instance, filename) -> str:
    return f"{instance.id}, {filename}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    brand = models.CharField(choices=choises.BRAND, max_length=100)
    image = models.ImageField(
        upload_to=upload_files,
        blank=False,
        null=False,
        height_field="height",
        width_field="width",
    )
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    screen_diagonal = models.CharField(choices=choises.SCREEN_DIAGONAL, max_length=40)
    screen_coating = models.CharField(choices=choises.SCREEN_COATING, max_length=40)
    in_stock = models.BooleanField(default=True)
    screen_resolution = models.CharField(
        choices=choises.SCREEN_RESOLUTION, max_length=40
    )
    touchscreen = models.BooleanField(default=False)
    processor = models.CharField(choices=choises.PROCESSOR, max_length=60)
    number_of_processor_cores = models.CharField(
        choices=choises.PROCESSOR_CORES, max_length=40
    )
    ram = models.CharField(choices=choises.RAM, max_length=60)
    ssd_scope = models.CharField(choices=choises.SSD_SCOPE, max_length=70)
    video_card_type = models.CharField(choices=choises.VIDEO_CARD_TYPE, max_length=50)
    keyboard_backlighting = models.BooleanField(default=True)
    os = models.CharField(choices=choises.OS, max_length=100)
    additionally = MultiSelectField(
        choices=choises.ADDITIONALLY, max_length=100)
    color = models.CharField(choices=choises.COLOR, max_length=100)
    is_new = models.BooleanField(default=True)

    def get_absolute_url(self) -> str:
        return f"/shop/detail/{self.id}"

    def __str__(self) -> str:
        return self.name
