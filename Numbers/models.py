from django.db import models

# Create your models here.
from datetime import *
from django.db import models

class TableStructure(models.Model):
    inputEnter = models.CharField(max_length=250)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    solutionTitle = models.CharField(max_length=250)
    date_modified = models.DateTimeField() 
 
    class Meta:
        abstract = True
 
    def __str__(self):
        """A string representation of the model."""
        return self.solutionTitle[:50]

class RoundingoffStructure(models.Model):
    inputEnter = models.CharField(max_length=250)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    solutionTitle = models.CharField(max_length=250)
    date_modified = models.DateTimeField() 
 
    class Meta:
        abstract = True
 
    def __str__(self):
        """A string representation of the model."""
        return self.solutionTitle[:50]


class percenttToDecimalCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "percenttToDecimalCalculator"


class decimalToPercentageCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "decimalToPercentageCalculator"


class moduloCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "moduloCalculator"


class dividedByWhatCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "dividedByWhatCalculator"        

class negativeDividedCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "negativeDividedCalculator"                

class productQuotientCalc(models.Model):
    prod=models.IntegerField()
    quo=models.IntegerField()
    x=models.DecimalField(max_digits=10 , decimal_places=5)
    y=models.DecimalField(max_digits=10 , decimal_places=5)

class quotientOfNumbersCalc(models.Model):
    quotient=models.DecimalField(max_digits=8, decimal_places=4)
    divisor=models.PositiveIntegerField()
    divident=models.PositiveIntegerField()
    remainder=models.PositiveIntegerField()

class fractionToDecimalCalc(models.Model):
    res=models.DecimalField(max_digits=8, decimal_places=4)
    numa=models.PositiveIntegerField()
    numb=models.PositiveIntegerField()

class factorPairCalc(models.Model):
    num=models.PositiveIntegerField()
    facs=models.CharField(max_length=255)

class sumofthree(models.Model):
    num1=models.CharField(max_length=100)
    result=models.CharField(max_length=100)
    detailSteps=models.TextField()
    url=models.CharField(max_length=200)        
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.num1