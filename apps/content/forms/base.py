from django import forms

from apps.content.models import PageComponent


class BaseComponentForm(forms.ModelForm):

    class Meta:
        model = PageComponent
        fields = "__all__"
