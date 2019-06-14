''''''

'''Это определяет Form класс с одним полем ( your_name). Мы применили к полю удобную для человека метку, которая будет 
отображаться в момент <label>ее рендеринга (хотя в этом случае label мы указали на самом деле тот же самый, который 
будет сгенерирован автоматически, если мы его опускаем).

Максимально допустимая длина поля определяется как max_length. Это делает две вещи. Он вставляет maxlength="100"HTML-код 
<input>(поэтому браузер должен не допускать, чтобы пользователь вводил больше, чем это количество символов). Это также 
означает, что когда Django получит форму обратно из браузера, она проверит длину данных.

FormЭкземпляр имеет is_valid()метод, который запускает процедуры проверки для всех его полей. Когда этот метод вызывается,
 если все поля содержат действительные данные, он будет:

вернуть True
поместите данные формы в ее cleaned_data атрибут.
Вся форма при первом отображении будет выглядеть так'''
from django import forms
class Registration(forms.Form):
    login = forms.CharField(label="Your login",max_length=15, error_messages={"required":"Input your login"})
    email = forms.EmailField(max_length=15, error_messages={"required":"Input your email"})
    password = forms.PasswordInput()
    password_again = forms.PasswordInput()
    city = forms.CharField(label="Your city",max_length=12,  error_messages={"required":"Input your city"})

# Валидация проходит в этом методе
def clean(self):
    # Определяем правило валидиации
    if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
        # Выбрасываем ошибку, если пароли не савпали
        raise forms.ValidationError("Passwords must match ")

    return self.cleaned_data