from django import forms
from .models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    """Форма відгуків"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'parent')


class RatingForm(forms.ModelForm):
    """Форма додавання рейтингу"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
