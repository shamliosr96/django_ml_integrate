# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from myapp.scripts.wine_script import TestSplitwine
from myapp.scripts.migration import migration2
from myapp.extrascript import TestSpli
from myapp.scripts.heart import TestSpli2
from myapp.scripts.diabetes import diabetes2
from myapp.scripts.Glass import Fglass
from myapp.scripts.liverscript import checkliver
from  myapp.scripts.irisscript import Firis
from  myapp.scripts.lenses import reales
from  myapp.scripts.balance import bal
from myapp.scripts.script_breast_cancer import TestSplitcancer
from myapp.scripts.blood import Fblood
from myapp.scripts.happiness import happy
from myapp.scripts.poker import Fpoker
from myapp.scripts.haberman import Fhaber
from myapp.scripts.teaching_script import TestSplitteach
from myapp.scripts.credit_script import TestSplitcredit
from myapp.scripts.new_wheat import TestSplitseed
from myapp.scripts.titanic_script import TestSplittitanic

def home(request):
   return render(request, "home.html", {})

def contact(request):
    return  render(request,'contactus.html',locals())
def about(request):
    return  render(request,'About_us.html',locals())

def migration(request):
    if request.method == 'POST':
        Assessment= request.POST['Assessment']
        Age= request.POST['Age']
        Shape=request.POST['Shape']
        Margin=request.POST['Margin']
        Density=request.POST['Density']
        mlist=[]
        mtest=[]
        mlist.append(Assessment)
        mlist.append(Age)
        mlist.append(Shape)
        mlist.append(Margin)
        mlist.append(Density)
        mtest.append(mlist)
        mig=migration2(mtest)
        migrane=[]
        if mig[0]==0:
            migrane.append('Not_Present')
        elif mig[0]==1:
            migrane.append('migration_Present')

    return render(request, "migration.html", locals())

def wine(request):
    msg = ''
    if request.method == 'POST':
        Malic_acid = request.POST['Malic_acid']
        Ash = request.POST['Ash']
        Alcalinity_of_ash = request.POST['Alcalinity_of_ash']
        Magnesium = request.POST['Magnesium']
        Total_phenols = request.POST['Total_phenols']
        Flavanoids = request.POST['Flavanoids']
        Nonflavanoid = request.POST['Nonflavanoid']
        Proanthocyanins = request.POST['Proanthocyanins']
        Color_intensity = request.POST['Color_intensity']
        Hue = request.POST['Hue']
        diluted_wines = request.POST['diluted_wines']
        Proline = request.POST['Proline']
        msg = "Successfully Enter the data ! Please wait Now for results"
        List = []
        test = []
        List.append(Malic_acid)
        List.append(Ash)
        List.append(Alcalinity_of_ash)
        List.append(Magnesium)
        List.append(Total_phenols)
        List.append(Flavanoids)
        List.append(Nonflavanoid)
        List.append(Proanthocyanins)
        List.append(Color_intensity)
        List.append(Hue)
        List.append(diluted_wines)
        List.append(Proline)
        print(List)
        test.append(List)
        abcd = TestSplitwine(test)
        wine_pre = []
        if abcd[0] == 0:
            wine_pre.append('bad_quality')
        elif abcd[0] == 1:
            wine_pre.append('good_quality')
    return render(request, 'wine.html', locals())

def car(request):
    msg = ''
    if request.method == 'POST':
        AGE = request.POST['AGE']
        Salary = request.POST['Salary']
        msg = 'Successfully Enter the data ! Please wait Now for results'
        list1 = []
        test = []
        list1.append(AGE)
        list1.append(Salary)
        test.append(list1)
        abc = TestSpli(test)
        car_pre = []
        if abc[0] == 0:
            car_pre.append('cannot_buy')
        elif abc[0] == 1:
            car_pre.append('can_buy')

    return render(request, "car.html", locals())

