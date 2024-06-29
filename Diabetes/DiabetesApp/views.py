from django.shortcuts import render
from DiabetesApp.models import users
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
# Create your views here.
def loginview(request):
    return render(request,'login.html')



def regiterview(request):
    return render(request,'registration.html')
def saveuserview(request):
    usersname=request.POST["name"]
    contactno=request.POST["Contact Number"]
    useremail=request.POST["Email"]
    address=request.POST["Address"]
    username=request.POST["username"]
    userpassword=request.POST["password"]
    

    newuser=users(name=usersname,ContactNumber=contactno,Email=useremail,Address=address,Username=username,Password=userpassword)
    newuser.save()
    return render(request,'login.html')
def verifyloginview(request):
    usersname=request.POST["username"]
    password=request.POST["password"]

    user=users.objects.filter(Username=usersname)
    for u in user:
        if u.Password == password:
            return render(request,'home.html')
        else:
            return render(request,'login.html')
    
def CheckDiseaseview(request):
    Pregnancies=request.POST["Pregnancies"]
    Glucose=request.POST["Glucose"]
    BloodPressure=request.POST["BloodPressure"]
    SkinThickness=request.POST["SkinThickness"]
    Insulin=request.POST["Insulin"]
    BMI=request.POST["BMI"]
    DiabetesPedigreeFunction=request.POST["DiabetesPedigreeFunction"]
    Age=request.POST["Age"]


    dataset = pd.read_csv("diabetes.csv")
    X=dataset.iloc[:,:-1]
    Y=dataset.iloc[:,-1]
    




    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=.90)
    model=RandomForestClassifier(random_state=48)

    model.fit(X_train,Y_train)
    # test_data=np.array([6,148,72.0,35,0,33.6,0.627,50]).reshape(1,-1)
    test_data=np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,-1)



    predicted_result=model.predict(test_data)
    print(predicted_result[0])
    
    if predicted_result[0] == 1:
        print("you have diabetes")
        result="You have Diabetes"
    else:
        print("you are normal")
        result="You are normal"
    return render(request,'result.html',{'result':result})