from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func_base(request):
    return HttpResponse("This is Function base view")


# #Django QuerySet- A QuerySet is a collection of data from a database.
# >>> from apps.finance_tracker.models import Transaction   # import Transaction model from finance_tracker app
#
# #1. all()-Retrieving All Objects(You can retrieve all records from the Transaction model by calling .all())
# >>> data = Transaction.objects.all()
# >>> print(data)
#
# # 2. first()- Return the first object from the QuerySet.
# >>> data = Transaction.objects.first()
# >>> print(data)
# Transaction object (1)
#
# #3. get()- Getting a Single Object-To retrieve a single object, you can use .get(). Note that it will raise a DoesNotExist exception if the object does not exist.
# >>> data = Transaction.objects.get(id=1)
# >>> print(data)
#
# # For accessing or print particular field
# >>> print(data.amount)
# 15000
# >>> print(data.description)
# Food and household shopping
#
#
# #4. Filter - Retrieve records matching certain conditions.
# >>> data = Transaction.objects.filter(id=1).values("amount", "description")
# >>> print(data)
# <QuerySet [{'amount': 15000, 'description': 'Food and household shopping'}]>
#
# To print sql query-
# >>> print(data.query)
# SELECT "finance_tracker_transaction"."amount", "finance_tracker_transaction"."description" FROM "finance_tracker_transaction" WHERE "finance_tracker_transaction"."id" = 1
#
#
# #5.ORDERED BY- To sort QuerySets, Django uses the order_by() method
# >>> amt_ordered = Budget.objects.all().order_by('amount').values()
# >>> print(amt_ordered)
#
#
# #6.Descending Order- For descending order, you can use a minus sign
# >>> amt_ordered_desc = Budget.objects.all().order_by('-amount').values()
# >>> print(amt_ordered_desc)
#
# #7. .count() – Count the number of records.
# >>> category_count = Budget.objects.count()
# >>> print(category_count)
# 3
#
# #8. .aggregate() – Perform aggregate calculations (like sum, avg).
# #-Avg()
# >>> from django.db.models import Avg
# >>> avg_amount = Budget.objects.all().aggregate(Avg('amount')) # You can also calculate the average
# >>> print(avg_amount)
#
# #Sum() - aggregate(Sum('field')) is used to calculate the sum of a field across all records in a QuerySet.
# >>> from django.db.models import Sum
# >>> sum_amount = Budget.objects.all().aggregate(Sum('amount'))
# >>> print(sum_amount)
#
# #9 exclude()-  to filter out records that match a certain condition
# >>> except_amt = Budget.objects.all().exclude(amount=2000)
# >>> print(except_amt)
#
# #10 Values() - Fetching Specific Fields
# >>> data = Budget.objects.all().values('user', 'category')  # To fetch only the the user and category field
# >>> print(data)



# Summary of Common Django ORM Methods:
# .all() – Retrieve all records.
# .filter() – Retrieve records matching certain conditions.
# .exclude() – Retrieve records excluding certain conditions.
# .get() – Retrieve a single record.
# .order_by() – Order records.
# .count() – Count the number of records.
# .aggregate() – Perform aggregate calculations (like sum, avg).
# .values() – Retrieve only certain fields.
# .distinct() – Remove duplicates from the QuerySet.
#

# 11.select related
# >>>from apps.finance_tracker.models import Category
# >>> from apps.finance_tracker.models import Budget
#
# >>> bud = Budget.objects.select_related('category').all()
# >>> for b in bud:
# ...     print(b.user, b.category.name)
# ...
# Hemlata Groceries
# Hemlata Dining
# Hemlata Salary





# 12.prefetch related

