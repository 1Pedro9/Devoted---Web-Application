from django.db import models
from django.utils import timezone

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=30)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.plan

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.category

class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    journal = models.CharField(max_length=5, default='cuj')
    date = models.DateTimeField(default=timezone.now)
    details = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return f"Journal {self.journal_id}"

class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    budget = models.CharField(max_length=100, default='Monthly Budget #1')
    date = models.DateTimeField(default=timezone.now)
    details = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.budget
