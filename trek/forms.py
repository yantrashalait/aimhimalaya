from django import forms
from .models import TripPersonalInfo, TripBooking, CustomTrip, Subscription, Review


class TripPersonalInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TripPersonalInfoForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone_number'].required = True
        self.fields['group_of_people'].required = True

    class Meta:
        model = TripPersonalInfo
        fields = ('title', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number',
                  'passport_number', 'place_of_issue', 'issue_date', 'expire_date', 
                  'emergency_contact_number', 'are_children_included', 'group_of_people', 
                  'people_above_60_age')


class TripBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TripBookForm, self).__init__(*args, **kwargs)
        self.fields['trip_name'].required = True
        self.fields['nationality'].required = True
        self.fields['start_date'].required = True

    class Meta:
        model = TripBooking
        fields = ('nationality', 'trip_name', 'start_date')


class CustomTripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomTripForm, self).__init__(*args, **kwargs)
        self.fields['trip_name'].required = True
        self.fields['duration'].required = True
        self.fields['price_range'].required = True
        self.fields['full_name'].required = True
        self.fields['email'].required = True
        self.fields['contact'].required = True

    class Meta:
        model = CustomTrip
        fields = ('trip_name', 'duration', 'price_range', 'full_name', 'email', 'country', 'contact', 'message')


class SubscriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = Subscription
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].required = True
        self.fields['email'].required = True
        self.fields['address'].required = True
        self.fields['review'].required = True
        self.fields['content'].required = True
        self.fields['contact'].required = True

    class Meta:
        model = Review
        fields = ('full_name', 'email', 'address', 'review', 'content', 'contact', 'rating')
