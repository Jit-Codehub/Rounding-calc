from django.contrib.sitemaps import Sitemap
from .urls import urlpatterns
from django.shortcuts import reverse
from datetime import datetime
from django.contrib import admin
from django.urls import path, include 
from .models import *



class percenttToDecimalCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return percenttToDecimalCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    


class decimalToPercentageCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return decimalToPercentageCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    



class moduloCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return moduloCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    


class dividedByWhatCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return dividedByWhatCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    

class negativeDividedCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return negativeDividedCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    


numbers={
     'percent-to-decimal-calculator-sitemap':percenttToDecimalCalculator_SiteMap,
     'decimal-to-percentage-calculator-sitemap':decimalToPercentageCalculator_SiteMap,
     'modulo-calculator-sitemap':moduloCalculator_SiteMap,
     'divided-by-what-calculator-sitemap':dividedByWhatCalculator_SiteMap,
     'negative-divided-calculator-sitemap':negativeDividedCalculator_SiteMap,

}

