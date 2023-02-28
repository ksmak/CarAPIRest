# Python modules
from typing import Any
from datetime import datetime
import random

# Django modules
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# Local
from cars.models import City, Brand, Body, Engine, Car

class Command(BaseCommand):
    """ Класс для заполнения рандомными данными базу данных """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def generate_five_cars(self) -> None:
        cities = []
        cities.append(City.objects.create(name="Астана"))
        cities.append(City.objects.create(name="Алматы"))
        cities.append(City.objects.create(name="Караганда"))
        cities.append(City.objects.create(name="Шымкент"))
        cities.append(City.objects.create(name="Жезказган"))
        brands = []
        brands.append(Brand.objects.create(name="Toyota"))
        brands.append(Brand.objects.create(name="Audi"))
        brands.append(Brand.objects.create(name="Mercedes"))
        brands.append(Brand.objects.create(name="Honda"))
        brands.append(Brand.objects.create(name="Wolkswagen"))
        bodies = []
        bodies.append(Body.objects.create(name="седан"))
        bodies.append(Body.objects.create(name="хэтчбек"))
        bodies.append(Body.objects.create(name="универсал"))
        bodies.append(Body.objects.create(name="кроссовер"))
        bodies.append(Body.objects.create(name="минивэн"))
        engines = []
        engines.append(Engine.objects.create(name="бензин"))
        engines.append(Engine.objects.create(name="дизель"))
        engines.append(Engine.objects.create(name="газ"))
        engines.append(Engine.objects.create(name="газ-бензин"))
        engines.append(Engine.objects.create(name="электрический"))
        user=get_user_model().objects.all().first()
        
        for _ in range(5):
            Car.objects.create(
                city=cities[random.randrange(0, len(cities))],
                brand=brands[random.randrange(0, len(brands))],
                year_of_manufacture=random.randrange(1990, 2024),
                price=random.randrange(1000000, 21000000),
                engine=engines[random.randrange(0, len(engines))],
                body=bodies[random.randrange(0, len(bodies))],
                capacity=random.randrange(1, 3),
                transmission=Car.TRANSMISSIONS[random.randrange(0, len(Car.TRANSMISSIONS))][0],
                drive=Car.DRIVERS[random.randrange(0, len(Car.DRIVERS))][0],
                wheel=Car.WHEELS[random.randrange(0, len(Car.WHEELS))][0],
                cleared_kz=True,
                user=user
            )
    
    def handle(self, *args: Any, **kwargs: Any) -> None:
        start: datetime = datetime.now()

        self.generate_five_cars()

        print(
            f"Genereated in: {(datetime.now()-start).total_seconds()}"
        )