import graphene
from graphene_django.types import ErrorType
from graphql_jwt.decorators import login_required

from merchant.models import Merchant, DynamicMerchantField
from payment.models import PaymentHistory


class FieldInput(graphene.InputObjectType):
    field_id = graphene.Int(required=True)
    value = graphene.String(required=True)


class PaymentInput(graphene.InputObjectType):
    merchant_id = graphene.Int(required=True)
    fields = graphene.List(FieldInput, required=True)


class ProcessPaymentMutation(graphene.Mutation):
    class Arguments:
        input = PaymentInput(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(self, info, input):
        user = info.context.user  # The authenticated user making the request
        merchant_id = input.merchant_id
        fields = input.fields
        print(user)
        try:
            merchant = Merchant.objects.get(id=merchant_id)
        except Merchant.DoesNotExist:
            return ProcessPaymentMutation(success=False, errors=[ErrorType(field="merchant_id", messages=["Invalid merchant ID"])])

        dynamic_fields = DynamicMerchantField.objects.filter(merchant=merchant)
        payment_amount = 0
        for field_input in fields:
            field_id = field_input['field_id']
            value = field_input['value']
            dynamic_field = dynamic_fields.get(id=field_id)
            if dynamic_field.field_type.title == 'payment_amount':
                payment_amount = value
        PaymentHistory.objects.create(
            user=user,
            merchant=merchant,
            amount=payment_amount
        )
        return ProcessPaymentMutation(success=True)

