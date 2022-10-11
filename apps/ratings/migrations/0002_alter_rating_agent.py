# Generated by Django 4.1.1 on 2022-10-10 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_phone_number'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_review', to='profiles.profile', verbose_name='Agent being rated'),
        ),
    ]