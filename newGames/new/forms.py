from django.forms import ModelForm
from .models import News


class CreateNewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'image', 'content', 'pub_add')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        i = 0
        for field_name, field in self.fields.items():
            i += 1
            field.widget.attrs['class'] = f'input_control {i}'
            field.help_text = ''
            # if field_name == 'name':
            #     field.widget.attrs['placeholder'] = field.label
            #     field.widget.attrs['style'] = 'display: none;'
            #     field.label = ''
            #     field.error_message = '1234567'
            # if field_name == 'email':
            #     field.widget.attrs['placeholder'] = 'Введите Email'
            #     field.widget.attrs['autofocus'] = 'true'
            #     field.label = ''
            #     field.error_message = '1234567'
            # if field_name == 'password1':
            #     field.widget.attrs['placeholder'] = 'Введите пароль'
            #     field.label = ''
            #     field.error_message = '123456'
            # if field_name == 'password2':
            #     field.widget.attrs['placeholder'] = 'Подтвердите пароль'
            #     field.label = ''
            #     field.error_message = '123'
            # if field_name == 'sex':
            #     field.widget.attrs['type'] = 'radio'
            #     # field.widget =
            #     field.label = ''
            #     field.error_message = '123456'
            # if field_name == 'avatar':
            #     field.widget.attrs['class'] = 'input-avatar'
            #     field.widget.attrs['onchange'] = 'showFileName()'
            #     field.label = ''