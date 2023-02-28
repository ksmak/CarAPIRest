# Django
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Project custom user model."""
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('username', )
    
    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return self.full_name