from django import forms

from .models import Post


class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(
                        attrs={
                            'placeholder': "Your Post",
                            "class": "form-control"}
                    ))

    class Meta:
        model = Post
        fields = [
            "content"
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "abc":
            raise forms.ValidationError("Cannot be ABC")
        return content
