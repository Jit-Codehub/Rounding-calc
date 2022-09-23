from django.contrib import admin
from django.urls import path
from.views import *
urlpatterns = [
    path('', home,name='home'),
    
    path('percent-to-decimal-calculator/', percenttodecimalcalculator, name='percent-to-decimal-calculator'),
    path('<aa>-percentage-as-a-decimal/',percentagetodecimal_details, name = "percent-to-decimal-calculator-details"),

    path('decimal-as-percentage-calculator/',decimaltopercentagecalculator, name = "decimal-to-percentage"),
    path('<aa>-decimal-as-a-percentage/',decimaltopercentage, name = "decimal-to-percentage-details"),

    path('divided-by-what-equals-calculator/',dividedbywhatcalculator, name = "divided-by-what"),
    path('<aa>-divided-by-what-equals-to-<cc>/',dividedbywhatcalculatordetails, name = "divided-by-what-details"),
 
    path('negative-divided-by-negative-calculator/',negativedividedcalculator, name = "negative-divided-by-negative"),
    path('what-is-negative-<int:aa>-divided-by-negative-<int:cc>/',negativeDividedCalculatorDetails, name = "negative-divided-by-negative-details"),

    path('modulo-calculator/', modulocalculator, name='modulo-calculator'),
    path('what-is-<aa>-mod-<cc>/',modulocalculatordetails, name = "modulo-calculator-details"),

    path('product-quotient-calculator/',productQuotient, name='productQuotient'),
    path('what-two-numbers-have-a-product-of-<str:prod>-and-a-quotient-of-<str:quo>/',productQuotientTail, name='productQuotientTail'),

    path('quotient-of-numbers-calculator/',quotientOfNumbers, name='quotientOfNumbers'),
    path('what-is-the-quotient-of-<str:divident>-and-<str:divisor>/',quotientOfNumbersTail, name='quotientOfNumbersTail'),

    path('fraction-to-decimal-calculator/',fractionToDecimal, name='fractionToDecimal'),
    path('what-is-<int:numa>-<int:numb>-as-a-decimal/',fractionToDecimalTail, name='fractionToDecimalTail'),

    path('factor-pairs-calculator/',factorPair, name='factorPair'),
    path('factors-of-<int:num>-in-pairs/',factorPairTail, name='factorPairTail'),

    path('sum-of-three-consecutive-integers-calculator/',sumofthreeconsecutiveintegers, name='sumofInteger'),
    path('what-three-consecutive-integers-have-a-sum-of-<int:sum>/',whatsumofthreeconsecutiveintegers),
    path('what-three-consecutive-integers-have-a-sum-of-minus-<int:nsum>/',whatsumofthreeconsecutiveintegers),


]
