from django.shortcuts import render,redirect
import math
import random
from  random import randint
from math import ceil, floor
from .models import *
import datetime
from datetime import date
from datetime import datetime

#Function for getting the random numbers with n digits
def random_with_N_digits(range_start,range_end):
    l1=[]
    present=dict()
    for i in range(0,5):
       temp=randint(range_start, range_end)
       if temp not in present.keys():
            l1.append(temp)
            present[temp]=1
            
    return l1  


# Create your views here.
def home(request):
         return render(request,'base/math-calculator.html')


def percenttodecimalcalculator(request):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-percentage-as-a-decimal/')

    else:
         return render(request,'Mathcue/percent-to-decimal-calculator.html')

def percentagetodecimal_details(request,aa):
  if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-percentage-as-a-decimal/')
  else:    
    
    x = round(float(aa)/100,4)
    z = int(float(aa))
    
    query=percenttToDecimalCalculator.objects.filter(inputEnter=str(aa))
    if len(query)==0:
        solutionTitle="Percent to Decimal  Calculator | Free Calculator to find Percent to Decimal"
        detailStep=f'''<p>What is {aa} percent as a decimal? Get the answer for the question using the percent to decimal conversion. {aa} percent to a decimal is {x}</p><p>The given number is : {aa} </p><p>Divide a percent by 100 and remove the percent sign to convert from a percent to a decimal. Another way is to move the decimal two places left. </p><p>The formula to convert percent to decimal is <b>d = p÷ 100</b> </p>p>Let us convert {aa} percent as a decimal number with detailed explanation. </p> <ol><li>First write the percent in the form of fraction.<br> {aa}% = {aa}/100</li>  <br><li>Now divide {aa} by 100 to write in the decimal form.<br>  {aa} ÷ 100 = {x}</li></ol><p>So, {aa}% as a decimal is equal to {x}</p>'''
        finalAnswer=str(x)
        obj=percenttToDecimalCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="",date_modified=datetime.datetime.now())
        obj.save()

    list1 = []
    lst1 = []
    sum1 = z
    while sum1 < z+0.33:
        sum1 = round(sum1 +0.01,2)
        list1.append(sum1)
        per1 = round(sum1/100,4)
        lst1.append(per1)

    dict1 = dict(zip(list1, lst1))
    
    list2 = []
    lst2 = []
    sum2 = z + 0.33
    while sum2 < z+0.66:
        sum2 = round(sum2 +0.01,2)
        list2.append(sum2)
        per2 = round(sum2/100,4)
        lst2.append(per2)
    dict2 = dict(zip(list2, lst2))

    list3 = []
    lst3 = []
    sum3 = z + 0.66
    while sum3 < z+0.99:
        sum3 = round(sum3 +0.01,2)
        list3.append(sum3)
        per3 = round(sum3/100,4)
        lst3.append(per3)
    dict3 = dict(zip(list3, lst3))
    r1=int(floor(float(aa)))
    randList1=random_with_N_digits(r1+1,r1+100)
    context = {
        'dict1':dict1,
        'dict2':dict2,
        'dict3':dict3,
        'list1':list1,
        'list2':list2,
        'list3':list3,
        'lst1':lst1,
        'lst2':lst2,
        'lst3':lst3,
        'x':x,
        'aa':aa,
        'check':True,
        'id':1,
        'randList1':randList1
    }
    return render(request,'Mathcue/percent-to-decimal-calculator-details.html',context)



def decimaltopercentagecalculator(request):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-decimal-as-a-percentage/')

    else:
        return render(request,"Mathcue/decimal_percentage.html")


