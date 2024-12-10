from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from transactions.models import Transaction, LogItem
from django.utils.timezone import now
import uuid

class TransactionLogsViewTestCase(TestCase):
    def setUp(self):
        """
        Set up mock data for testing.
        """
        self.client = APIClient()

        # Create a mock transaction
        self.transaction = Transaction.objects.create(
            transaction_id=uuid.uuid4(),
            status='SUCCESS',
            start_time=now(),
            end_time=now(),
            num_pages=10,
            num_characters=1000
        )

        # Create mock log items for the transaction
        LogItem.objects.create(
            transaction=self.transaction,
            step_name="Step 1",
            status="COMPLETED",
            start_time=now(),
            end_time=now(),
            message="Step 1 completed successfully."
        )
        LogItem.objects.create(
            transaction=self.transaction,
            step_name="Step 2",
            status="COMPLETED",
            start_time=now(),
            end_time=now(),
            message="Step 2 completed successfully."
        )

    def test_transaction_logs_view_valid_transaction(self):
        """
        Test the API with a valid transaction_id.
        """
        response = self.client.get(f'/transaction/{self.transaction.transaction_id}/')
        
        # Assert response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert response data
        data = response.json()
        self.assertEqual(data['transaction_id'], str(self.transaction.transaction_id))
        self.assertEqual(data['status'], 'SUCCESS')
        self.assertEqual(data['num_pages'], 10)
        self.assertEqual(data['num_characters'], 1000)
        self.assertEqual(len(data['log_items']), 2)

        # Check log items
        log_items = data['log_items']
        self.assertEqual(log_items[0]['step_name'], "Step 1")
        self.assertEqual(log_items[0]['status'], "COMPLETED")
        self.assertEqual(log_items[1]['step_name'], "Step 2")
        self.assertEqual(log_items[1]['status'], "COMPLETED")

    def test_transaction_logs_view_invalid_transaction(self):
        """
        Test the API with an invalid transaction_id.
        """
        invalid_transaction_id = uuid.uuid4()
        response = self.client.get(f'/transaction/{invalid_transaction_id}/')

        # Assert response status
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
