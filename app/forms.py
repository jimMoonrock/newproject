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
class login_Form(forms.Form):
    input_login = forms.CharField(label="Your login",max_length=15)

class email_Form(forms.Form):
    email_form = forms.EmailField(max_length=15)


class password_Form(forms.Form):
    password_form = forms.PasswordInput()

class city_Form(forms.Form):
    city_form = forms.CharField(label="Your login",max_length=12)