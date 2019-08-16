from django.contrib import admin
from .models import Package, Review, Activity, Country, Destination, PhotoGallery, \
    HappyClient, HeaderImage, Subscription, PackageImage, PackageCostIncluded, \
    PackageCostExluded, PackageItinerary, CustomTrip, TripBooking, TripPersonalInfo, Blog

admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Activity)
admin.site.register(Review)
admin.site.register(PhotoGallery)
admin.site.register(HappyClient)
admin.site.register(Subscription)
admin.site.register(CustomTrip)


class PackageImageInline(admin.TabularInline):
    model = PackageImage


class PackageIncludedCostInline(admin.TabularInline):
    model = PackageCostIncluded


class PackageExcludedCostInline(admin.TabularInline):
    model = PackageCostExluded


class PackageItineraryInline(admin.TabularInline):
    model = PackageItinerary


class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageImageInline, PackageIncludedCostInline, PackageExcludedCostInline, PackageItineraryInline]


class TripPersonalInformationInline(admin.TabularInline):
    model = TripPersonalInfo


class TripBookingAdmin(admin.ModelAdmin):
    inlines = [TripPersonalInformationInline]


admin.site.register(Package, PackageAdmin)
admin.site.register(HeaderImage)
admin.site.register(TripBooking, TripBookingAdmin)
admin.site.register(Blog)
