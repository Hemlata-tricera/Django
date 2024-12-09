from django.contrib import admin
from .models import User,Account,Budget,Category,Transaction


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # Display these fields in the admin list view
    search_fields = ['name']



class UserAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email_id')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'category', 'user', 'account')
    list_filter = ('category',)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance','user')




class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'start_date', 'end_date')
    ordering = ['category']  # Sort  by category in ascending order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    sortable_by = ('name',)







# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)