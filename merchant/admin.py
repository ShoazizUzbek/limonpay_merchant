from django.contrib import admin

from common.models import Region, District, ElectricalNetworkDistrict, PaymentType
from merchant.models import MerchantCategory, Merchant, DynamicMerchantField, FieldModel


class DynamicMerchantFieldInline(admin.TabularInline):
    model = DynamicMerchantField
    extra = 0


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', )
    inlines = [DynamicMerchantFieldInline]


@admin.register(MerchantCategory)
class MerchantCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(FieldModel)
class FieldModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'field_type')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ElectricalNetworkDistrict)
class ElectricalNetworkDistrictAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')

