# Generated by Django 3.0.5 on 2020-04-18 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0013_committeespage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committee',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='committee',
            name='people',
        ),
        migrations.RemoveField(
            model_name='committeepage',
            name='committee',
        ),
        migrations.AddField(
            model_name='committeepage',
            name='formation_type',
            field=models.CharField(choices=[('C', 'Committee'), ('WG', 'Working Group')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='committeepage',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='committee_leader', to='committees.Person'),
        ),
        migrations.AddField(
            model_name='committeepage',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='committeepage',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='committee_member', to='committees.Person'),
        ),
    ]
