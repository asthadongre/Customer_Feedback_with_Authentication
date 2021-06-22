from django.contrib import admin
from app.models import Product, Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'date', 'happy',)
    list_filter = ('product', 'date',)
    search_fields = ('product__name', 'details',)

admin.site.register(Product)
admin.site.register(Feedback,FeedbackAdmin)