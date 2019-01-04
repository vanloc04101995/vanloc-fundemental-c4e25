
p_list = [
    {"name":"Quan","age": 25},
    {"name":"Quan","age": 25},
    {"name" : "loc","age" : 23}
]

# khong dung append p_lst=[p1,p2,p3]
p_first = p_list[0]
print(p_first)
print(p_first["name"])

for p in p_list:
    print(p["name"],p["age"])