def heart(request):
    if request.method == 'POST':
        BP= request.POST['Blood_Pressure']
        Chlestrol = request.POST['Chlestrol']
        Sugar= request.POST['Blood_Sugar']
        ECG = request.POST['ECG']
        Heart= request.POST['Heartrate']
        EIA = request.POST['EIA']
        Oldpeak= request.POST['oldpeak']
        Slope = request.POST['Slope']
        Vessels = request.POST['Vessels']
        Thal= request.POST['Thal']
        hlist=[]
        htest=[]
        hlist.append(BP)
        hlist.append(Chlestrol)
        hlist.append(Sugar)
        hlist.append(ECG)
        hlist.append(Heart)
        hlist.append(EIA)
        hlist.append(Oldpeak)
        hlist.append(Slope)
        hlist.append(Vessels)
        hlist.append(Thal)
        htest.append(hlist)
        abc= TestSpli2(htest)
        heart_pre = []
        if abc[0] == 0:
            heart_pre.append('no_heart_disease')
        elif abc[0] == 1:
            heart_pre.append('have_heart_disease')

    return render(request,'heart.html',locals())

def diabetes(request):
    if request.method == 'POST':
        preg = request.POST['Pregnancies']
        Glucose = request.POST['Glucose']
        BP = request.POST['Blood_pressure']
        ST = request.POST['Skin_thickness']
        Insulin = request.POST['Insulin']
        DPF= request.POST['DPF']
        Age = request.POST['Age']
        Dlist=[]
        outcome=[]
        Dlist.append(preg)
        Dlist.append(Glucose)
        Dlist.append(BP)
        Dlist.append(ST)
        Dlist.append(Insulin)
        Dlist.append(DPF)
        Dlist.append(Age)
        outcome.append(Dlist)
        output=diabetes2(outcome)
        diabtets_pre=[]
        if output[0]==0:
            diabtets_pre.append('Not_Present')
        elif output[0]==1:
            diabtets_pre.append('Diabetes_Present')
        print(output)


    return render(request, "diabetes.html", locals())


def Glass(request):
    if request.method == 'POST':
        RI = request.POST['RI']
        SO = request.POST['SO']
        MO = request.POST['MO']
        AO = request.POST['AO']
        S = request.POST['Silicon']
        PO = request.POST['PO']
        CO = request.POST['CO']
        BO = request.POST['BO']
        IO = request.POST['IO']
        Dlist = []
        out = []
        Dlist.append(RI)
        Dlist.append(SO)
        Dlist.append(MO)
        Dlist.append(AO)
        Dlist.append(S)
        Dlist.append(PO)
        Dlist.append(CO)
        Dlist.append(BO)
        Dlist.append(IO)
        out.append(Dlist)
        output2 = Fglass(out)
        print(output2)

    return render(request, "Glass.html", locals())

def liver(request):
   if request.method == 'POST':
        TB = request.POST['TB']
        DB = request.POST['DB']
        AD = request.POST['AP']
        SG = request.POST['Sgpt']
        S = request.POST['Sgot']
        TP = request.POST['TP']
        AL = request.POST['AL']
        AG = request.POST['AG']
        list10=[]
        newlist=[]
        list10.append(TB)
        list10.append(DB)
        list10.append(AD)
        list10.append(SG)
        list10.append(S)
        list10.append(TP)
        list10.append(AL)
        list10.append(AG)
        newlist.append(list10)
        bcd=checkliver(newlist)
        print(bcd)
        liver_disease = []
        if bcd[0] == 1:
            liver_disease.append('Disease_not_Present')
        elif bcd[0] == 2:
            liver_disease.append('Liver_Disease_Present')


   return render(request, "liver.html", locals())

def Iris(request):
    msg = ''
    if request.method == 'POST':
        SepalL= request.POST['Sepal_L']
        SepalW = request.POST['Sepal_W']
        PetalL = request.POST['Petal_L']
        PetalW = request.POST['Petal_W']
        msg = 'Successfully Enter the data ! Please wait Now for resluts'
        listi = []
        testi = []
        listi.append(SepalL)
        listi.append(SepalW)
        listi.append(PetalL)
        listi.append(PetalW)
        testi.append(listi)
        efg = Firis(testi)
        print(efg)

    return render(request, "iris.html", locals())

