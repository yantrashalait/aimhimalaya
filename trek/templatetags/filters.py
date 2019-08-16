# -*- coding: utf-8 -*-

from django.template import Library
from django import template
from django.db.models import Q
from trek.models import Package, Activity, Review

register = Library()


@register.filter
def get_packages(activity):
    package = Package.objects.filter(speciality='Special', activities=activity)
    return package


@register.filter
def range_rating(rating):
    return range(int(str(rating).split('.')[0]))


@register.filter
def rating_decimal(rating):
    return int(str(rating).split('.')[1])


@register.filter
def get_review_count(package):
    return Review.objects.filter(package_id=package, accepted=True).count()


