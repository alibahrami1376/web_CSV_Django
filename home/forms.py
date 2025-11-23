from django.forms import ModelForm
from captcha.fields import CaptchaField
from home.models import Contact, Profile

class ContactForm(ModelForm):
    captcha = CaptchaField(label='کد امنیتی')
    
    class Meta:
        model = Contact
        fields = "__all__"

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'phone', 'location', 'website', 'github', 'linkedin', 'twitter']
        labels = {
            'avatar': 'آواتار',
            'bio': 'بیوگرافی',
            'phone': 'شماره تماس',
            'location': 'موقعیت',
            'website': 'وب‌سایت',
            'github': 'GitHub',
            'linkedin': 'LinkedIn',
            'twitter': 'Twitter',
        }