def house(request):
    if request.method == 'POST':
        age= request.POST['X2 house age']
        market = request.POST['X3 distance to the nearest MRT station']
        Store = request.POST["X4 number of convenience store"]
        l = request.POST['X5 latitude']
        lo = request.POST['X6 longitude']
        msg = 'Successfully Enter the data ! Please wait Now for resluts'
        listh = []
        testh = []
        listh.append(age)
        listh.append(market)
        listh.append(Store)
        listh.append(l)
        listh.append(lo)
        testh.append(listh)
        jkl=reales(testh)
        print(jkl)

    return render(request, "estate.html", locals())

def Bscale(request):
    if request.method == 'POST':
        LW= request.POST['Left-Weight']
        LD = request.POST['Left-Distance']
        RW = request.POST["Right-Weight"]
        RD = request.POST['Right-Distance']
        blist=[]
        btest=[]
        blist.append(LW)
        blist.append(LD)
        blist.append(RW)
        blist.append(RD)
        btest.append(blist)
        bresult=bal(btest)
        print(bresult)

    return render(request, "balance.html", locals())

def cancer(request):
    msg = ''
    if request.method == 'POST':
        clump_thickness = request.POST['clump_thickness']
        uniform_cell_size = request.POST['uniform_cell_size']
        uniform_cell_shape = request.POST['uniform_cell_shape']
        marginal_adhesion = request.POST['marginal_adhesion']
        bare_nuclei = request.POST['bare_nuclei']
        bland_chromation = request.POST['bland_chromation']
        normal_nucleoli = request.POST['normal_nucleoli']
        mitoses = request.POST['mitoses']
        msg = "Successfully Enter the data ! Please wait Now for results"
        List = []
        test = []
        List.append(clump_thickness)
        List.append(uniform_cell_size)
        List.append(uniform_cell_shape)
        List.append(marginal_adhesion)
        List.append(bare_nuclei)
        List.append(bland_chromation)
        List.append(normal_nucleoli)
        List.append(mitoses)
        test.append(List)
        abc = TestSplitcancer(test)
        print( abc)

    return render(request, 'cancer.html', locals())

def Bdonate(request):
    if request.method == 'POST':
        R= request.POST['Recency']
        F = request.POST['Frequency']
        M = request.POST['Monetary']
        T = request.POST['Time']
        bllist=[]
        bltest=[]
        bllist.append(R)
        bllist.append(F)
        bllist.append(M)
        bllist.append(T)
        bltest.append(bllist)
        blresult=Fblood(bltest)
        print(blresult)

    return render(request, "blood.html", locals())

def mood(request):
    if request.method == 'POST':
        H1= request.POST['X1']
        H2 = request.POST['X2']
        H3= request.POST['X3']
        H4= request.POST['X4']
        H5 = request.POST['X5']
        H6 = request.POST['X6']
        Hlist=[]
        Htest=[]
        Hlist.append(H1)
        Hlist.append(H2)
        Hlist.append(H3)
        Hlist.append(H4)
        Hlist.append(H5)
        Hlist.append(H6)
        Htest.append(Hlist)
        Hresult=happy(Htest)
        print(Hresult)

    return render(request, "happy.html", locals())

def Poker(request):
    if request.method == 'POST':
        S1= request.POST['S1']
        S2 = request.POST['C1']
        S3= request.POST['S2']
        S4= request.POST['C2']
        S5 = request.POST['S3']
        S6 = request.POST['C3']
        S7 = request.POST['S4']
        S8 = request.POST['C4']
        S9 = request.POST['S5']
        S10 = request.POST['C5']
        Plist=[]
        Ptest=[]
        Plist.append(S1)
        Plist.append(S2)
        Plist.append(S3)
        Plist.append(S4)
        Plist.append(S5)
        Plist.append(S6)
        Plist.append(S2)
        Plist.append(S3)
        Plist.append(S4)
        Plist.append(S5)
        Plist.append(S6)
        Ptest.append(Plist)
        Poutput=Fpoker(Ptest)
        print(Poutput)

    return render(request, "poker.html", locals())

def haber(request):
    if request.method == 'POST':
        A= request.POST['age']
        OP = request.POST['op']
        POS = request.POST["pos"]
        blist=[]
        stest=[]
        blist.append(A)
        blist.append(OP)
        blist.append(POS)
        stest.append(blist)
        sresult=Fhaber(stest)
        print(sresult)

    return render(request, "survival.html", locals())

