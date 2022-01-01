import sys
sys.path.append('/Users/attreyeem/Desktop/projects/covidclickapp/env/lib/python3.7/site-packages/django/contrib')
from django.shortcuts import render,HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .models import Hospital
from django.conf import settings
from django.core.mail import send_mail





# Create your views here.
def index(request):
    return render(request,'index.html')

def bed(request):
	hosp1 = Hospital()
	hosp1.name = 'Asian Heart Institute'
	hosp1.number = 30
	hosp1.price = 10000
	hosp1.address = 'Mumbai'
	hosp1.rating = 4.5

	hosp2 = Hospital()
	hosp2.name = 'Bhabha Hospital'
	hosp2.number = 36
	hosp2.price = 9000
	hosp2.address = 'Mumbai'
	hosp2.rating = 4.2

	hosp3 = Hospital()
	hosp3.name = 'Bhaktivedanta Hospital'
	hosp3.number = 32
	hosp3.price = 10000
	hosp3.address = 'Mumbai'
	hosp3.rating = 4.3
	hosp4 = Hospital()
	hosp4.name = 'Bombay Hospital'
	hosp4.number = 23
	hosp4.price = 9500
	hosp4.address = 'Mumbai'
	hosp4.rating = 4.3
	hosp5 = Hospital()
	hosp5.name = 'Breach Candy Hospital'
	hosp5.number = 38
	hosp5.price = 9600
	hosp5.address = 'Mumbai'
	hosp5.rating = 4.3
	hosp6 = Hospital()
	hosp6.name = 'D Y Patil Hospital'
	hosp6.number = 9
	hosp6.price = 10000
	hosp6.address = 'Mumbai'
	hosp6.rating = 4.3
	hosp7 = Hospital()
	hosp7.name = 'Cloudnine Hospitals'
	hosp7.number = 14
	hosp7.price = 8000
	hosp7.address = 'Mumbai'
	hosp7.rating = 4.3
	hosp8 = Hospital()
	hosp8.name = 'Cooper Hospital'
	hosp8.number = 23
	hosp8.price = 8900
	hosp8.address = 'Mumbai'
	hosp8.rating = 4.3
	hosp9 = Hospital()
	hosp9.name = 'Gokuldas Tejpal Hospital'
	hosp9.number = 25
	hosp9.price = 9200
	hosp9.address = 'Mumbai'
	hosp9.rating = 4.3
	hosp10 = Hospital()
	hosp10.name = 'Hinduja Hospital'
	hosp10.number = 31
	hosp10.price = 9300
	hosp10.address = 'Mumbai'
	hosp10.rating = 4.3
	hosp11 = Hospital()
	hosp11.name = 'All India Institute of Medical Sciences'
	hosp11.number = 31
	hosp11.price = 9600
	hosp11.address = 'Delhi'
	hosp11.rating = 4.3
	hosp12 = Hospital()
	hosp12.name = 'Columbia Asia,'
	hosp12.number = 3
	hosp12.price = 1000
	hosp12.address = 'Delhi'
	hosp12.rating = 4.3
	hosp13 = Hospital()
	hosp13.name = 'Eden Hospital'
	hosp13.number = 3
	hosp13.price = 1000
	hosp13.address = 'Delhi'
	hosp13.rating = 4.3
	hosp14 = Hospital()
	hosp14.name = 'Fortis Hospital'
	hosp14.number = 3
	hosp14.price = 1000
	hosp14.address = 'Delhi'
	hosp14.rating = 4.
	hosp15 = Hospital()
	hosp15.name = 'National Heart Institute'
	hosp15.number = 3
	hosp15.price = 1000
	hosp15.address = 'Delhi'
	hosp15.rating = 4.3
	hosp16 = Hospital()
	hosp16.name = 'Safdarjang Hospital'
	hosp16.number = 3
	hosp16.price = 1000
	hosp16.address = 'Delhi'
	hosp16.rating = 4.3
	hosp17 = Hospital()
	hosp17.name = 'Sanjeevan Hospitals'
	hosp17.number = 3
	hosp17.price = 1000
	hosp17.address = 'Delhi'
	hosp17.rating = 4.3
	hosp18 = Hospital()
	hosp18.name = 'Sunrise Hospital'
	hosp18.number = 3
	hosp18.price = 1000
	hosp18.address = 'Delhi'
	hosp18.rating = 4.3
	hosp19 = Hospital()
	hosp19.name = 'Indraprastha Apollo Hospital'
	hosp19.number = 3
	hosp19.price = 1000
	hosp19.address = 'Delhi'
	hosp19.rating = 4.3
	hosp20 = Hospital()
	hosp20.name = 'Sir Ganga Ram Hospital'
	hosp20.number = 3
	hosp20.price = 1000
	hosp20.address = 'Delhi'
	hosp20.rating = 4.3
	hosp21 = Hospital()
	hosp21.name = 'Somaiya'
	hosp21.number = 3
	hosp21.price = 1000
	hosp21.address = 'Mumbai'
	hosp21.rating = 4.3
	hosp25 = Hospital()
	hosp25.name = 'Somaiya'
	hosp25.number = 3
	hosp25.price = 1000
	hosp25.address = 'Mumbai'
	hosp25.rating = 4.3
	hosp22 = Hospital()
	hosp22.name = 'Somaiya'
	hosp22.number = 3
	hosp22.price = 1000
	hosp22.address = 'Mumbai'
	hosp22.rating = 4.3
	hosp26 = Hospital()
	hosp26.name = 'Somaiya'
	hosp26.number = 3
	hosp26.price = 1000
	hosp26.address = 'Mumbai'
	hosp26.rating = 4.3
	hosp23 = Hospital()
	hosp23.name = 'Somaiya'
	hosp23.number = 3
	hosp23.price = 1000
	hosp23.address = 'Mumbai'
	hosp23.rating = 4.3
	hosp24 = Hospital()
	hosp24.name = 'Somaiya'
	hosp24.number = 3
	hosp24.price = 1000
	hosp24.address = 'Mumbai'
	hosp24.rating = 4.3
	hosp25 = Hospital()
	hosp25.name = 'Somaiya'
	hosp25.number = 3
	hosp25.price = 1000
	hosp25.address = 'Mumbai'
	hosp25.rating = 4.3
	hosp26 = Hospital()
	hosp26.name = 'Somaiya'
	hosp26.number = 3
	hosp26.price = 1000
	hosp26.address = 'Mumbai'
	hosp26.rating = 4.3
	hosp27 = Hospital()
	hosp27.name = 'Somaiya'
	hosp27.number = 3
	hosp27.price = 1000
	hosp27.address = 'Mumbai'
	hosp27.rating = 4.3
	hosp28 = Hospital()
	hosp28.name = 'Somaiya'
	hosp28.number = 3
	hosp28.price = 1000
	hosp28.address = 'Mumbai'
	hosp28.rating = 4.3
	hosp29 = Hospital()
	hosp29.name = 'Somaiya'
	hosp29.number = 3
	hosp29.price = 1000
	hosp29.address = 'Mumbai'
	hosp29.rating = 4.3
	hosp30 = Hospital()
	hosp30.name = 'Somaiya'
	hosp30.number = 3
	hosp30.price = 1000
	hosp30.address = 'Mumbai'
	hosp30.rating = 4.3
	hosp31 = Hospital()
	hosp31.name = 'Somaiya'
	hosp31.number = 3
	hosp31.price = 1000
	hosp31.address = 'Mumbai'
	hosp31.rating = 4.3
	hosp32 = Hospital()
	hosp32.name = 'Somaiya'
	hosp32.number = 3
	hosp32.price = 1000
	hosp32.address = 'Mumbai'
	hosp32.rating = 4.3
	hosp33 = Hospital()
	hosp33.name = 'Somaiya'
	hosp33.number = 3
	hosp33.price = 1000
	hosp33.address = 'Mumbai'
	hosp33.rating = 4.3
	hosp34 = Hospital()
	hosp34.name = 'Somaiya'
	hosp34.number = 3
	hosp34.price = 1000
	hosp34.address = 'Mumbai'
	hosp34.rating = 4.3
	hosp35 = Hospital()
	hosp35.name = 'Somaiya'
	hosp35.number = 3
	hosp35.price = 1000
	hosp35.address = 'Mumbai'
	hosp35.rating = 4.3
	hosp36 = Hospital()
	hosp36.name = 'Somaiya'
	hosp36.number = 3
	hosp36.price = 1000
	hosp36.address = 'Mumbai'
	hosp36.rating = 4.3
	hosp37 = Hospital()
	hosp37.name = 'Somaiya'
	hosp37.number = 3
	hosp37.price = 1000
	hosp37.address = 'Mumbai'
	hosp37.rating = 4.3
	hosp38 = Hospital()
	hosp38.name = 'Somaiya'
	hosp38.number = 3
	hosp38.price = 1000
	hosp38.address = 'Mumbai'
	hosp38.rating = 4.3
	hosp38 = Hospital()
	hosp38.name = 'Somaiya'
	hosp38.number = 3
	hosp38.price = 1000
	hosp38.address = 'Mumbai'
	hosp38.rating = 4.3
	hosp39 = Hospital()
	hosp39.name = 'Somaiya'
	hosp39.number = 3
	hosp39.price = 1000
	hosp39.address = 'Mumbai'
	hosp39.rating = 4.3
	hosp40 = Hospital()
	hosp40.name = 'Somaiya'
	hosp40.number = 3
	hosp40.price = 1000
	hosp40.address = 'Mumbai'
	hosp40.rating = 4.3
	hosp41 = Hospital()
	hosp41.name = 'Somaiya'
	hosp41.number = 3
	hosp41.price = 1000
	hosp41.address = 'Mumbai'
	hosp41.rating = 4.3
	hosp42 = Hospital()
	hosp42.name = 'Somaiya'
	hosp42.number = 3
	hosp42.price = 1000
	hosp42.address = 'Mumbai'
	hosp42.rating = 4.3
	hosp43 = Hospital()
	hosp43.name = 'Somaiya'
	hosp43.number = 3
	hosp43.price = 1000
	hosp43.address = 'Mumbai'
	hosp43.rating = 4.3
	hosp44 = Hospital()
	hosp44.name = 'Somaiya'
	hosp44.number = 3
	hosp44.price = 1000
	hosp44.address = 'Mumbai'
	hosp44.rating = 4.3
	hosp45 = Hospital()
	hosp45.name = 'Somaiya'
	hosp45.number = 3
	hosp45.price = 1000
	hosp45.address = 'Mumbai'
	hosp45.rating = 4.3
	hosp46 = Hospital()
	hosp46.name = 'Somaiya'
	hosp46.number = 3
	hosp46.price = 1000
	hosp46.address = 'Mumbai'
	hosp46.rating = 4.3
	hosp47 = Hospital()
	hosp47.name = 'Somaiya'
	hosp47.number = 3
	hosp47.price = 1000
	hosp47.address = 'Mumbai'
	hosp47.rating = 4.3
	hosp48 = Hospital()
	hosp48.name = 'Somaiya'
	hosp48.number = 3
	hosp48.price = 1000
	hosp48.address = 'Mumbai'
	hosp48.rating = 4.3
	hosp49 = Hospital()
	hosp49.name = 'Somaiya'
	hosp49.number = 3
	hosp49.price = 1000
	hosp49.address = 'Mumbai'
	hosp49.rating = 4.3
	hosp50 = Hospital()
	hosp50.name = 'Somaiya'
	hosp50.number = 3
	hosp50.price = 1000
	hosp50.address = 'Mumbai'
	hosp50.rating = 4.3
	hosp51 = Hospital()
	hosp51.name = 'Somaiya'
	hosp51.number = 3
	hosp51.price = 1000
	hosp51.address = 'Mumbai'
	hosp51.rating = 4.3
	hosp52 = Hospital()
	hosp52.name = 'Somaiya'
	hosp52.number = 3
	hosp52.price = 1000
	hosp52.address = 'Mumbai'
	hosp52.rating = 4.3
	hosp52 = Hospital()
	hosp52.name = 'Somaiya'
	hosp52.number = 3
	hosp52.price = 1000
	hosp52.address = 'Mumbai'
	hosp52.rating = 4.3
	hosp53 = Hospital()
	hosp53.name = 'Somaiya'
	hosp53.number = 3
	hosp53.price = 1000
	hosp53.address = 'Mumbai'
	hosp53.rating = 4.3
	hosp54 = Hospital()
	hosp54.name = 'Somaiya'
	hosp54.number = 3
	hosp54.price = 1000
	hosp54.address = 'Mumbai'
	hosp54.rating = 4.3
	hosp55 = Hospital()
	hosp55.name = 'Somaiya'
	hosp55.number = 3
	hosp55.price = 1000
	hosp55.address = 'Mumbai'
	hosp55.rating = 4.3
	hosp56 = Hospital()
	hosp56.name = 'Somaiya'
	hosp56.number = 3
	hosp56.price = 1000
	hosp56.address = 'Mumbai'
	hosp56.rating = 4.3
	hosp57 = Hospital()
	hosp57.name = 'Somaiya'
	hosp57.number = 3
	hosp57.price = 1000
	hosp57.address = 'Mumbai'
	hosp57.rating = 4.3
	hosp58 = Hospital()
	hosp58.name = 'Somaiya'
	hosp58.number = 3
	hosp58.price = 1000
	hosp58.address = 'Mumbai'
	hosp58.rating = 4.3
	hosp59 = Hospital()
	hosp59.name = 'Somaiya'
	hosp59.number = 3
	hosp59.price = 1000
	hosp59.address = 'Mumbai'
	hosp59.rating = 4.3
	hosp60 = Hospital()
	hosp60.name = 'Somaiya'
	hosp60.number = 3
	hosp60.price = 1000
	hosp60.address = 'Mumbai'
	hosp60.rating = 4.3
	hosp61 = Hospital()
	hosp61.name = 'Somaiya'
	hosp61.number = 3
	hosp61.price = 1000
	hosp61.address = 'Mumbai'
	hosp61.rating = 4.3
	hosp62 = Hospital()
	hosp62.name = 'Somaiya'
	hosp62.number = 3
	hosp62.price = 1000
	hosp62.address = 'Mumbai'
	hosp62.rating = 4.3
	hosp63 = Hospital()
	hosp63.name = 'Somaiya'
	hosp63.number = 3
	hosp63.price = 1000
	hosp63.address = 'Mumbai'
	hosp63.rating = 4.3
	hosp64 = Hospital()
	hosp64.name = 'Somaiya'
	hosp64.number = 3
	hosp64.price = 1000
	hosp64.address = 'Mumbai'
	hosp64.rating = 4.3
	hosp65 = Hospital()
	hosp65.name = 'Somaiya'
	hosp65.number = 3
	hosp65.price = 1000
	hosp65.address = 'Mumbai'
	hosp65.rating = 4.3
	hosp66 = Hospital()
	hosp66.name = 'Somaiya'
	hosp66.number = 3
	hosp66.price = 1000
	hosp66.address = 'Mumbai'
	hosp66.rating = 4.3
	hosp67 = Hospital()
	hosp67.name = 'Somaiya'
	hosp67.number = 3
	hosp67.price = 1000
	hosp67.address = 'Mumbai'
	hosp67.rating = 4.3
	hosp68 = Hospital()
	hosp68.name = 'Somaiya'
	hosp68.number = 3
	hosp68.price = 1000
	hosp68.address = 'Mumbai'
	hosp68.rating = 4.3
	hosp69 = Hospital()
	hosp69.name = 'Somaiya'
	hosp69.number = 3
	hosp69.price = 1000
	hosp69.address = 'Mumbai'
	hosp69.rating = 4.3
	hosp70 = Hospital()
	hosp70.name = 'Somaiya'
	hosp70.number = 3
	hosp70.price = 1000
	hosp70.address = 'Mumbai'
	hosp70.rating = 4.3
	hosp71 = Hospital()
	hosp71.name = 'Somaiya'
	hosp71.number = 3
	hosp71.price = 1000
	hosp71.address = 'Mumbai'
	hosp71.rating = 4.3
	hosp72 = Hospital()
	hosp72.name = 'Somaiya'
	hosp72.number = 3
	hosp72.price = 1000
	hosp72.address = 'Mumbai'
	hosp72.rating = 4.3
	hosp73 = Hospital()
	hosp73.name = 'Somaiya'
	hosp73.number = 3
	hosp73.price = 1000
	hosp73.address = 'Mumbai'
	hosp73.rating = 4.3
	hosp74 = Hospital()
	hosp74.name = 'Somaiya'
	hosp74.number = 3
	hosp74.price = 1000
	hosp74.address = 'Mumbai'
	hosp74.rating = 4.3
	hosp75 = Hospital()
	hosp75.name = 'Somaiya'
	hosp75.number = 3
	hosp75.price = 1000
	hosp75.address = 'Mumbai'
	hosp75.rating = 4.3
	hosp76 = Hospital()
	hosp76.name = 'Somaiya'
	hosp76.number = 3
	hosp76.price = 1000
	hosp76.address = 'Mumbai'
	hosp76.rating = 4.3
	hosp77 = Hospital()
	hosp77.name = 'Somaiya'
	hosp77.number = 3
	hosp77.price = 1000
	hosp77.address = 'Mumbai'
	hosp77.rating = 4.3
	hosp78 = Hospital()
	hosp78.name = 'Somaiya'
	hosp78.number = 3
	hosp78.price = 1000
	hosp78.address = 'Mumbai'
	hosp78.rating = 4.3
	hosp79 = Hospital()
	hosp79.name = 'Somaiya'
	hosp79.number = 3
	hosp79.price = 1000
	hosp79.address = 'Mumbai'
	hosp79.rating = 4.3
	hosp80 = Hospital()
	hosp80.name = 'Somaiya'
	hosp80.number = 3
	hosp80.price = 1000
	hosp80.address = 'Mumbai'
	hosp80.rating = 4.3
	hosp81 = Hospital()
	hosp81.name = 'Somaiya'
	hosp81.number = 3
	hosp81.price = 1000
	hosp81.address = 'Mumbai'
	hosp81.rating = 4.3
	hosp82 = Hospital()
	hosp82.name = 'Somaiya'
	hosp82.number = 3
	hosp82.price = 1000
	hosp82.address = 'Mumbai'
	hosp82.rating = 4.3
	hosp83 = Hospital()
	hosp83.name = 'Somaiya'
	hosp83.number = 3
	hosp83.price = 1000
	hosp83.address = 'Mumbai'
	hosp83.rating = 4.3
	hosp83 = Hospital()
	hosp83.name = 'Somaiya'
	hosp83.number = 3
	hosp83.price = 1000
	hosp83.address = 'Mumbai'
	hosp83.rating = 4.3
	hosp84 = Hospital()
	hosp84.name = 'Somaiya'
	hosp84.number = 3
	hosp84.price = 1000
	hosp84.address = 'Mumbai'
	hosp84.rating = 4.3
	hosp85 = Hospital()
	hosp85.name = 'Somaiya'
	hosp85.number = 3
	hosp85.price = 1000
	hosp85.address = 'Mumbai'
	hosp85.rating = 4.3
	hosp86 = Hospital()
	hosp86.name = 'Somaiya'
	hosp86.number = 3
	hosp86.price = 1000
	hosp86.address = 'Mumbai'
	hosp86.rating = 4.3
	hosp87 = Hospital()
	hosp87.name = 'Somaiya'
	hosp87.number = 3
	hosp87.price = 1000
	hosp87.address = 'Mumbai'
	hosp87.rating = 4.3
	hosp88 = Hospital()
	hosp88.name = 'Somaiya'
	hosp88.number = 3
	hosp88.price = 1000
	hosp88.address = 'Mumbai'
	hosp88.rating = 4.3
	hosp89 = Hospital()
	hosp89.name = 'Somaiya'
	hosp89.number = 3
	hosp89.price = 1000
	hosp89.address = 'Mumbai'
	hosp89.rating = 4.3
	hosp90 = Hospital()
	hosp90.name = 'Somaiya'
	hosp90.number = 3
	hosp90.price = 1000
	hosp90.address = 'Mumbai'
	hosp90.rating = 4.3
	hosp91 = Hospital()
	hosp91.name = 'Somaiya'
	hosp91.number = 3
	hosp91.price = 1000
	hosp91.address = 'Mumbai'
	hosp91.rating = 4.3
	hosp92 = Hospital()
	hosp92.name = 'Somaiya'
	hosp92.number = 3
	hosp92.price = 1000
	hosp92.address = 'Mumbai'
	hosp92.rating = 4.3
	hosp93 = Hospital()
	hosp93.name = 'Somaiya'
	hosp93.number = 3
	hosp93.price = 1000
	hosp93.address = 'Mumbai'
	hosp93.rating = 4.3
	hosp94 = Hospital()
	hosp94.name = 'Somaiya'
	hosp94.number = 3
	hosp94.price = 1000
	hosp94.address = 'Mumbai'
	hosp94.rating = 4.3
	hosp95 = Hospital()
	hosp95.name = 'Somaiya'
	hosp95.number = 3
	hosp95.price = 1000
	hosp95.address = 'Mumbai'
	hosp95.rating = 4.3
	hosp96 = Hospital()
	hosp96.name = 'Somaiya'
	hosp96.number = 3
	hosp96.price = 1000
	hosp96.address = 'Mumbai'
	hosp96.rating = 4.3
	hosp97 = Hospital()
	hosp97.name = 'Somaiya'
	hosp97.number = 3
	hosp97.price = 1000
	hosp97.address = 'Mumbai'
	hosp97.rating = 4.3
	hosp98 = Hospital()
	hosp98.name = 'Somaiya'
	hosp98.number = 3
	hosp98.price = 1000
	hosp98.address = 'Mumbai'
	hosp98.rating = 4.3
	hosp99 = Hospital()
	hosp99.name = 'Somaiya'
	hosp99.number = 3
	hosp99.price = 1000
	hosp99.address = 'Mumbai'
	hosp99.rating = 4.3
	hosp100 = Hospital()
	hosp100.name = 'Somaiya'
	hosp100.number = 3
	hosp100.price = 1000
	hosp100.address = 'Mumbai'
	hosp100.rating = 4.3

	hospitals = [hosp1,hosp2,hosp3,hosp4,hosp5,hosp6,hosp7,hosp8,hosp9,hosp10,hosp11,hosp12,hosp13,hosp14,hosp15,hosp16,hosp17,hosp18,hosp19,hosp20,hosp21,hosp22,hosp23,hosp24,hosp25,hosp26,hosp27,hosp28,hosp29,hosp30,hosp31,hosp32,hosp33,hosp34,hosp35,hosp36,hosp37,hosp38,hosp39,hosp40,hosp41,hosp42,hosp43,hosp44,hosp45,hosp46,hosp47,hosp48,hosp49,hosp50,hosp51,hosp52,hosp53,hosp54,hosp55,hosp56,hosp57,hosp58,hosp59,hosp60,hosp61,hosp62,hosp63,hosp64,hosp65,hosp66,hosp67,hosp68,hosp69,hosp70,hosp71,hosp72,hosp73,hosp74,hosp75,hosp76,hosp77,hosp78,hosp79,hosp80,hosp81,hosp82,hosp83,hosp84,hosp85,hosp86,hosp87,hosp88,hosp89,hosp90,hosp91,hosp92,hosp93,hosp94,hosp95,hosp96,hosp97,hosp98,hosp99,hosp100]
	

	cityList = set([hosp1.address,hosp2.address,hosp3.address])

	return render(request,'beds.html',{'hospitals' : hospitals , 'city' : cityList})

