# Generated by Django 2.2 on 2019-04-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0006_auto_20190420_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=60)),
                ('customer_email', models.EmailField(max_length=254)),
                ('status', models.IntegerField(choices=[(1, 'Processing'), (2, 'Completed')], default=1)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='catalog.Product')),
            ],
        ),
    ]