def decimaltopercentage(request,aa):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-decimal-as-a-percentage/')
    else:
        
        x = int(float(aa)*100)
        r1=int(floor(float(aa)))
        randList1=random_with_N_digits(r1+1,r1+100)
        query=decimalToPercentageCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Decimal to percent  Calculator makes it easy for you to find Decimal to percent "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Multiply a decimal by 100 and add the percent sign to convert from a decimal to a percent. </p> <p>The formula to convert Decimal to percent is <b>p = d x 100</b> </p> <p>Let us convert {aa} decimal as a percent number with detailed explanation. </p> <ul style="list-style: none;"> <li>Express the decimal number {aa} as a percent.</li> <li>To convert the decimal {aa} into a percentage you have to multiply {aa} by 100.</li> <li>{aa} × 100 = {x}</li> <li>Now add the % symbol to the obtained result.</li> <li>Thus {aa} as a percent is {x}%</li> </ul>'''
            finalAnswer=str(x)
            obj=decimalToPercentageCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="",date_modified=datetime.datetime.now())
            obj.save()

        list1 = []
        lst1 = []
        for i in range(1, 34):      
            z = str(aa)+str(i)
            #print(z)
            list1.append(z)
            zz = round(float(z)*100, 4)
            lst1.append(zz)
        dict1 = dict(zip(list1, lst1))


        list2 = []
        lst2 = []
        for i in range(34, 67):
            z = (str(aa)+str(i))
            list2.append(z)
            zz = round(float(z)*100, 4)
            lst2.append(zz)
        dict2 = dict(zip(list2, lst2))

        list3 = []
        lst3 = []
        for i in range(67, 100):
            z = (str(aa)+str(i))
            list3.append(z)
            zz = round(float(z)*100, 4)
            lst3.append(zz)
        dict3 = dict(zip(list3, lst3))

        
        context = {
            #'randomlist':randomlist,
            'x':x,
            'aa':aa,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'list1':list1,
            'list2':list2,
            'list3':list3,
            'lst1':lst1,
            'lst2':lst2,
            'lst3':lst3,
            
            'check':True,
            'id':1,
            'randList':randList1
                }
        return render(request,"Mathcue/decimaltopercentage_details.html", context) 



def dividedbywhatcalculator(request): 
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None
        return redirect(f'/{aa}-divided-by-what-equals-to-{cc}/')    

    else:
        return render(request,"Mathcue/dividedbywhat.html")

def dividedbywhatcalculatordetails(request,aa,cc):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None
        return redirect(f'/{aa}-divided-by-what-equals-to-{cc}/')    

    else:
        x = round(float(float(aa)/float(cc)) ,3)
        inputEnter=f"{aa},{cc}"

        query=dividedByWhatCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Divided by what equals  Calculatorr | Divided by what equals"
                finalAnswer=f"{x}"
                detailStep=f'''<p>The process to find out Divided by What Equals is given below. They are along the lines </p> <ol> <li>The first and foremost step is to identify the given inputs and unknown values to be found.</li> <li>Then, plug in the inputs in the formula divided by what equals i.e. Z/X = Y.</li> <li>Using the cross multiplication technique rewrite the equation.</li> <li>Solve for the unknown value easily.</li> </ol>'''
                obj=dividedByWhatCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug="",date_modified=datetime.datetime.now())
                obj.save()
        r1=int(floor(float(aa)))
        r2=int(floor(float(cc)))
        randList1=random_with_N_digits(r1+1,r1+100)
        randList2=random_with_N_digits(r2+1,r2+100)
            
        context = {
            'aa':aa,
            'cc':cc,
            'x':x,
            'check':True,
            'id':1,
            'randList1':randList1,
            'randList2':randList2
        }
        return render(request,"Mathcue/dividedbywhat-details.html", context)




def negativedividedcalculator(request): 
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if cc == None:
            cc = 1
        return redirect(f'/what-is-negative-{aa}-divided-by-negative-{cc}/')    
 
    else:
        return render(request,"Mathcue/negative-divided-by-negative.html")


def negativeDividedCalculatorDetails(request,aa,cc):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if cc == None:
            cc = 1
        return redirect(f'/what-is-negative-{aa}-divided-by-negative-{cc}/')    
 
    else:
        x = round(aa/cc,4)    
       
        inputEnter=f"{aa},{cc}"
        query=negativeDividedCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Negative Divided By Negative Calculator | Free Calculator to find Negative Divided By Negative"
                finalAnswer=f"{x}"
                detailStep=f'''p>See how to find the division of negative numbers - {aa} and - {cc} below</p> <p>-{aa} ÷ -{cc}</p> <p>Divide as if they are normal numbers</p> <p>= <span class="frac"><span>{aa}</span><span class="symbol">/</span><span class="bottom">{cc}</span></span></p> <p>= {x}</p> <p>The sign will be positive as both numbers have the same sign.</p> <br> <p>Therefore, - {aa} ÷ - {cc} is {x}.</p>'''
                obj=negativeDividedCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug="",date_modified=datetime.datetime.now())
                obj.save()

        r1=int(floor(float(aa)))
        r2=int(floor(float(cc)))
        randList1=random_with_N_digits(r1+1,r1+100)
        randList2=random_with_N_digits(r2+1,r2+100)   

        context = {
            'aa':aa,
            'cc':cc,
            'x':x,
            'check':True,
            'id':1,
            'randList1':randList1,
            'randList2':randList2,
        }
        return render(request,"Mathcue/negative-divided-by-negative-details.html", context)
        



