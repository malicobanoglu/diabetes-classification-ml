import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report



print("Welcome to diabet test")
print("Please select the action you want to perform:")
print("1)Adding data\n2)Diabet Test")

diabet_data = pd.read_csv("diyabet_temizlenmis.csv")
df = diabet_data.copy()
x = df.drop("Outcome" , axis =1 )
y = df["Outcome"]
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size= 0.2 ,random_state= 42)

xgb_model = xgb.XGBRFClassifier().fit(x_train, y_train)

deneme_hakki = 3 
while deneme_hakki > 0 :
    cevap = input("Your action : ")
    if cevap == 0 :
        print("Geçersiz işlem Lütfen tekrar deneyin")
        deneme_hakki -= 1
    elif cevap == 1 : 
         pregnacies = input("Pregnancies?(Y/N)") 
         Glucose = int(input("Glucose:"))
         BloodPressure = int(input("BloodPressure:"))
         SkinThickness = int(input("SkinThickness:"))
         Insulin = int(input("Insulin:"))
         BMI = int(input("BMI:"))
         Age = int(input("Age:"))
         DiabetesPedigreeFunction = int(input("DiabetesPedigreeFunction:"))
         output = int(input("Do you have diabetes?"))

    else : 
         answers = [[]]
         pregnacies = input("Pregnancies?(Y/N)") 
         if pregnacies == "Y":
             answers[0].append(1)
         else :
             answers[0].append(0)
         Glucose = int(input("Glucose:"))
         answers[0].append(Glucose)
         BloodPressure = int(input("BloodPressure:"))
         answers[0].append(BloodPressure)
         SkinThickness = int(input("SkinThickness:"))
         answers[0].append(SkinThickness)
         Insulin = int(input("Insulin:"))
         answers[0].append(Insulin)
         BMI = int(input("BMI:"))
         answers[0].append(BMI)
         Age = int(input("Age:"))
         answers[0].append(Age)
         DiabetesPedigreeFunction = float(input("DiabetesPedigreeFunction:"))
         answers[0].append(DiabetesPedigreeFunction)
        
         pred = xgb_model.predict(answers)

         if pred == 1 :
             print("According to our model you have diabets.")
         else :  
            print("According to our model you do not have diabets.")




if deneme_hakki == 0 :
    print("Exiting...")