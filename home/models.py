import logging
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='بیوگرافی')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره تماس')
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name='موقعیت')
    website = models.URLField(blank=True, null=True, verbose_name='وب‌سایت')
    github = models.CharField(max_length=100, blank=True, null=True, verbose_name='GitHub')
    linkedin = models.CharField(max_length=100, blank=True, null=True, verbose_name='LinkedIn')
    twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name='Twitter')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل‌ها'
    
    def __str__(self):
        return f'پروفایل {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            logger.info(f'Creating profile for new user: {instance.username}')
            Profile.objects.create(user=instance)
            logger.info(f'Profile created successfully for user: {instance.username}')
            logger.info('Everything is OK!')
        except Exception as e:
            logger.error(f'Error creating profile for user {instance.username}: {e}')
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if not created:
        if hasattr(instance, 'profile'):
            try:
                logger.info(f'Saving profile for user: {instance.username}')
                instance.profile.save(update_fields=[])
                logger.info('Profile saved successfully!')
                logger.info('Everything is OK!')
            except Exception as e:
                logger.error(f'Error saving profile for user {instance.username}: {e}')