def modulocalculator(request):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/what-is-{aa}-mod-{cc}/')
    else:
         return render(request,'Mathcue/modulo-calculator.html')


def modulocalculatordetails(request,aa,cc):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/what-is-{aa}-mod-{cc}/')
    
    else:
        x = int(float(aa)%float(cc))
        r =int(float(aa)//float(cc)) 
        inputEnter=f"{aa},{cc}"

        query=moduloCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Modulo Calculator | Free Calculator to find Modulo"
                finalAnswer=f"{x},{r}"
                detailStep=f'''<p>Solve the given problem what is {aa} mod {cc} by using the modulo calculation. a mod b means we have to divide <span class="frac"><span>a</span><span class="symbol">/</span><span class="bottom">b</span></span></p> <p>In mathematics, the modulo is the remainder or the number that’s left after a number is divided by another value. Modulo is also referred to as ‘mod.’</p> <p>Let us discuss {aa} mod {cc} in detail here.</p> <p><b>Solution:</b></p> <p>If you needed to find {aa} mod {cc}, divide {aa} by {cc}.</p> <ul> <li><p>{aa} mod {cc} = ?</p></li> <li><p>{aa} ÷ {cc} = {r} with a remainder of {x}</p></li> <li><p>{aa} mod {cc} = {x}</p></li> </ul>'''
                obj=moduloCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug="",date_modified=datetime.datetime.now())
                obj.save()
        randList1=random_with_N_digits(int(aa)-100,int(aa)+100)
        randList2=random_with_N_digits(int(cc)-100,int(cc)+100)
        
        context = {
            'aa':aa,
            'cc':cc,
            'x':x,
            'r':r,
            'check':True,
            'id':1,
            'randList1':randList1,
            'randList2':randList2
        }
        return render(request,'Mathcue/modulo-calculator-details.html',context)


def productQuotient(request):
    if request.method=='POST':

        prod=str(request.POST['prod'])
        quo=str(request.POST['quo'])
        return redirect('/what-two-numbers-have-a-product-of-{}-and-a-quotient-of-{}'.format(prod,quo))    
    else:
        return render(request,'Mathcue/product-quotient-calculator.html')
def productQuotientTail(request,prod,quo):
    prod=int(prod)
    quo=int(quo)
    l=productQuotientCalc.objects.filter(prod=prod,quo=quo)
    if l:
        print('from DB')
        product50=[]
        [product50.append(i) for i in range(prod+1,prod+51)]
        quotient50=[]
        [quotient50.append(i) for i in range(quo+1,quo+51)]
        ya50=[]
        [ya50.append(round(((prod/i)**0.5),4)) for i in quotient50]
        yb50=[]
        [yb50.append(round(((i/quo)**0.5),4)) for i in product50] 
        xa50=[]
        [xa50.append(round((prod/j),4)) for j in ya50]
        xb50=[]
        [xb50.append(round((i/j),4)) for i,j in zip(product50,yb50)]
        mylist=zip(quotient50,xa50,ya50)
        mylist1=zip(product50,xb50,yb50)
        product5=[]
        [product5.append(i) for i in range(prod+1,prod+6)]
        quotient5=[]
        [quotient5.append(i) for i in range(quo+1,quo+6)]
        return render(request,'Mathcue/product-quotient-calculator-details.html',{'res':l,'mylist':mylist,'mylist1':mylist1,'product5':product5,'quotient5':quotient5,'product':str(prod),'quotient':str(quo)})
    else:
        l=prodquocalc(prod,quo)
        print('fist time')
        product50=[]
        [product50.append(i) for i in range(prod+1,prod+51)]
        quotient50=[]
        [quotient50.append(i) for i in range(quo+1,quo+51)]
        ya50=[]
        [ya50.append(round(((prod/i)**0.5),4)) for i in quotient50]
        yb50=[]
        [yb50.append(round(((i/quo)**0.5),4)) for i in product50]       
        xa50=[]
        [xa50.append(round((prod/j),4)) for j in ya50]
        xb50=[]
        [xb50.append(round((i/j),4)) for i,j in zip(product50,yb50)]
        mylist=zip(quotient50,xa50,ya50)
        mylist1=zip(product50,xb50,yb50)
        product5=[]
        [product5.append(i) for i in range(prod+1,prod+6)]
        quotient5=[]
        [quotient5.append(i) for i in range(quo+1,quo+6)]
        return render(request,'Mathcue/product-quotient-calculator-details.html',{'res':l,'mylist':mylist,'mylist1':mylist1,'product5':product5,'quotient5':quotient5,'product':str(prod),'quotient':str(quo)}) 
