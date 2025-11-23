from django.forms import ModelForm
from blog.models import Newsletter



class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"