def oxygen(request):
	hosp1 = Hospital()
	hosp1.name = 'Asian Heart Institute'
	hosp1.number = 30
	hosp1.price = 10000
	hosp1.address = 'Mumbai'
	hosp1.rating = 4.5

	hosp2 = Hospital()
	hosp2.name = 'Bhabha Hospital'
	hosp2.number = 36
	hosp2.price = 9000
	hosp2.address = 'Mumbai'
	hosp2.rating = 4.2

	hosp3 = Hospital()
	hosp3.name = 'Bhaktivedanta Hospital'
	hosp3.number = 32
	hosp3.price = 10000
	hosp3.address = 'Mumbai'
	hosp3.rating = 4.3
	hosp4 = Hospital()
	hosp4.name = 'Bombay Hospital'
	hosp4.number = 23
	hosp4.price = 9500
	hosp4.address = 'Mumbai'
	hosp4.rating = 4.3
	hosp5 = Hospital()
	hosp5.name = 'Breach Candy Hospital'
	hosp5.number = 38
	hosp5.price = 9600
	hosp5.address = 'Mumbai'
	hosp5.rating = 4.3
	hosp6 = Hospital()
	hosp6.name = 'D Y Patil Hospital'
	hosp6.number = 9
	hosp6.price = 10000
	hosp6.address = 'Mumbai'
	hosp6.rating = 4.3
	hosp7 = Hospital()
	hosp7.name = 'Cloudnine Hospitals'
	hosp7.number = 14
	hosp7.price = 8000
	hosp7.address = 'Mumbai'
	hosp7.rating = 4.3
	hosp8 = Hospital()
	hosp8.name = 'Cooper Hospital'
	hosp8.number = 23
	hosp8.price = 8900
	hosp8.address = 'Mumbai'
	hosp8.rating = 4.3
	hosp9 = Hospital()
	hosp9.name = 'Gokuldas Tejpal Hospital'
	hosp9.number = 25
	hosp9.price = 9200
	hosp9.address = 'Mumbai'
	hosp9.rating = 4.3
	hosp10 = Hospital()
	hosp10.name = 'Hinduja Hospital'
	hosp10.number = 31
	hosp10.price = 9300
	hosp10.address = 'Mumbai'
	hosp10.rating = 4.3
	hosp11 = Hospital()
	hosp11.name = 'All India Institute of Medical Sciences'
	hosp11.number = 31
	hosp11.price = 9600
	hosp11.address = 'Delhi'
	hosp11.rating = 4.3
	hosp12 = Hospital()
	hosp12.name = 'Columbia Asia,'
	hosp12.number = 3
	hosp12.price = 1000
	hosp12.address = 'Delhi'
	hosp12.rating = 4.3
	hosp13 = Hospital()
	hosp13.name = 'Eden Hospital'
	hosp13.number = 3
	hosp13.price = 1000
	hosp13.address = 'Delhi'
	hosp13.rating = 4.3
	hosp14 = Hospital()
	hosp14.name = 'Fortis Hospital'
	hosp14.number = 3
	hosp14.price = 1000
	hosp14.address = 'Delhi'
	hosp14.rating = 4.
	hosp15 = Hospital()
	hosp15.name = 'National Heart Institute'
	hosp15.number = 3
	hosp15.price = 1000
	hosp15.address = 'Delhi'
	hosp15.rating = 4.3
	hosp16 = Hospital()
	hosp16.name = 'Safdarjang Hospital'
	hosp16.number = 3
	hosp16.price = 1000
	hosp16.address = 'Delhi'
	hosp16.rating = 4.3
	hosp17 = Hospital()
	hosp17.name = 'Sanjeevan Hospitals'
	hosp17.number = 3
	hosp17.price = 1000
	hosp17.address = 'Delhi'
	hosp17.rating = 4.3
	hosp18 = Hospital()
	hosp18.name = 'Sunrise Hospital'
	hosp18.number = 3
	hosp18.price = 1000
	hosp18.address = 'Delhi'
	hosp18.rating = 4.3
	hosp19 = Hospital()
	hosp19.name = 'Indraprastha Apollo Hospital'
	hosp19.number = 3
	hosp19.price = 1000
	hosp19.address = 'Delhi'
	hosp19.rating = 4.3
	hosp20 = Hospital()
	hosp20.name = 'Sir Ganga Ram Hospital'
	hosp20.number = 3
	hosp20.price = 1000
	hosp20.address = 'Delhi'
	hosp20.rating = 4.3
	hosp21 = Hospital()
	hosp21.name = 'Somaiya'
	hosp21.number = 3
	hosp21.price = 1000
	hosp21.address = 'Mumbai'
	hosp21.rating = 4.3
	hosp25 = Hospital()
	hosp25.name = 'Somaiya'
	hosp25.number = 3
	hosp25.price = 1000
	hosp25.address = 'Mumbai'
	hosp25.rating = 4.3
	hosp22 = Hospital()
	hosp22.name = 'Somaiya'
	hosp22.number = 3
	hosp22.price = 1000
	hosp22.address = 'Mumbai'
	hosp22.rating = 4.3
	hosp26 = Hospital()
	hosp26.name = 'Somaiya'
	hosp26.number = 3
	hosp26.price = 1000
	hosp26.address = 'Mumbai'
	hosp26.rating = 4.3
	hosp23 = Hospital()
	hosp23.name = 'Somaiya'
	hosp23.number = 3
	hosp23.price = 1000
	hosp23.address = 'Mumbai'
	hosp23.rating = 4.3
	hosp24 = Hospital()
	hosp24.name = 'Somaiya'
	hosp24.number = 3
	hosp24.price = 1000
	hosp24.address = 'Mumbai'
	hosp24.rating = 4.3
	hosp25 = Hospital()
	hosp25.name = 'Somaiya'
	hosp25.number = 3
	hosp25.price = 1000
	hosp25.address = 'Mumbai'
	hosp25.rating = 4.3
	hosp26 = Hospital()
	hosp26.name = 'Somaiya'
	hosp26.number = 3
	hosp26.price = 1000
	hosp26.address = 'Mumbai'
	hosp26.rating = 4.3
	hosp27 = Hospital()
	hosp27.name = 'Somaiya'
	hosp27.number = 3
	hosp27.price = 1000
	hosp27.address = 'Mumbai'
	hosp27.rating = 4.3
	hosp28 = Hospital()
	hosp28.name = 'Somaiya'
	hosp28.number = 3
	hosp28.price = 1000
	hosp28.address = 'Mumbai'
	hosp28.rating = 4.3
	hosp29 = Hospital()
	hosp29.name = 'Somaiya'
	hosp29.number = 3
	hosp29.price = 1000
	hosp29.address = 'Mumbai'
	hosp29.rating = 4.3
	hosp30 = Hospital()
	hosp30.name = 'Somaiya'
	hosp30.number = 3
	hosp30.price = 1000
	hosp30.address = 'Mumbai'
	hosp30.rating = 4.3
	hosp31 = Hospital()
	hosp31.name = 'Somaiya'
	hosp31.number = 3
	hosp31.price = 1000
	hosp31.address = 'Mumbai'
	hosp31.rating = 4.3
	hosp32 = Hospital()
	hosp32.name = 'Somaiya'
	hosp32.number = 3
	hosp32.price = 1000
	hosp32.address = 'Mumbai'
	hosp32.rating = 4.3
	hosp33 = Hospital()
	hosp33.name = 'Somaiya'
	hosp33.number = 3
	hosp33.price = 1000
	hosp33.address = 'Mumbai'
	hosp33.rating = 4.3
	hosp34 = Hospital()
	hosp34.name = 'Somaiya'
	hosp34.number = 3
	hosp34.price = 1000
	hosp34.address = 'Mumbai'
	hosp34.rating = 4.3
	hosp35 = Hospital()
	hosp35.name = 'Somaiya'
	hosp35.number = 3
	hosp35.price = 1000
	hosp35.address = 'Mumbai'
	hosp35.rating = 4.3
	hosp36 = Hospital()
	hosp36.name = 'Somaiya'
	hosp36.number = 3
	hosp36.price = 1000
	hosp36.address = 'Mumbai'
	hosp36.rating = 4.3
	hosp37 = Hospital()
	hosp37.name = 'Somaiya'
	hosp37.number = 3
	hosp37.price = 1000
	hosp37.address = 'Mumbai'
	hosp37.rating = 4.3
	hosp38 = Hospital()
	hosp38.name = 'Somaiya'
	hosp38.number = 3
	hosp38.price = 1000
	hosp38.address = 'Mumbai'
	hosp38.rating = 4.3
	hosp38 = Hospital()
	hosp38.name = 'Somaiya'
	hosp38.number = 3
	hosp38.price = 1000
	hosp38.address = 'Mumbai'
	hosp38.rating = 4.3
	hosp39 = Hospital()
	hosp39.name = 'Somaiya'
	hosp39.number = 3
	hosp39.price = 1000
	hosp39.address = 'Mumbai'
	hosp39.rating = 4.3
	hosp40 = Hospital()
	hosp40.name = 'Somaiya'
	hosp40.number = 3
	hosp40.price = 1000
	hosp40.address = 'Mumbai'
	hosp40.rating = 4.3
	hosp41 = Hospital()
	hosp41.name = 'Somaiya'
	hosp41.number = 3
	hosp41.price = 1000
	hosp41.address = 'Mumbai'
	hosp41.rating = 4.3
	hosp42 = Hospital()
	hosp42.name = 'Somaiya'
	hosp42.number = 3
	hosp42.price = 1000
	hosp42.address = 'Mumbai'
	hosp42.rating = 4.3
	hosp43 = Hospital()
	hosp43.name = 'Somaiya'
	hosp43.number = 3
	hosp43.price = 1000
	hosp43.address = 'Mumbai'
	hosp43.rating = 4.3
	hosp44 = Hospital()
	hosp44.name = 'Somaiya'
	hosp44.number = 3
	hosp44.price = 1000
	hosp44.address = 'Mumbai'
	hosp44.rating = 4.3
	hosp45 = Hospital()
	hosp45.name = 'Somaiya'
	hosp45.number = 3
	hosp45.price = 1000
	hosp45.address = 'Mumbai'
	hosp45.rating = 4.3
	hosp46 = Hospital()
	hosp46.name = 'Somaiya'
	hosp46.number = 3
	hosp46.price = 1000
	hosp46.address = 'Mumbai'
	hosp46.rating = 4.3
	hosp47 = Hospital()
	hosp47.name = 'Somaiya'
	hosp47.number = 3
	hosp47.price = 1000
	hosp47.address = 'Mumbai'
	hosp47.rating = 4.3
	hosp48 = Hospital()
	hosp48.name = 'Somaiya'
	hosp48.number = 3
	hosp48.price = 1000
	hosp48.address = 'Mumbai'
	hosp48.rating = 4.3
	hosp49 = Hospital()
	hosp49.name = 'Somaiya'
	hosp49.number = 3
	hosp49.price = 1000
	hosp49.address = 'Mumbai'
	hosp49.rating = 4.3
	hosp50 = Hospital()
	hosp50.name = 'Somaiya'
	hosp50.number = 3
	hosp50.price = 1000
	hosp50.address = 'Mumbai'
	hosp50.rating = 4.3
	hosp51 = Hospital()
	hosp51.name = 'Somaiya'
	hosp51.number = 3
	hosp51.price = 1000
	hosp51.address = 'Mumbai'
	hosp51.rating = 4.3
	hosp52 = Hospital()
	hosp52.name = 'Somaiya'
	hosp52.number = 3
	hosp52.price = 1000
	hosp52.address = 'Mumbai'
	hosp52.rating = 4.3
	hosp52 = Hospital()
	hosp52.name = 'Somaiya'
	hosp52.number = 3
	hosp52.price = 1000
	hosp52.address = 'Mumbai'
	hosp52.rating = 4.3
	hosp53 = Hospital()
	hosp53.name = 'Somaiya'
	hosp53.number = 3
	hosp53.price = 1000
	hosp53.address = 'Mumbai'
	hosp53.rating = 4.3
	hosp54 = Hospital()
	hosp54.name = 'Somaiya'
	hosp54.number = 3
	hosp54.price = 1000
	hosp54.address = 'Mumbai'
	hosp54.rating = 4.3
	hosp55 = Hospital()
	hosp55.name = 'Somaiya'
	hosp55.number = 3
	hosp55.price = 1000
	hosp55.address = 'Mumbai'
	hosp55.rating = 4.3
	hosp56 = Hospital()
	hosp56.name = 'Somaiya'
	hosp56.number = 3
	hosp56.price = 1000
	hosp56.address = 'Mumbai'
	hosp56.rating = 4.3
	hosp57 = Hospital()
	hosp57.name = 'Somaiya'
	hosp57.number = 3
	hosp57.price = 1000
	hosp57.address = 'Mumbai'
	hosp57.rating = 4.3
	hosp58 = Hospital()
	hosp58.name = 'Somaiya'
	hosp58.number = 3
	hosp58.price = 1000
	hosp58.address = 'Mumbai'
	hosp58.rating = 4.3
	hosp59 = Hospital()
	hosp59.name = 'Somaiya'
	hosp59.number = 3
	hosp59.price = 1000
	hosp59.address = 'Mumbai'
	hosp59.rating = 4.3
	hosp60 = Hospital()
	hosp60.name = 'Somaiya'
	hosp60.number = 3
	hosp60.price = 1000
	hosp60.address = 'Mumbai'
	hosp60.rating = 4.3
	hosp61 = Hospital()
	hosp61.name = 'Somaiya'
	hosp61.number = 3
	hosp61.price = 1000
	hosp61.address = 'Mumbai'
	hosp61.rating = 4.3
	hosp62 = Hospital()
	hosp62.name = 'Somaiya'
	hosp62.number = 3
	hosp62.price = 1000
	hosp62.address = 'Mumbai'
	hosp62.rating = 4.3
	hosp63 = Hospital()
	hosp63.name = 'Somaiya'
	hosp63.number = 3
	hosp63.price = 1000
	hosp63.address = 'Mumbai'
	hosp63.rating = 4.3
	hosp64 = Hospital()
	hosp64.name = 'Somaiya'
	hosp64.number = 3
	hosp64.price = 1000
	hosp64.address = 'Mumbai'
	hosp64.rating = 4.3
	hosp65 = Hospital()
	hosp65.name = 'Somaiya'
	hosp65.number = 3
	hosp65.price = 1000
	hosp65.address = 'Mumbai'
	hosp65.rating = 4.3
	hosp66 = Hospital()
	hosp66.name = 'Somaiya'
	hosp66.number = 3
	hosp66.price = 1000
	hosp66.address = 'Mumbai'
	hosp66.rating = 4.3
	hosp67 = Hospital()
	hosp67.name = 'Somaiya'
	hosp67.number = 3
	hosp67.price = 1000
	hosp67.address = 'Mumbai'
	hosp67.rating = 4.3
	hosp68 = Hospital()
	hosp68.name = 'Somaiya'
	hosp68.number = 3
	hosp68.price = 1000
	hosp68.address = 'Mumbai'
	hosp68.rating = 4.3
	hosp69 = Hospital()
	hosp69.name = 'Somaiya'
	hosp69.number = 3
	hosp69.price = 1000
	hosp69.address = 'Mumbai'
	hosp69.rating = 4.3
	hosp70 = Hospital()
	hosp70.name = 'Somaiya'
	hosp70.number = 3
	hosp70.price = 1000
	hosp70.address = 'Mumbai'
	hosp70.rating = 4.3
	hosp71 = Hospital()
	hosp71.name = 'Somaiya'
	hosp71.number = 3
	hosp71.price = 1000
	hosp71.address = 'Mumbai'
	hosp71.rating = 4.3
	hosp72 = Hospital()
	hosp72.name = 'Somaiya'
	hosp72.number = 3
	hosp72.price = 1000
	hosp72.address = 'Mumbai'
	hosp72.rating = 4.3
	hosp73 = Hospital()
	hosp73.name = 'Somaiya'
	hosp73.number = 3
	hosp73.price = 1000
	hosp73.address = 'Mumbai'
	hosp73.rating = 4.3
	hosp74 = Hospital()
	hosp74.name = 'Somaiya'
	hosp74.number = 3
	hosp74.price = 1000
	hosp74.address = 'Mumbai'
	hosp74.rating = 4.3
	hosp75 = Hospital()
	hosp75.name = 'Somaiya'
	hosp75.number = 3
	hosp75.price = 1000
	hosp75.address = 'Mumbai'
	hosp75.rating = 4.3
	hosp76 = Hospital()
	hosp76.name = 'Somaiya'
	hosp76.number = 3
	hosp76.price = 1000
	hosp76.address = 'Mumbai'
	hosp76.rating = 4.3
	hosp77 = Hospital()
	hosp77.name = 'Somaiya'
	hosp77.number = 3
	hosp77.price = 1000
	hosp77.address = 'Mumbai'
	hosp77.rating = 4.3
	hosp78 = Hospital()
	hosp78.name = 'Somaiya'
	hosp78.number = 3
	hosp78.price = 1000
	hosp78.address = 'Mumbai'
	hosp78.rating = 4.3
	hosp79 = Hospital()
	hosp79.name = 'Somaiya'
	hosp79.number = 3
	hosp79.price = 1000
	hosp79.address = 'Mumbai'
	hosp79.rating = 4.3
	hosp80 = Hospital()
	hosp80.name = 'Somaiya'
	hosp80.number = 3
	hosp80.price = 1000
	hosp80.address = 'Mumbai'
	hosp80.rating = 4.3
	hosp81 = Hospital()
	hosp81.name = 'Somaiya'
	hosp81.number = 3
	hosp81.price = 1000
	hosp81.address = 'Mumbai'
	hosp81.rating = 4.3
	hosp82 = Hospital()
	hosp82.name = 'Somaiya'
	hosp82.number = 3
	hosp82.price = 1000
	hosp82.address = 'Mumbai'
	hosp82.rating = 4.3
	hosp83 = Hospital()
	hosp83.name = 'Somaiya'
	hosp83.number = 3
	hosp83.price = 1000
	hosp83.address = 'Mumbai'
	hosp83.rating = 4.3
	hosp83 = Hospital()
	hosp83.name = 'Somaiya'
	hosp83.number = 3
	hosp83.price = 1000
	hosp83.address = 'Mumbai'
	hosp83.rating = 4.3
	hosp84 = Hospital()
	hosp84.name = 'Somaiya'
	hosp84.number = 3
	hosp84.price = 1000
	hosp84.address = 'Mumbai'
	hosp84.rating = 4.3
	hosp85 = Hospital()
	hosp85.name = 'Somaiya'
	hosp85.number = 3
	hosp85.price = 1000
	hosp85.address = 'Mumbai'
	hosp85.rating = 4.3
	hosp86 = Hospital()
	hosp86.name = 'Somaiya'
	hosp86.number = 3
	hosp86.price = 1000
	hosp86.address = 'Mumbai'
	hosp86.rating = 4.3
	hosp87 = Hospital()
	hosp87.name = 'Somaiya'
	hosp87.number = 3
	hosp87.price = 1000
	hosp87.address = 'Mumbai'
	hosp87.rating = 4.3
	hosp88 = Hospital()
	hosp88.name = 'Somaiya'
	hosp88.number = 3
	hosp88.price = 1000
	hosp88.address = 'Mumbai'
	hosp88.rating = 4.3
	hosp89 = Hospital()
	hosp89.name = 'Somaiya'
	hosp89.number = 3
	hosp89.price = 1000
	hosp89.address = 'Mumbai'
	hosp89.rating = 4.3
	hosp90 = Hospital()
	hosp90.name = 'Somaiya'
	hosp90.number = 3
	hosp90.price = 1000
	hosp90.address = 'Mumbai'
	hosp90.rating = 4.3
	hosp91 = Hospital()
	hosp91.name = 'Somaiya'
	hosp91.number = 3
	hosp91.price = 1000
	hosp91.address = 'Mumbai'
	hosp91.rating = 4.3
	hosp92 = Hospital()
	hosp92.name = 'Somaiya'
	hosp92.number = 3
	hosp92.price = 1000
	hosp92.address = 'Mumbai'
	hosp92.rating = 4.3
	hosp93 = Hospital()
	hosp93.name = 'Somaiya'
	hosp93.number = 3
	hosp93.price = 1000
	hosp93.address = 'Mumbai'
	hosp93.rating = 4.3
	hosp94 = Hospital()
	hosp94.name = 'Somaiya'
	hosp94.number = 3
	hosp94.price = 1000
	hosp94.address = 'Mumbai'
	hosp94.rating = 4.3
	hosp95 = Hospital()
	hosp95.name = 'Somaiya'
	hosp95.number = 3
	hosp95.price = 1000
	hosp95.address = 'Mumbai'
	hosp95.rating = 4.3
	hosp96 = Hospital()
	hosp96.name = 'Somaiya'
	hosp96.number = 3
	hosp96.price = 1000
	hosp96.address = 'Mumbai'
	hosp96.rating = 4.3
	hosp97 = Hospital()
	hosp97.name = 'Somaiya'
	hosp97.number = 3
	hosp97.price = 1000
	hosp97.address = 'Mumbai'
	hosp97.rating = 4.3
	hosp98 = Hospital()
	hosp98.name = 'Somaiya'
	hosp98.number = 3
	hosp98.price = 1000
	hosp98.address = 'Mumbai'
	hosp98.rating = 4.3
	hosp99 = Hospital()
	hosp99.name = 'Somaiya'
	hosp99.number = 3
	hosp99.price = 1000
	hosp99.address = 'Mumbai'
	hosp99.rating = 4.3
	hosp100 = Hospital()
	hosp100.name = 'Somaiya'
	hosp100.number = 3
	hosp100.price = 1000
	hosp100.address = 'Mumbai'
	hosp100.rating = 4.3

	hospitals = [hosp1,hosp2,hosp3,hosp4,hosp5,hosp6,hosp7,hosp8,hosp9,hosp10,hosp11,hosp12,hosp13,hosp14,hosp15,hosp16,hosp17,hosp18,hosp19,hosp20,hosp21,hosp22,hosp23,hosp24,hosp25,hosp26,hosp27,hosp28,hosp29,hosp30,hosp31,hosp32,hosp33,hosp34,hosp35,hosp36,hosp37,hosp38,hosp39,hosp40,hosp41,hosp42,hosp43,hosp44,hosp45,hosp46,hosp47,hosp48,hosp49,hosp50,hosp51,hosp52,hosp53,hosp54,hosp55,hosp56,hosp57,hosp58,hosp59,hosp60,hosp61,hosp62,hosp63,hosp64,hosp65,hosp66,hosp67,hosp68,hosp69,hosp70,hosp71,hosp72,hosp73,hosp74,hosp75,hosp76,hosp77,hosp78,hosp79,hosp80,hosp81,hosp82,hosp83,hosp84,hosp85,hosp86,hosp87,hosp88,hosp89,hosp90,hosp91,hosp92,hosp93,hosp94,hosp95,hosp96,hosp97,hosp98,hosp99,hosp100]
	cityList = set([hosp1.address,hosp2.address,hosp3.address])
	return render(request,'oxygen.html',{'hospitals' : hospitals, 'city' : cityList})    

def search(request):
	lol = request.GET['search']

	return render(request,'beds.html',{"answer":lol})



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			subject = 'Welcome to CovidClick'
			message = f'Hi {user.username}, thank you for registering with CovidClick.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return redirect("beds.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form}) 
		

 	
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/index")

def booknow(request):
	return render (request,"booknow.html") 
		

 	
	






	