def prodquocalc(prod,quo):
    y=(prod/quo)**0.5
    x=prod/y
    print(x,y)
    ins=productQuotientCalc(x=x,y=y,prod=prod,quo=quo)
    ins.save()
    l=productQuotientCalc.objects.filter(prod=prod,quo=quo)
    return l


def quotientOfNumbers(request):
    if request.method=='POST':

        divident=str(request.POST['divident'])
        divisor=str(request.POST['divisor'])
        return redirect('/what-is-the-quotient-of-{}-and-{}/'.format(divident,divisor))    
    else:
        return render(request,'Mathcue/quotient-of-numbers-calculator.html') 
def quotientOfNumbersTail(request,divident,divisor):
    divident=int(divident)
    divisor=int(divisor)
    l=quotientOfNumbersCalc.objects.filter(divident=divident,divisor=divisor)
    if l:
        print('from DB')
        div50=[]
        [div50.append(i) for i in range(divident+1,divident+51)]
        divi50=[]
        [divi50.append(i) for i in range(divisor+1,divisor+51)]
        quo=[]
        mylist=zip(div50,quo)
        
        [quo.append(round((div50[i]/divisor),4)) for i in range(0,50)]
        quo2=[]
        [quo2.append(round((divident/divi50[i]),4)) for i in range(0,50)]
        mylist1=zip(divi50,quo2)
        divisor5=[]
        divident5=[]
        [divisor5.append(str(i)) for i in range(divisor+1,divisor+6)]
        [divident5.append(str(i)) for i in range(divident+1,divident+6)]
        
        return render(request,'Mathcue/quotient-of-numbers-calculator-details.html/',{'res':l,'mylist':mylist,'mylist1':mylist1,'divisor5':divisor5,'divident5':divident5,'divident':str(divident),'divisor':str(divisor)})
    else:
        l=calcquotient(divident,divisor)
        print('fist time')
        div50=[]
        [div50.append(i) for i in range(divident+1,divident+51)]
        divi50=[]
        [divi50.append(i) for i in range(divisor+1,divisor+51)]
        quo=[]
        [quo.append(round((div50[i]/divisor),4)) for i in range(0,50)]
        quo2=[]
        [quo2.append(round((divident/divi50[i]),4)) for i in range(0,50)]
        mylist=zip(div50,quo)
        mylist1=zip(divi50,quo2)

        divisor5=[]
        divident5=[]
        [divisor5.append(str(i)) for i in range(divisor+1,divisor+6)]
        [divident5.append(str(i)) for i in range(divident+1,divident+6)]
        
        return render(request,'Mathcue/quotient-of-numbers-calculator-details.html/',{'res':l,'mylist':mylist,'mylist1':mylist1,'divisor5':divisor5,'divident5':divident5,'divident':str(divident),'divisor':str(divisor)})
   
def calcquotient(divident,divisor):
    quotient=divident/divisor
    remainder=divident%divisor
    ins=quotientOfNumbersCalc(divident=divident,quotient=quotient,divisor=divisor,remainder=remainder)
    ins.save()
    l=quotientOfNumbersCalc.objects.filter(divident=divident,divisor=divisor)
    return l


