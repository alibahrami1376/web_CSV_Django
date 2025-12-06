import logging
from django.forms import ModelForm
from django import forms
from blog.models import Newsletter

logger = logging.getLogger(__name__)


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(
                attrs={"placeholder": "ایمیل خود را وارد کنید", "required": True}
            )
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        logger.info(f"Validating newsletter email: {email}")
        if Newsletter.objects.filter(email=email).exists():
            logger.warning(f"Newsletter email already exists: {email}")
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        logger.info("Newsletter email validation passed!")
        logger.info("Everything is OK!")
        return email
