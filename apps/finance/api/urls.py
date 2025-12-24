from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'feestructures', views.FeeStructureViewSet)
router.register(r'feediscounts', views.FeeDiscountViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoiceitems', views.InvoiceItemViewSet)
router.register(r'applieddiscounts', views.AppliedDiscountViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'refunds', views.RefundViewSet)
router.register(r'expensecategorys', views.ExpenseCategoryViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'budgets', views.BudgetViewSet)
router.register(r'budgetcategorys', views.BudgetCategoryViewSet)
router.register(r'budgetitems', views.BudgetItemViewSet)
router.register(r'budgettemplates', views.BudgetTemplateViewSet)
router.register(r'budgettemplateitems', views.BudgetTemplateItemViewSet)
router.register(r'financialtransactions', views.FinancialTransactionViewSet)
router.register(r'bankaccounts', views.BankAccountViewSet)
router.register(r'financialreports', views.FinancialReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
