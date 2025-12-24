from rest_framework import serializers
from apps.finance.models import *

class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = '__all__'
        ref_name = "FinanceAPIFeeStructureSerializer"

class FeeDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeDiscount
        fields = '__all__'
        ref_name = "FinanceAPIFeeDiscountSerializer"

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        ref_name = "FinanceAPIInvoiceSerializer"

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
        ref_name = "FinanceAPIInvoiceItemSerializer"

class AppliedDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedDiscount
        fields = '__all__'
        ref_name = "FinanceAPIAppliedDiscountSerializer"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        ref_name = "FinanceAPIPaymentSerializer"

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
        ref_name = "FinanceAPIRefundSerializer"

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'
        ref_name = "FinanceAPIExpenseCategorySerializer"

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        ref_name = "FinanceAPIExpense"

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        ref_name = "FinanceAPIBudgetSerializer"

class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = '__all__'
        ref_name = "FinanceAPIBudgetCategorySerializer"

class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetItem
        fields = '__all__'
        ref_name = "FinanceAPIBudgetItemSerializer"

class BudgetTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTemplate
        fields = '__all__'
        ref_name = "FinanceAPIBudgetTemplateSerializer"

class BudgetTemplateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTemplateItem
        fields = '__all__'
        ref_name = "FinanceAPIBudgetTemplateItemSerializer"

class FinancialTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTransaction
        fields = '__all__'
        ref_name = "FinanceAPIFinancialTransactionSerializer"

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
        ref_name = "FinanceAPIBankAccountSerializer"

class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'
        ref_name = "FinanceAPIFinancialReportSerializer"

