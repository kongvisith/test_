
print ("---------------Homework---------------")


while  True:
    A = float(input("Khmer_Score :"))
    B = float(input("English_Score :"))
    C = float(input("Mathematical_Score :"))
    D = float(input("Chemistry_Score :"))
    E = float(input("Physics_Score :"))

    print ("--------------------------------------")
    Total = A+B+C+D+E
    average = Total / 5

    if average >=50:

        print ("Result = ",average,"Pass✅")
    else:
        print("Result =",average,"Fiall❌")

    print("--------------------------------------")
