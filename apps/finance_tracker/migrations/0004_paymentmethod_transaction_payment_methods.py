# Generated by Django 5.1.3 on 2024-12-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_tracker', '0003_remove_budget_category_id_remove_budget_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_methods',
            field=models.ManyToManyField(blank=True, related_name='transactions', to='finance_tracker.paymentmethod'),
        ),
    ]