def fractionToDecimal(request):
    if request.method=='POST':

        numa=int(request.POST['numa'])
        numb=int(request.POST['numb'])
        return redirect('/what-is-{}-{}-as-a-decimal/'.format(numa,numb))    
    else:
        return render(request,'Mathcue/fraction-to-decimal-calculator.html')
    
def fractionToDecimalTail(request,numa,numb):
   
    l=fractionToDecimalCalc.objects.filter(numa=numa,numb=numb)
    if l:

        numa50=[]
        [numa50.append(i) for i in range(numa+1,numa+51)]
        numb50=[]
        [numb50.append(i) for i in range(numb+1,numb+51)]
        decia=[]
        [decia.append(round((numa/i),4)) for i in numb50]
        decib=[]
        [decib.append(round((i/numb),4)) for i in numa50]
        mylist=zip(numa50,decib)
        mylist1=zip(numb50,decia)

        numa5=[]
        numb5=[]
        [numa5.append(int(i)) for i in range(numa+1,numa+6)]
        [numb5.append(int(i)) for i in range(numb+1,numb+6)]
        return render(request,'Mathcue/fraction-to-decimal-calculator-details.html',{'res':l,'numa':numa,'numb':numb,'numa5':numa5,'numb5':numb5,'mylist':mylist,'mylist1':mylist1})
    else:
        l=decimalcalc(numa,numb)

        numa50=[]
        [numa50.append(i) for i in range(numa+1,numa+51)]
        numb50=[]
        [numb50.append(i) for i in range(numb+1,numb+51)]
        decia=[]
        [decia.append(round((numa/i),4)) for i in numb50]
        decib=[]
        [decib.append(round((i/numb),4)) for i in numa50]
        mylist=zip(numb50,decib)
        mylist1=zip(numa50,decia)

        numa5=[]
        numb5=[]
        [numa5.append(int(i)) for i in range(numa+1,numa+6)]
        [numb5.append(int(i)) for i in range(numb+1,numb+6)]
        return render(request,'Mathcue/fraction-to-decimal-calculator-details.html',{'res':l,'numa':numa,'numb':numb,'numa5':numa5,'numb5':numb5,'mylist':mylist,'mylist1':mylist1})
   
def decimalcalc(numa,numb):
    deci=numa/numb
    ins=fractionToDecimalCalc(res=deci,numa=numa,numb=numb)
    ins.save()
    l=fractionToDecimalCalc.objects.filter(numa=numa,numb=numb)
    return l

def factorPair(request):
    if request.method=='POST':

        numb=int(request.POST['num'])
        return redirect('/factors-of-{}-in-pairs'.format(numb))    
    else:
        return render(request,'Mathcue/factor-pairs-calculator.html')

    
def factorPairTail(request,num):
    fcs='1'
    for i in range(2,num):
        if num%i==0:
            fcs+=', '+ str(i)
    fcs+=' and '+str(num)
    l=factorPairCalc.objects.filter(num=num)
    if l:
        num10=[]
        [num10.append(i) for i in range(num+1,num+11)]
        return render(request,'Mathcue/factor-pairs-calculator-details.html',{'res':l,'num':num,'num10':num10,'fcs':fcs})
    else:
        l=factorcalc(num)
        num10=[]
        [num10.append(i) for i in range(num+1,num+11)]
        return render(request,'Mathcue/factor-pairs-calculator-details.html',{'res':l,'num':num,'num10':num10,'fcs':fcs})

   
