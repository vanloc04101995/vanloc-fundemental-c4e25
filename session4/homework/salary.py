p_list = [
    {"name":"Huy","salary_hour": 25,"hours" : 30},
    { "name" : "Quan","salary_hour" : 25,"hours" : 20},
    {"name" : "Duc","salary_hour" : 30,"hours" : 40}
]
total_salary = 0
print("Salary each person :")
for i,val in enumerate(p_list) :
    print(val["name"],":",end=" ")
    salary_per = val["salary_hour"]*val["hours"]
    print(salary_per)
    total_salary += salary_per
print("Total salary:")
print(total_salary)
