from django.db import models
from django.utils.timezone import now

class Transaction(models.Model):
    TRANSACTION_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILURE', 'Failure'),
    ]

    transaction_id = models.UUIDField(primary_key=True, editable=False)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES, default='PENDING')
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    num_characters = models.IntegerField(null=True, blank=True)
    duration_ms = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.status}"


class LogItem(models.Model):
    LOG_STATUS_CHOICES = [
        ('STARTED', 'Started'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    transaction = models.ForeignKey(Transaction, related_name="log_items", on_delete=models.CASCADE)
    step_name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=LOG_STATUS_CHOICES, default='STARTED')
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    duration_ms = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.step_name} - {self.status}"