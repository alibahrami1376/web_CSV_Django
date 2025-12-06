from django import forms
from projects.models import Projects, Category


class ProjectSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "جستجو در پروژه‌ها...", "class": "form-control"}
        ),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="همه دسته‌بندی‌ها",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    status = forms.ChoiceField(
        choices=[("", "همه وضعیت‌ها")] + Projects.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
