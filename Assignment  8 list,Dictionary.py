# List (Creation,Modification,Access)
# 1,List creation

age_list = [24,25,26,27,28]

name_list = ["raeeza","remees","adam","amaal","suhara"]

#List operations and modifications

name_list.append("Yazhini")
print(name_list)

age_list.insert(2,30)
print(age_list)

name_list.remove("Yazhini")
print(name_list)

age_list.pop(-1)
print(age_list)

age_list.extend([29,30,26])
print(age_list)

age_list.sort(reverse=True)
print(age_list)

print(max(age_list))
print(min(age_list))
print(sum(age_list))

#3,Accessing list elements

print(name_list[0])
print(name_list[-1])
print(name_list[2:4])
print(name_list[::-1])

#Dictionary(Creation.Modification,Access)
Student_marks={"raeeza":85,
               "Remees":90,
               "Adam":75,
              "Amaal":95,
              "John":80}

print(Student_marks["Remees"])

Student_marks["Janani"] = 80
Student_marks["Raeeza"] = 82

Student_marks = {"Raeeza":85,
                 "Remees":90,
                 "Adam":75,
                 "Amaal":95,
                 "John":80}
print(Student_marks["Raeeza"])
Student_marks["Janani"] = 80
Student_marks["Raeeza"] = 82
print(Student_marks)

my_set = {'a','e','i','o','u','a','a','i'}
print(my_set)
# my_set[4] = 's'  #sets are unordered and unindexed ,so we cannot access an element
set1 = {1,3,5,7,9}
set2 = {2,3,5,8,10}
set3 = set1.union(set2)
print(set3)


set3=set1.intersection(set2)
print(set3)

#Operators and conditional statement
score = float(input("enter your score(0 to 10): "))

if score > 7 :
    print("Above Average: Excellent performance!")
elif score >= 4 :
    print("Average : Good effort!Keep practising.")
else:
    print("Below Average: Need to improve your Performance.") 



    
        
    



        
