# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean);

# calculateGmean(8,7); 
# calculateGmean(b=7, a=8);  // can change order to 


# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     return mean;   

# ans=calculateGmean(8,7); 
# print(ans) 



# take tuple in arguments

# def avg(* no):
#     sm=0;
#     for i in no:
#         sm+=i;
#     print("avg is: ", sm/len(no));

# avg(5, 6, 7);



#  taking dictionary in arguments

# def name(** name):
#     print("Hello,", name["fname"], name["lname"]);

# name(fname="Ankit", lname="Yadav");


# enumerate function

marks = [12, 56, 32, 98, 12, 45];
for idx, mark in enumerate(marks):
    print(mark);
    if(idx==3):
        print("harry")
    idx+=1;