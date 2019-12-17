import io
import json

from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, request, FileResponse
from django.shortcuts import redirect, render
from .models import Package, Review, Activity, HappyClient, PhotoGallery, Country, Destination, CustomTrip, \
    TripBooking, TripPersonalInfo, Subscription, Blog, HeaderImage, AboutUsDetail, BlogBannerImage, Generic,\
        TermsAndCondition, PaymentProcess
from .forms import TripPersonalInfoForm, TripBookForm, CustomTripForm, SubscriptionForm, ReviewForm
from django.http import JsonResponse
from django.db.models import Q

from reportlab.pdfgen import canvas
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape


class IndexView(TemplateView):
    template_name = 'trek/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['best'] = Package.objects.filter(speciality='Best')[:5]
        context['popular'] = Package.objects.filter(speciality='Popular')
        context['awesome'] = Package.objects.filter(speciality='Awesome')
        context['search_activities'] = Activity.objects.all()
        context['activities'] = Activity.objects.filter(hidden=False)
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
        context['banner'] = BlogBannerImage.objects.last()
        return context

    def post(self, request, *args, **kwargs):
        package = Package.objects.get(id=kwargs.get('pk'))
        form = ReviewForm(request.POST)
        
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
        context['banner'] = BlogBannerImage.objects.last()
        context['name'] = "Best Offers"
        return context


class BlogsView(ListView):
    template_name = 'trek/blogs.html'
    model = Blog
    context_object_name = 'blogs'
    queryset = Blog.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        return context


class BlogDetailView(DetailView):
    template_name = 'trek/detailblog.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['related'] = Blog.objects.filter(~Q(id=kwargs.get('pk')))[:2]
        context['banner'] = BlogBannerImage.objects.last()
        return context


class TermsView(TemplateView):
    template_name = 'trek/terms.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TermsView, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        context['terms'] = TermsAndCondition.objects.last()
        return context


class CreateTripView(CreateView):
    template_name = 'trek/create.html'
    model = CustomTrip
    fields = '__all__'
    success_url = '/success/'

    def get_context_data(self, *args, **kwargs):
        context = super(CreateTripView, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        return context   


def success(request, *args, **kwargs):
    banner = BlogBannerImage.objects.last()
    return render(request, 'trek/success.html', {'banner': banner})


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
    
    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        return context


class PackageListView(TemplateView):
    template_name = 'trek/packagelisting.html'

    def get_context_data(self, **kwargs):
        context = super(PackageListView, self).get_context_data(**kwargs)
        context['packages'] = Package.objects.filter(speciality='Awesome')
        context['country'] = Country.objects.all()
        context['destination'] = Destination.objects.all()
        context['activities'] = Activity.objects.all()
        context['happy_clients'] = HappyClient.objects.all()
        context['banner'] = BlogBannerImage.objects.last()
        context['name'] = "Awesome Tours"
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
        context['banner'] = BlogBannerImage.objects.last()
        context['name'] = "Popular Tours"
        return context


class Book1(CreateView):
    template_name = 'trek/book1.html'
    model = TripBooking
    fields = ('nationality', 'trip_name', 'start_date')

    def get_context_data(self, *args, **kwargs):
        context = super(Book1, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        return context

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
        payment = PaymentProcess.objects.last()
        return render(request, 'trek/book3.html', {'payment': payment})
    
    def get_context_data(self, *args, **kwargs):
        context = super(Book2, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        return context


class PackageBook(TemplateView):
    template_name = 'trek/book1.html'

    def get(self, request, *args, **kwargs):
        banner = BlogBannerImage.objects.last()
        package = Package.objects.get(pk=kwargs.get('pk'))
        form = TripBookForm(initial={'trip_name': package})
        return render(request, self.template_name, {'form': form, 'banner': banner})

    def post(self, request, *args, **kwargs):
        form = TripBookForm(request.POST)
        obj = form.save(commit=True)
        return HttpResponseRedirect(reverse('trek:book2', kwargs=({'pk': obj.id})))


class CustomizeTripView(TemplateView):
    template_name = 'trek/create.html'

    def get(self, request, *args, **kwargs):
        banner = BlogBannerImage.objects.last()
        package = Package.objects.get(pk=kwargs.get('pk'))
        form = CustomTripForm(initial={'trip_name': package.name, 'duration': package.duration})
        return render(request, self.template_name, {'form': form, 'banner': banner})

    def post(self, request, *args, **kwargs):
        form = CustomTripForm(request.POST)
        form.save(commit=True)
        about = AboutUsDetail.objects.last()
        return render(request, 'trek/success.html', {'message': 'Your trip has been created.', 'topic': 'Trip Customized', 'banner': BlogBannerImage.objects.last(), 'about': about})


class SubscribeView(TemplateView):
    template_name = 'trek/success.html'
    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        about = AboutUsDetail.objects.last()
        if Subscription.objects.filter(email=form['email'].value()).exists():
            return render(request, self.template_name, {'message': 'You have already subscribed.', 'topic': 'Subscription', 'head': 'Failed', 'banner': BlogBannerImage.objects.last(), 'about': about})
        else:
            form.save()
        return render(request, self.template_name, {'message': 'You have successfully subscribed to this website.', 'topic': 'Subscription', 'banner': BlogBannerImage.objects.last(), 'about': about})


class GenericView(TemplateView):
    template_name = 'trek/generic.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GenericView, self).get_context_data(**kwargs)
        context['banner'] = BlogBannerImage.objects.last()
        context['generic'] = Generic.objects.get(pk=self.kwargs.get('pk'))
        return context


def get_destination(request, *args, **kwargs):
    if request.method == 'GET':
        act = request.GET.get('activity')
        act = act.replace('act_', '')
        destination = Destination.objects.filter(package__activities__id=act).distinct().values('name', 'id')
        dst = json.dumps(list(destination))
        return JsonResponse(dst, safe=False)


def get_activity(request, *args, **kwargs):
    if request.method == 'GET':
        act = request.GET.get('country')
        act = act.replace('count_', '')
        activities = Activity.objects.filter(package__activities__id=act).distinct().values('name', 'id')
        act = json.dumps(list(activities))
        return JsonResponse(act, safe=False)


def download_terms(request):
    content = TermsAndCondition.objects.last().content

    data = {'content': content}

    template = get_template('trek/download.html')
    html  = template.render(data)

    file = open('Terms.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()            
    return HttpResponse(pdf, 'application/pdf')


def download_payment(request):
    content = PaymentProcess.objects.last().content

    data = {'content': content}

    template = get_template('trek/download.html')
    html  = template.render(data)

    file = open('Payment.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()            
    return HttpResponse(pdf, 'application/pdf')
