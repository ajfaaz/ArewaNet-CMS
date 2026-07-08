from django import forms

from .base import BaseComponentForm


class HeroComponentForm(BaseComponentForm):

    overlay_opacity_percent = forms.IntegerField(
        label="Overlay Opacity (%)",
        min_value=0,
        max_value=100,
        initial=55,
    )

    class Meta(BaseComponentForm.Meta):
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.instance.pk:

            value = self.instance.get_config(
                "overlay_opacity",
                0.55,
            )

            self.fields["overlay_opacity_percent"].initial = int(value * 100)

    def save(self, commit=True):

        instance = super().save(commit=False)

        instance.set_config(
            "overlay_opacity",
            self.cleaned_data["overlay_opacity_percent"] / 100,
        )

        if commit:
            instance.save()

        return instance
