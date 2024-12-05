from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=1001)
    lname = models.CharField(max_length=100)
    email_id = models.EmailField(default="default@email.com")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fname


class Transaction(models.Model):
    amount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    transaction_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user= models.ForeignKey('User', on_delete=models.CASCADE, related_name="transactions")
    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name="transactions")




class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Enter category like Groceries, Salary, etc")
    description = models.TextField()

    def __str__(self):
        return self.name



class Budget(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='budgets')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()


ACCOUNT_NAME_CHOICES = [
    ('S', 'Saving'),
    ('C', 'Checking')
]

class Account(models.Model):
    name = models.CharField(max_length=100, default='saving', verbose_name="Account Name", choices=ACCOUNT_NAME_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return f"{self.name}"



