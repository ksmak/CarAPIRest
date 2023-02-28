# Django
from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    """Task model."""
    STATUS_NEW_TASK = 1
    STATUS_PROCESSING = 2
    STATUS_DONE = 3

    STATUSES = (
        (STATUS_NEW_TASK, 'Новое задание'),
        (STATUS_PROCESSING, 'Задание в процессе выполнения'),
        (STATUS_DONE, 'Задание выполнено'),
    )

    status = models.PositiveSmallIntegerField(
        verbose_name="статус",
        choices=STATUSES
    )

    title = models.CharField(
        verbose_name="название",
        max_length=150
    )

    description = models.TextField(
        verbose_name="описание"
    )

    user = models.ForeignKey(
        verbose_name="исполнитель",
        to=get_user_model(),
        on_delete=models.CASCADE
    )

    date_create = models.DateTimeField(
        verbose_name="дата создания",
        auto_now_add=True
    )

    date_done = models.DateTimeField(
        verbose_name="дата выполнения задания",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "задание"
        verbose_name_plural = "задания"
        ordering = ('date_create', )

    def __str__(self) -> str:
        return self.title
