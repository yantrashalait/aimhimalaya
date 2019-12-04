from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    font_awesome_code = models.CharField(max_length=50, null=True, blank=True, help_text="Paste a font awesome code for activity icon here(e.g. fa-mountain, fa-hiking)")

    def __str__(self):
        return self.name


class Package(models.Model):
    PACKAGE_CHOICES = (
        ('Awesome', 'Awesome Tour'),
        ('Best', 'Best Offer'),
        ('Special', 'Special Package'),
        ('Popular', 'Popular Tour'),
    )
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Total time duration(in days)')
    price = models.FloatField(help_text='Price per person')
    minimum_group_size = models.IntegerField(null=True, blank=True)
    departure_from = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country,  null=True, blank=True, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, null=True, blank=True, on_delete=models.CASCADE)
    introduction = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    speciality = models.CharField(max_length=50, choices=PACKAGE_CHOICES, null=True, blank=True)
    activities = models.ManyToManyField(Activity, help_text='Activities included in the package')
    rating = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    map_image = models.ImageField(upload_to="package/map/", null=True, blank=True)

    def __str__(self):
        return self.name


class PackageImage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='package/images/', help_text="Image size: width=360px height=245px")

    # def save(self, *args, **kwargs):
    #     image = Image.open(self.image)
    #     image = image.convert('RGB')
    #     outputstream = BytesIO()
    #     imageresized = image.resize((300, 260))
    #     imageresized.save(outputstream, format='JPEG', quality=85)
    #     outputstream.seek(0)
    #     self.image = InMemoryUploadedFile(outputstream, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputstream), None)
    #     super(PackageImage, self).save(*args, **kwargs)


class PackageCostIncluded(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='cost_included')
    included_items = models.CharField(max_length=200, default='')


class PackageCostExluded(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='cost_excluded')
    excluded_items = models.CharField(max_length=200, default='')


class PackageItinerary(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='itinerary')
    day = models.IntegerField(help_text='Number of day(1, 2, 3, etc.)')
    place = models.CharField(max_length=200, null=True, blank=True)
    place_description = models.CharField(max_length=200, null=True, blank=True)
    outline = models.TextField(null=True, blank=True)
    description = models.TextField()
    meals = models.IntegerField(help_text='Served meals (in number)', null=True, blank=True)
    altitude = models.CharField(max_length=100, help_text='Altitude of the place', null=True, blank=True)
    accomodation = models.CharField(max_length=50, help_text='Type of Accomodation (Example: Hotel, Camp, etc.)', null=True, blank=True)
    travel = models.CharField(max_length=50, help_text='Type of travel (Example: Bus, Plane, Train, etc.)', null=True, blank=True)
    image = models.ImageField(upload_to='package/itinerary/', help_text="Image size: width=376px height=376px ")

    class Meta:
        ordering = ['day']

class Review(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100)
    review = models.CharField(max_length=255)
    content = models.TextField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name + ' ' + self.review

    class Meta:
        ordering = ['review_date']


class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='gallery/', help_text="Image size: width=350px height=350px")
    name = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     image = Image.open(self.image)
    #     image = image.convert('RGB')
    #     outputstream = BytesIO()
    #     imageresized = image.resize((700, 700))
    #     imageresized.save(outputstream, format='JPEG', quality=85)
    #     outputstream.seek(0)
    #     self.image = InMemoryUploadedFile(outputstream, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputstream), None)
    #     super(PhotoGallery, self).save(*args, **kwargs)


class HappyClient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    happy_review = models.TextField()
    profile_picture = models.ImageField(upload_to='clients/profile/', help_text="Image size: width=65px height=65px")
    cover_picture = models.ImageField(upload_to='clients/cover/', help_text="Image size: width=350px height=120px")

    def __str__(self):
        return self.name


class Subscription(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.email


class HeaderImage(models.Model):
    image = models.ImageField(upload_to='header/', help_text="Image size: width=1800px; height=600px")
    name = models.CharField(max_length=100, null=True, blank=True)
    banner_title = models.CharField(max_length=100, null=True, blank=True)
    banner_description = models.TextField(null=True, blank=True)
    package = models.ForeignKey(Package, related_name="banners", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomTrip(models.Model):
    trip_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, null=True, blank=True)
    price_range = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trip_name + ', ' + self.full_name

    class Meta:
        ordering = ['date']


TITLE_CHOICES = (
    ('mr.', 'Mr'),
    ('mrs.', 'Mrs.'),
    ('ms.', 'Miss'),
)


class TripBooking(models.Model):
    nationality = models.CharField(max_length=100, null=True, blank=True)
    trip_name = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='book')
    start_date = models.DateField(null=True, blank=True)
    booking_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.trip_name.name

    class Meta:
        ordering = ['booking_date']


class TripPersonalInfo(models.Model):
    trip_book = models.ForeignKey(TripBooking, on_delete=models.CASCADE, null=True, blank=True, related_name="person")
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=50, null=True, blank=True)
    place_of_issue = models.CharField(max_length=100, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=100, null=True, blank=True)
    group_of_people = models.IntegerField(null=True, blank=True)
    are_children_included = models.BooleanField(null=True, blank=True)
    people_above_60_age = models.IntegerField(default=0, help_text="Number of people above 60 years of age")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blogs/', help_text="Image size: width=370px height=370px")
    content = models.TextField()

    def __str__(self):
        return self.author + ' ' + self.title


class AboutUsDetail(models.Model):
    about_description = models.TextField()
    video_url = models.CharField(max_length=100, null=True, blank=True, help_text="Paste the youtube video url here")
    address = models.CharField(max_length=300, null=True, blank=True, help_text="Your address")
    contact_number = models.CharField(max_length=255, null=True, blank=True, help_text="Your contact Number")
    email = models.CharField(max_length=255, null=True, blank=True, help_text="Your email address")


class BlogBannerImage(models.Model):
    image = models.ImageField(upload_to='banner/blogs/', help_text="Image size: width=1803px height=380px")