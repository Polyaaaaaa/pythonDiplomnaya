from django.db import models

# Create your models here.


class Note():
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="diary_owner",
        verbose_name="Пользователь (если зарегистрирован)"
    )
    title = models.CharField(max_length=150, verbose_name="тема заметки")
    note = models.TextField(verbose_name="заметка")

    class Meta:
        verbose_name = "заметка"
        verbose_name_plural = "заметки"
        ordering = ["email", "full_name"]
        permissions = [
            ("can_unpublish_note", "Can unpublish note"),
            ("can_delete_note", "Can delete note"),
            ("view_all_note", "View all notes"),
            ("can_create_note", "Can create a note"),
            ("can_edit_note", "Can edit a note"),
        ]

    def __str__(self):
        return self.title

