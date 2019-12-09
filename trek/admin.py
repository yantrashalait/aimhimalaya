from django.contrib import admin
from .models import Package, Review, Activity, Country, Destination, PhotoGallery, \
    HappyClient, HeaderImage, Subscription, PackageImage, PackageCostIncluded, BlogBannerImage, \
    PackageCostExluded, PackageItinerary, CustomTrip, TripBooking, TripPersonalInfo, Blog, AboutUsDetail,\
        Generic, TermsAndCondition, PaymentProcess

admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Activity)
admin.site.register(Review)
admin.site.register(PhotoGallery)
admin.site.register(HappyClient)
admin.site.register(Subscription)
admin.site.register(CustomTrip)
admin.site.register(AboutUsDetail)
admin.site.register(Generic)
admin.site.register(TermsAndCondition)
admin.site.register(PaymentProcess)


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
    readonly_fields = ['title', 'first_name', 'middle_name', 'last_name', 'email', 
    'phone_number', 'passport_number', 'place_of_issue', 'issue_date', 'expire_date', 
    'emergency_contact_number', 'group_of_people', 'are_children_included']


class TripBookingAdmin(admin.ModelAdmin):
    inlines = [TripPersonalInformationInline]
    readonly_fields = ['nationality', 'trip_name', 'start_date', 'booking_date']
    list_display = ('trip_name', 'nationality', 'start_date', 'booking_date')
    list_select_related = ('trip_name',)

    def get_package_detail(self, obj):
        return obj.trip_name + str(obj.trip_name.price)

    # def get_person(self, obj):
    #     return obj.person.first_name

admin.site.register(Package, PackageAdmin)
admin.site.register(HeaderImage)
admin.site.register(TripBooking, TripBookingAdmin)
admin.site.register(Blog)
admin.site.register(BlogBannerImage)
