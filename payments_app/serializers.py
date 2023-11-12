from rest_framework import serializers

class PaymentSerializer(serializers.Serializer):
    partner_order_id = serializers.CharField()
    partner_user_id = serializers.CharField()
    item_name = serializers.CharField()
    quantity = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    vat_amount = serializers.IntegerField()
    tax_free_amount = serializers.IntegerField()

class PaymentApprovalSerializer(serializers.Serializer):
    pg_token = serializers.CharField()