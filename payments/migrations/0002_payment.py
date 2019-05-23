# Generated by Django 2.2.1 on 2019-05-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0024_session_cost'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(max_length=350)),
                ('stripe_payment_id', models.CharField(max_length=350)),
                ('amount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='coderdojochi.Student')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session', to='coderdojochi.Session')),
            ],
        ),
    ]
