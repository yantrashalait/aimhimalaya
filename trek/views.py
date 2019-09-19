from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import redirect, render
from .models import Package, Review, Activity, HappyClient, PhotoGallery, Country, Destination, CustomTrip, \
    TripBooking, TripPersonalInfo, Subscription, Blog, HeaderImage, AboutUsDetail
from .forms import TripPersonalInfoForm, TripBookForm, CustomTripForm, SubscriptionForm, ReviewForm

from django.db.models import Q


class IndexView(TemplateView):
    template_name = 'trek/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['best'] = Package.objects.filter(speciality='Best')[:5]
        context['popular'] = Package.objects.filter(speciality='Popular')
        context['awesome'] = Package.objects.filter(speciality='Awesome')
        context['activities'] = Activity.objects.all()
        context['happy_clients'] = HappyClient.objects.all()
        context['gallery'] = PhotoGallery.objects.all()
        context['country'] = Country.objects.all()
        context['destination'] = Destination.objects.all()
        context['banner'] = HeaderImage.objects.all()
        context['about'] = AboutUsDetail.objects.last()
        return context


class PackageDetail(TemplateView):
    template_name = 'trek/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PackageDetail, self).get_context_data(**kwargs)
        package = Package.objects.get(id=kwargs.get('pk'))
        context['item'] = package
        package.views = package.views + 1
        package.save()

        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        package = Package.objects.get(id=kwargs.get('pk'))
        form = ReviewForm(request.POST)
        if not Subscription.objects.filter(email=form['email'].value()).exists():
            return render(request, 'trek/subscribe.html', {'message': 'You need to subscribe to post a review.'})
        else:
            obj = form.save(commit=False)
            obj.package = package
            obj.save()

            return HttpResponseRedirect(reverse('trek:detail', kwargs=({'pk': kwargs.get('pk')})) + '#tab-5')


class ContactView(TemplateView):
    template_name = 'trek/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['gallery'] = PhotoGallery.objects.all()
        context['about'] = AboutUsDetail.objects.last()
        return context


class OfferView(TemplateView):
    template_name = 'trek/offerlist.html'

    def get_context_data(self, **kwargs):
        context = super(OfferView, self).get_context_data(**kwargs)
        context['packages'] = Package.objects.filter(speciality='Best')
        context['country'] = Country.objects.all()
        context['destination'] = Destination.objects.all()
        context['activities'] = Activity.objects.all()
        context['happy_clients'] = HappyClient.objects.all()
        return context


class BlogsView(ListView):
    template_name = 'trek/blogs.html'
    model = Blog
    context_object_name = 'blogs'
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    template_name = 'trek/detailblog.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['related'] = Blog.objects.filter(~Q(id=kwargs.get('pk')))[:2]
        return context


class TermsView(TemplateView):
    template_name = 'trek/terms.html'


class CreateTripView(CreateView):
    template_name = 'trek/create.html'
    model = CustomTrip
    fields = '__all__'
    success_url = '/success/'


def success(request, *args, **kwargs):
    return render(request, 'trek/success.html')


class SearchView(TemplateView):
    template_name = 'trek/search.html'

    def post(self, request):
        activity = request.POST.get('activity')
        destination = request.POST.get('destination')
        country = request.POST.get('country')

        packages = Package.objects.all()
        if activity is not "":
            packages = packages.filter(activities=activity)

        if destination is not "":
            packages = packages.filter(destination=destination)

        if country is not "":
            packages = packages.filter(country=country)

        return render(request, self.template_name, {'packages': packages})


class PackageListView(TemplateView):
    template_name = 'trek/packagelisting.html'

    def get_context_data(self, **kwargs):
        context = super(PackageListView, self).get_context_data(**kwargs)
        context['packages'] = Package.objects.filter(speciality='Awesome')
        context['country'] = Country.objects.all()
        context['destination'] = Destination.objects.all()
        context['activities'] = Activity.objects.all()
        context['happy_clients'] = HappyClient.objects.all()
        return context


class PopularListView(TemplateView):
    template_name = 'trek/packagelisting.html'

    def get_context_data(self, **kwargs):
        context = super(PopularListView, self).get_context_data(**kwargs)
        context['packages'] = Package.objects.filter(speciality='Popular')
        context['country'] = Country.objects.all()
        context['destination'] = Destination.objects.all()
        context['activities'] = Activity.objects.all()
        context['happy_clients'] = HappyClient.objects.all()
        return context


class Book1(CreateView):
    template_name = 'trek/book1.html'
    model = TripBooking
    fields = ('nationality', 'trip_name', 'start_date')

    def get_success_url(self):
        return reverse('trek:book2', kwargs=({'pk': self.object.id}))


class Book2(TemplateView):
    template_name = 'trek/book2.html'

    def get(self, request, *args, **kwargs):
        form = TripPersonalInfoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TripPersonalInfoForm(request.POST)
        trip = TripBooking.objects.get(pk=kwargs.get('pk'))
        obj = form.save(commit=False)
        obj.trip_book = trip
        obj.save()
        return render(request, 'trek/book3.html')


class PackageBook(TemplateView):
    template_name = 'trek/book1.html'

    def get(self, request, *args, **kwargs):
        package = Package.objects.get(pk=kwargs.get('pk'))
        form = TripBookForm(initial={'trip_name': package})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TripBookForm(request.POST)
        obj = form.save(commit=True)
        return HttpResponseRedirect(reverse('trek:book2', kwargs=({'pk': obj.id})))


class CustomizeTripView(TemplateView):
    template_name = 'trek/create.html'

    def get(self, request, *args, **kwargs):
        package = Package.objects.get(pk=kwargs.get('pk'))
        form = CustomTripForm(initial={'trip_name': package.name, 'duration': package.duration})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomTripForm(request.POST)
        form.save(commit=True)
        return render(request, 'trek/success.html', {'message': 'Your trip has been created.', 'topic': 'Trip Customized'})


class SubscribeView(TemplateView):
    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if Subscription.objects.filter(email=form['email'].value()).exists():
            return render(request, 'trek/success.html', {'message': 'You have already subscribed.', 'topic': 'Subscription', 'head': 'Failed'})
        else:
            form.save()
        return render(request, 'trek/success.html', {'message': 'You have successfully subscribed to this website.', 'topic': 'Subscription'})


class GenericView(TemplateView):
    template_name = 'trek/generic.html'
