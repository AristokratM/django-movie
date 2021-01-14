from django import forms
from .models import Reviews, RatingStar, Rating
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ReviewForm(forms.ModelForm):
    """Форма відгуків"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'parent', 'captcha')
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "id": "contactusername"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "id": "contactemail"}),
            "text": forms.Textarea(attrs={"class": "form-control border", "id": "contactcomment"}),

        }


class RatingForm(forms.ModelForm):
    """Форма додавання рейтингу"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
