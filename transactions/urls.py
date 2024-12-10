from django.urls import path
from .views import TransactionLogsView

urlpatterns = [
    path('transaction/<uuid:transaction_id>/', TransactionLogsView.as_view(), name='transaction-logs'),
]