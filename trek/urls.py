from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.PackageDetail.as_view(), name='detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('offer-list/', views.OfferView.as_view(), name='offer_list'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),

    path('create-trip/', views.CreateTripView.as_view(), name='create_trip'),
    path('customize-trip/<int:pk>/', views.CustomizeTripView.as_view(), name='customize_trip'),

    path('search/', views.SearchView.as_view(), name='search'),
    path('success/', views.success, name='success'),
    path('package-list/', views.PackageListView.as_view(), name='package_listing'),
    path('popular-list/', views.PopularListView.as_view(), name='popular_listing'),

    path('book1/', views.Book1.as_view(), name='book1'),
    path('book1/<int:pk>/', views.PackageBook.as_view(), name='package_book'),
    path('book2/<int:pk>/', views.Book2.as_view(), name='book2'),
    # path('book3/', views.Book3.as_view(), name='book3'),

    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),

    path('generic/', views.GenericView.as_view(), name='generic'),
]
