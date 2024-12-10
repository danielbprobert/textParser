from django.contrib import admin
from .models import Transaction, LogItem

# Inline admin for LogItem
class LogItemInline(admin.TabularInline):
    model = LogItem
    extra = 0  # Do not show extra empty rows for new log items
    readonly_fields = ('step_name', 'status', 'start_time', 'end_time', 'message', 'duration_ms')

# Admin for Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'status', 'start_time', 'end_time', 'duration_ms')
    search_fields = ('transaction_id', 'status')
    list_filter = ('status', 'start_time', 'end_time')
    inlines = [LogItemInline]
    readonly_fields = ('transaction_id', 'status', 'start_time', 'end_time', 'duration_ms')

# Admin for LogItem (if needed as standalone view)
@admin.register(LogItem)
class LogItemAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'step_name', 'status', 'start_time', 'end_time', 'duration_ms')
    search_fields = ('transaction__transaction_id', 'step_name', 'status')
    list_filter = ('status', 'start_time', 'end_time')
    readonly_fields = ('transaction', 'step_name', 'status', 'start_time', 'end_time', 'message', 'duration_ms')