def teach(request):
    if request.method == 'POST':
        C= request.POST["Courseinstructor"]
        co = request.POST["Course"]
        SE = request.POST["Summer_or_regular_semester"]
        CS = request.POST["Class_size"]
        List = []
        test = []
        List.append(C)
        List.append(co)
        List.append(SE)
        List.append(CS)
        test.append(List)
        abcd = TestSplitteach(test)
        print("abc", abcd)

    return render(request, 'teach.html', locals())

def creditcard(request):
    msg = ''
    if request.method == 'POST':
        PAY = request.POST['payy0']
        PA2= request.POST['PAY_2']
        PA3 = request.POST['PAY_3']
        PA4= request.POST['PAY_4']
        PA5 = request.POST['PAY_5']
        PA6 = request.POST['PAY_6']
        BI = request.POST['BILL_AMT1']
        BILL_AMT2 = request.POST['BILL_AMT2']
        BILL_AMT3 = request.POST['BILL_AMT3']
        BILL_AMT4 = request.POST['BILL_AMT4']
        BILL_AMT5 = request.POST['BILL_AMT5']
        BILL_AMT6 = request.POST['BILL_AMT6']
        PAY_AMT1 = request.POST['PAY_AMT1']
        PAY_AMT2 = request.POST['PAY_AMT2']
        PAY_AMT3 = request.POST['PAY_AMT3']
        PAY_AMT4 = request.POST['PAY_AMT4']
        PAY_AMT5 = request.POST['PAY_AMT5']
        PAY_AMT6 = request.POST['PAY_AMT6']
        msg = "Successfully Enter the data ! Please wait Now for results"
        List = []
        test = []
        List.append(PAY)
        List.append(PA2)
        List.append(PA3)
        List.append(PA4)
        List.append(PA5)
        List.append(PA6)
        List.append(BI)
        List.append(BILL_AMT2)
        List.append(BILL_AMT3)
        List.append(BILL_AMT4)
        List.append(BILL_AMT5)
        List.append(BILL_AMT6)
        List.append(PAY_AMT1)
        List.append(PAY_AMT2)

        List.append(PAY_AMT3)
        List.append(PAY_AMT4)
        List.append(PAY_AMT5)
        List.append(PAY_AMT6)
        test.append(List)
        print("testttttttttttttttttttttttttttt",test)
        abc = TestSplitcredit(test)
        print("abc",abc)

    return render(request,'credict card.html',locals())


def wheat(request):
    msg = ''

    if request.method == 'POST':
        Area = request.POST['Area']
        Perimeter = request.POST['Perimeter']
        Compactness = request.POST['Compactness']
        Length_of_kernel = request.POST['Length_of_kernel']
        Width_of_kernel = request.POST['Width_of_kernel']
        Asymmetry_coefficient = request.POST['Asymmetry_coefficient']
        Length_of_kernel_groove = request.POST['Length_of_kernel_groove']
        msg = "Successfully Enter the data ! Please wait Now for results"
        List = []
        test = []
        List.append(Area)
        List.append(Perimeter)
        List.append(Compactness)
        List.append(Length_of_kernel)
        List.append(Width_of_kernel)
        List.append(Asymmetry_coefficient)
        List.append(Length_of_kernel_groove)
        print(List)
        test.append(List)
        abc = TestSplitseed(test)
        print("abc", abc)

    return render(request, 'wheat.html', locals())

def titanic(request):
    msg = ''
    if request.method == 'POST':
        PassengerId = request.POST['PassengerId']
        Pclass = request.POST['Pclass']
        Sex = request.POST['Sex']
        Age = request.POST['Age']
        SibSp = request.POST['SibSp']
        Parch = request.POST['Parch']
        Fare = request.POST['Fare']
        msg = "Successfully Enter the data ! Please wait Now for results"
        List = []
        test = []
        List.append(PassengerId)
        List.append(Pclass)
        List.append(Sex)
        List.append(Age)
        List.append(SibSp)
        List.append(Parch)
        List.append(Fare)
        test.append(List)
        abc = TestSplittitanic(test)
        print("abcccccc", abc)

    return render(request,'titanic.html',locals())



