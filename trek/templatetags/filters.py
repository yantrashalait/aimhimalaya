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


@register.filter
def separate_four(popular):
    total = len(popular)
    if total < 4:
        return range(1)
    else:
        if(total / 4) == 0:
            return range((total / 4))
        else:
            return range((total // 4) + 1)


@register.filter
def block_popular(popular, index=None):
    if index == 1:
        return Package.objects.filter(speciality='Popular')[:4]

    if index > 1:
        start = (index - 1) * 4
        end = start + 4
        print(start, end)
        print(Package.objects.filter(speciality='Popular')[start:end])
        return Package.objects.filter(speciality='Popular')[start:end]



