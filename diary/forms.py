from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from diary.models import Note


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class NoteForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        exclude = ['user']

    def clean_title(self):
        title = self.cleaned_data["title"]
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in forbidden_words:
            if word in title:
                raise ValidationError(
                    "Ваша тема записи содержит слова, которые включены в список запрещенных."
                )
        return title

    def clean_body(self):
        body = self.cleaned_data["body"]
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in forbidden_words:
            if word in body:
                raise ValidationError(
                    "Тело записи содержит слова, которые включены в список запрещенных."
                )
        return body
