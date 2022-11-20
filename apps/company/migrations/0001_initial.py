# Generated by Django 4.0.5 on 2022-11-19 17:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('company_address', models.CharField(max_length=300)),
                ('company_number', models.PositiveBigIntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 05999999999', regex='^(977)\\d{10}$')])),
                ('email_address', models.EmailField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('start_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('is_complete', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('companybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.companybasemodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('company.companybasemodel',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('ToDo', 'ToDo'), ('InProgress', 'InProgress'), ('Pending', 'Pending'), ('Done', 'Done')], default='ToDo', max_length=100)),
                ('deadline', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='company.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='company.organization'),
        ),
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='company.organization'),
        ),
    ]