# Generated manually

from django.db import migrations, models


def remove_duplicate_emails(apps, schema_editor):
    """حذف ایمیل‌های تکراری قبل از اعمال unique constraint"""
    Newsletter = apps.get_model('blog', 'Newsletter')
    
    # پیدا کردن ایمیل‌های تکراری
    seen_emails = set()
    duplicates = []
    
    for newsletter in Newsletter.objects.all().order_by('id'):
        if newsletter.email.lower() in seen_emails:
            duplicates.append(newsletter.id)
        else:
            seen_emails.add(newsletter.email.lower())
    
    # حذف رکوردهای تکراری (نگه داشتن اولین رکورد)
    if duplicates:
        Newsletter.objects.filter(id__in=duplicates).delete()


def reverse_remove_duplicates(apps, schema_editor):
    """تابع معکوس - هیچ کاری انجام نمی‌دهد"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_url'),
    ]

    operations = [
        # ابتدا فیلد created_date را اضافه کن
        migrations.AddField(
            model_name='newsletter',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        # حذف ایمیل‌های تکراری
        migrations.RunPython(remove_duplicate_emails, reverse_remove_duplicates),
        # حالا unique constraint را اضافه کن
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(unique=True),
        ),
        # حذف null=True از created_date (اگر نیاز باشد)
        migrations.AlterField(
            model_name='newsletter',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        # اضافه کردن ordering
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['-created_date']},
        ),
    ]

