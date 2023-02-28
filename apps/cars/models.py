# Django
from django.db import models
from django.contrib.auth import get_user_model


class Brand(models.Model):
    """Brand model."""
    name = models.CharField(
        verbose_name="название",
        max_length=150
    )

    class Meta:
        verbose_name = "марка"
        verbose_name_plural = "марка"
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    """City model."""
    name = models.CharField(
        verbose_name="название",
        max_length=150
    )

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Body(models.Model):
    """Body model."""
    name = models.CharField(
        verbose_name="название",
        max_length=150
    )

    class Meta:
        verbose_name = "кузов"
        verbose_name_plural = "кузова"
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Engine(models.Model):
    """Engine model."""
    name = models.CharField(
        verbose_name="название",
        max_length=150
    )

    class Meta:
        verbose_name = "двигатель"
        verbose_name_plural = "двигатель"
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    """Car model."""
    TRANSMISSION_MECHANIC = 1
    TRANSMISSION_AUTOMATIC = 2
    TRANSMISSION_TIPTRONIC = 3
    TRANSMISSION_VARIATOR = 4
    TRANSMISSION_ROBOT = 5

    TRANSMISSIONS = (
        (TRANSMISSION_MECHANIC, "механика"),
        (TRANSMISSION_AUTOMATIC, "автомат"),
        (TRANSMISSION_TIPTRONIC, "типтроник"),
        (TRANSMISSION_VARIATOR, "вариатор"),
        (TRANSMISSION_ROBOT, "робот"),
    )

    DRIVE_FRONT_WHEEL = 1
    DRIVE_REAR_WHEEL = 2
    DRIVE_ALL_WHEEL = 3

    DRIVERS = (
        (DRIVE_FRONT_WHEEL, "передний привод"),
        (DRIVE_REAR_WHEEL, "задний привод"),
        (DRIVE_ALL_WHEEL, "полный привод"),
    )

    WHEEL_LEFT = 1
    WHEEL_RIGHT = 2

    WHEELS = (
        (WHEEL_LEFT, "слева"),
        (WHEEL_RIGHT, "справа"),
    )

    city = models.ForeignKey(
        verbose_name="город",
        to=City,
        on_delete=models.RESTRICT
    )

    brand = models.ForeignKey(
        verbose_name="марка",
        to=Brand,
        on_delete=models.RESTRICT
    )

    year_of_manufacture = models.PositiveSmallIntegerField(
        verbose_name="год выпуска",
        default=0
    )

    price = models.DecimalField(
        verbose_name="цена",
        max_digits=10,
        decimal_places=2
    )

    engine = models.ForeignKey(
        verbose_name="двигатель",
        to=Engine,
        on_delete=models.RESTRICT
    )

    body = models.ForeignKey(
        verbose_name="кузов",
        to=Body,
        on_delete=models.RESTRICT,
    )

    capacity = models.DecimalField(
        verbose_name="объем двигателя",
        max_digits=2,
        decimal_places=1
    )

    transmission = models.PositiveSmallIntegerField(
        verbose_name="коробка передач",
        choices=TRANSMISSIONS
    )

    drive = models.PositiveSmallIntegerField(
        verbose_name="привод",
        choices=DRIVERS
    )

    wheel = models.PositiveSmallIntegerField(
        verbose_name="руль",
        choices=WHEELS
    )

    cleared_kz = models.BooleanField(
        verbose_name="растаможен в Казахстане",
        default=False
    )

    description = models.TextField(
        verbose_name="описание",
        null=True,
        blank=True
    )

    date_create = models.DateTimeField(
        verbose_name="дата создания",
        auto_now_add=True
    )

    date_change = models.DateTimeField(
        verbose_name="дата изменения",
        auto_now=True
    )

    date_public = models.DateTimeField(
        verbose_name="дата публикации",
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name="изображение",
        upload_to='upload/'
    )

    user = models.ForeignKey(
        verbose_name="автор",
        to=get_user_model(),
        on_delete=models.RESTRICT
    )

    class Meta:
        verbose_name = "Автомашина"
        verbose_name_plural = "Автомашины"
        ordering = ('date_create', 'date_public')

    def __str__(self):
        return f"Автор:{self.user} - {self.name}, цена:{self.price}"
