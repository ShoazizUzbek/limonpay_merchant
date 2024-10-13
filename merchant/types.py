import graphene
from graphene_django import DjangoObjectType

from common.models import Region, District, ElectricalNetworkDistrict, PaymentType
from merchant.models import MerchantCategory, FieldModel, DynamicMerchantField, Merchant


class FieldModelType(DjangoObjectType):
    class Meta:
        model = FieldModel
        fields = ('id', 'title', 'field_type')


class MerchantCategoryType(DjangoObjectType):
    class Meta:
        model = MerchantCategory
        fields = ('id', 'title', 'merchants')

    merchants = graphene.List(lambda: MerchantType)

    def resolve_merchants(self, info):
        return self.merchants.all()

class RegionType(DjangoObjectType):
    class Meta:
        model = Region
        fields = ('id', 'name')


class DistrictType(DjangoObjectType):
    class Meta:
        model = District
        fields = ('id', 'name', 'region')


class ElectricalNetworkDistrictType(DjangoObjectType):
    class Meta:
        model = ElectricalNetworkDistrict
        fields = ('id', 'name', 'region')


class PaymentModelType(DistrictType):
    class Meta:
        model = PaymentType
        fields = ('id', 'title', 'value')

class ContentTypeUnion(graphene.Union):
    class Meta:
        types = (RegionType, DistrictType, ElectricalNetworkDistrictType)

    @staticmethod
    def resolve_type(instance, info):
        if isinstance(instance, Region):
            return RegionType
        elif isinstance(instance, District):
            return DistrictType
        elif isinstance(instance, ElectricalNetworkDistrict):
            return ElectricalNetworkDistrictType
        return None

class DynamicMerchantFieldType(DjangoObjectType):
    class Meta:
        model = DynamicMerchantField
        fields = ('id', 'field_type', 'content_type')

    content_type = graphene.List(ContentTypeUnion)

    def resolve_content_type(self, info):
        if self.content_type:
            if self.content_type.model == 'region':
                return Region.objects.all()
            elif self.content_type.model == 'district':
                return District.objects.all()
            elif self.content_type.model == 'electricalnetworkdistrict':
                return ElectricalNetworkDistrict.objects.all()
            elif self.content_type.model == 'paymenttype':
                return PaymentType.objects.all()
        return None


class MerchantType(DjangoObjectType):
    class Meta:
        model = Merchant
        fields = ('id', 'title', 'category', 'fields')

    fields = graphene.List(DynamicMerchantFieldType)

    def resolve_fields(self, info):
        return self.fields.all()

