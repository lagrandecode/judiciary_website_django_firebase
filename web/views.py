import email
from email import header
from multiprocessing import context
from re import sub
from django.shortcuts import render,redirect,HttpResponse
import pyrebase
from django.contrib import messages
import folium

# Create your views here.


#Applyinf firebase to the project 
# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyDN-Sne0GF1uSNlIYU_aRKqI7iIigAh7ww",
  "authDomain": "judicary-5d20a.firebaseapp.com",
  "databaseURL": "https://judicary-5d20a-default-rtdb.firebaseio.com",
  "projectId": "judicary-5d20a",
  "storageBucket": "judicary-5d20a.appspot.com",
  "messagingSenderId": "286397750808",
  "appId": "1:286397750808:web:536792ae3e428ba8d26d6d",
  "measurementId": "G-BMHM4XDXVY"
};

# # // Initialize Firebase

firebase = pyrebase.initialize_app(firebaseConfig)

# Get reference to the auth service

auth = firebase.auth()

def home(request):
# This is the authentication functions
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            auth.sign_in_with_email_and_password(email=email,password=password)
            print("successful")
            return redirect('dashboard')
        except:
            messages.info(request,'Incorrect Password or Username')
    return render(request, 'home.html')
# End of authentication functions

# function to download csv 
def dashboard(request):
    import json
    import requests
    header={
        "Authorization":"Token 9d605040f864b7572c3938ae5eaeacd28519dee7"
    }
    fetch_csv = requests.get("https://kobo.humanitarianresponse.info/api/v2/assets/aT5kWCgcFpLDuBmTsowebo/export-settings/esRJfp8Wm4xjbjdbXxhxw9R.json",
    headers=header,auth=('lagosjudiciarytemplate','lagosstate'))
    csv = json.loads(fetch_csv.content)
    

    # Here I'm fetching the submission url

    fetch_submission = requests.get("https://kobo.humanitarianresponse.info/api/v2/assets/aT5kWCgcFpLDuBmTsowebo.json",
    headers=header,auth=('lagosjudiciarytemplate','lagosstate'))
    deploy = json.loads(fetch_submission.content)
    
    context={
        "csv":csv,
        'deploy':deploy
    }
    return render(request,"dashboard.html",context)
# end csv function

# Adding map to the project
# def showmap(request):
#     import requests
#     import json

#     k = 'hello world'
#     context = {
#         'k':k
#     }

#     header={
#         "Authorization":"Token 9d605040f864b7572c3938ae5eaeacd28519dee7"
#     }
#     fetchmap = requests.get("https://kc.humanitarianresponse.info/api/v1/data/1204071.json",
#     headers=header,auth=('lagosjudiciarytemplate','lagosstate'))
#     mapper = json.loads(fetchmap.content)
#     context= {
#         'mapper':mapper
#     }



#     # m = folium.Map(location=[6.452019, 3.43081],zoom_start=10)
#     # test = folium.Html('<b>Hello world</b>', script=True)
#     # popup = folium.Popup(test, max_width=2650)
#     # folium.RegularPolygonMarker(location=[6.452019, 3.43081], popup=popup).add_to(m)
#     # m=m._repr_html_() #updated
#     # context = {
#     #     'my_map': m,
#     #     }
#     print(mapper)
#     return render(request,"map.html",context)
