import graphene

from payment.mutations import ProcessPaymentMutation
from .mutations import Mutation as MerchantMutation
from .query import Query


class Mutation(MerchantMutation, graphene.ObjectType):
    process_payment = ProcessPaymentMutation.Field()  # Payment mutation

schema = graphene.Schema(query=Query, mutation=Mutation)