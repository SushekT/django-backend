# Generated by Django 4.0.5 on 2023-03-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('template_name', models.CharField(max_length=256)),
                ('profile_logo', models.ImageField(upload_to='profile/')),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('data', models.JSONField(default=dict)),
                ('html_template', models.TextField()),
                ('ts_template', models.TextField()),
                ('is_archived', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
