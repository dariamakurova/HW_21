from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        restricted_words = ['казино',
                            'криптовалюта',
                            'крипта',
                            'биржа',
                            'дешево',
                            'бесплатно',
                            'обман',
                            'полиция',
                            'радар']

        words_found = [word for word in restricted_words if word in name.lower() or word in description.lower()]

        if words_found:
            raise ValidationError(f'Использованы недопустимые слова: {(', ').join(words_found)}')
        return cleaned_data


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price