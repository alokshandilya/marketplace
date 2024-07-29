from django import forms

from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image")

        widgets = {
            "category": forms.Select(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter item name",
                    "class": INPUT_CLASSES,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter item description",
                    "class": INPUT_CLASSES,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "Enter item price",
                    "class": INPUT_CLASSES,
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
        }