def factorcalc(num):
    l={}

    for i in range(1,num+1):
        if num%i==0:
            l[str(i)+' x '+str(num//i)]=num
    for i in l:
        ins=factorPairCalc(num=num,facs=i)
        ins.save()
    l=factorPairCalc.objects.filter(num=num)
    return l





def sumofthreeconsecutiveintegers(request):
    if request.POST:
        sum=int(request.POST['sum'])
        if sum >= 0:
            return redirect(f'/what-three-consecutive-integers-have-a-sum-of-{sum}/')
        return redirect(f'/what-three-consecutive-integers-have-a-sum-of-minus{sum}/')
    else:
        return render(request,'Mathcue/sumofthreeconsecutiveintegers.html')


def whatsumofthreeconsecutiveintegers(request,sum=None,nsum=None):
    if sum != None:
        input=sum
        url = f'/what-three-consecutive-integers-have-a-sum-of-{input}/'
    else:
        input = -nsum
        url = f'/what-three-consecutive-integers-have-a-sum-of-minus{input}/'
    
    r = abs(int(input))
    randomList = [r+1,r+2,r+3,r+4,r+5,r+6,r+7,r+8,r+9,r+10]

    query = sumofthree.objects.filter(num1=input)
    if len(query)!=0:
        q = query[0]
        qresult = q.result.split(',')
        print(qresult)
        print(f'%%%%%%%%%%%%%%%%%%%%%DATABASE DATABASE%%%%%%%%%%')
        print(q.result[0],type(q.result[0]))
        
        context = {
            "input":input,
            "a":qresult[0],
            "b":qresult[1],
            "c":qresult[2],
            "a1":int(qresult[0])-1,
            "c1":int(qresult[2])+1,
            "randomList":randomList,
            "detailSteps":q.detailSteps,
            "result":"result",
        }
        print(context)
        return render(request,'Mathcue/whatsumofthreeconsecutiveintegers.html',context)

    result = (input - 3) / 3
    integerCheck = result % 1
    
    if integerCheck == 0:
        a = result
        b = result + 1
        c = result + 2
        detailSteps = f'''<h2>Detailed solutions for the three Consecutive Integers have a Sum of {input}</h2>
        <p>The detailed solution below will help you to identify the detailed description of the three Consecutive Integers having the sum of {input}.</p>
        <p>Let&rsquo;s assume,</p>
        <p>The first integer is x</p>
        <p>The second consecutive integer be x+1</p>
        <p>The third consecutive integer is x+2</p>
        <p>According to the question,</p>
        <p>&rArr; x + ( x+ 1) + ( x + 2 ) = {input}</p>
        <p>&rArr; 3x+3={input}</p>
        <p>&rArr; 3 ( x + 1) = {input}</p>
        <p>&rArr; x + 1 = {int(b)} ( because, 3*{int(b)} = {input} )</p>
        <p>&rArr; x = {int(b)} - 1 = {int(a)}</p>
        <p>&rArr; x + 2 = {int(a)} + 2 = {int(c)}</p>
        <p>Hence, the three Consecutive Integers have a Sum of {input} are {int(a)},{int(b)},{int(c)}.</p>'''

        obj = sumofthree(num1=input,result=f'{int(a)},{int(b)},{int(c)}',detailSteps=detailSteps,url=url,date_modified=datetime.now())
        obj.save()
        
        context = {
            "input":input,
            "a":int(a),
            "b":int(b),
            "c":int(c),
            "a1":int(a)-1,
            "c1":int(c)+1,
            "randomList":randomList,
            "detailSteps":detailSteps,
            "result":"result",
        }
        print(context)
        return render(request,'Mathcue/whatsumofthreeconsecutiveintegers.html',context)
        
    else:
        detailSteps = f'''<p>The detailed solution below will help you to identify the detailed description of the three Consecutive Integers having the sum of {input}.</p>
        <h2>Detailed solutions for the three Consecutive Integers have a Sum of {input}</h2>
        <p>Let&rsquo;s assume,</p>
        <p>The first integer is x</p>
        <p>The second consecutive integer be x+1</p>
        <p>The third consecutive integer is x+2</p>
        <p>According to the question,</p>
        <p>&rArr; x + ( x+ 1) + ( x + 2 ) = {input}</p>
        <p>&rArr; 3x+3={input}</p>
        <p>&rArr; 3x + 3 - 3 = {input} - 3</p>
        <p>&rArr; 3x = {input - 3}</p>
        <p>&rArr; x = {input - 3} / 3</p>
        <p>&rArr; x = {result}</p>
        <p  style="color: red;">Since x is not an integer, there are no three consecutive integers which add up to {input}.</p>'''

        context = {
            "input":input,
            "a":result,
            "randomList":randomList,
            'detailSteps':detailSteps,
        }
        print(context)
        return render(request,'Mathcue/whatsumofthreeconsecutiveintegers.html',context)
    



