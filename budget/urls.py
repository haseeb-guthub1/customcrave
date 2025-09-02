from django.urls import path
from . import views

urlpatterns = [
    path("budgets/", views.budget_list, name="budgets"),
    path("expenses/", views.expense_list, name="expenses"),
]
