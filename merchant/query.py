import graphene
from django.db.models import Prefetch
from graphql_jwt.decorators import login_required

from common.models import Region, District, ElectricalNetworkDistrict, PaymentType
from merchant.models import MerchantCategory, Merchant, DynamicMerchantField
from merchant.types import MerchantCategoryType, MerchantType, RegionType, DistrictType, ElectricalNetworkDistrictType, \
    PaymentModelType


class Query(graphene.ObjectType):
    all_merchant_categories = graphene.List(MerchantCategoryType)

    merchants_by_category = graphene.List(MerchantType, category_id=graphene.Int())

    merchant_details = graphene.Field(MerchantType, merchant_id=graphene.Int())

    all_regions = graphene.List(RegionType)
    all_districts = graphene.List(DistrictType, region_id=graphene.Int())
    all_elect_net_districts = graphene.List(ElectricalNetworkDistrictType, region_id=graphene.Int())
    all_payment_types = graphene.List(PaymentModelType)

    @login_required
    def resolve_all_merchant_categories(self, info, ):
        return MerchantCategory.objects.prefetch_related(
            Prefetch(
                'merchants',
                queryset=Merchant.objects.prefetch_related(
                    Prefetch(
                        'fields',
                        queryset=DynamicMerchantField.objects.select_related('field_type')
                    )
                )
            )
        ).all()

    @login_required
    def resolve_merchants_by_category(self, info, category_id):
        return Merchant.objects.filter(category__id=category_id)

    @login_required
    def resolve_merchant_details(self, info, merchant_id):
        return Merchant.objects.get(id=merchant_id)

    @login_required
    def resolve_all_regions(self, info):
        return Region.objects.all()

    @login_required
    def resolve_all_districts(self, info, region_id):
        return District.objects.filter(region__id=region_id)

    @login_required
    def resolve_all_elect_net_districts(self, info, region_id):
        return ElectricalNetworkDistrict.objects.filter(region__id=region_id)

    @login_required
    def resolve_all_payment_types(self, info):
        return PaymentType.objects.all()