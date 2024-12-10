from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transactions.models import Transaction, LogItem
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

# Serializers for Transaction and LogItem
class LogItemSerializer(ModelSerializer):
    class Meta:
        model = LogItem
        fields = ['step_name', 'status', 'start_time', 'end_time', 'message', 'duration_ms']

class TransactionSerializer(ModelSerializer):
    log_items = LogItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'status', 'start_time', 'end_time', 'num_pages', 'num_characters', 'duration_ms', 'log_items']

# View for fetching transaction logs
class TransactionLogsView(APIView):
    def get(self, request, transaction_id):
        """
        Retrieve transaction details and logs based on transaction UUID.
        """
        # Fetch the transaction using the transaction_id
        transaction = get_object_or_404(Transaction, transaction_id=transaction_id)

        # Serialize the transaction and its related log items
        serializer = TransactionSerializer(transaction)

        return Response(serializer.data, status=status.HTTP_200_OK)