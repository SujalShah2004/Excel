age=int(input("enter age"))
weight=int(input("enter weight"))

if age>=18 and age<=50:
    if weight>=45 and weight<=90:
        print("person is eligible to donate")

    else:
        print("person is not eligible due to weight")

else:
    print("person is not eligible due to age")