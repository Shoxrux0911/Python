# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])

# sample_dict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
#     }

# sample_dict["location"] = sample_dict.pop("city")

# print(sample_dict)

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }

# sample_dict["emp3"]["salary"] = 8500

# print(sample_dict)

# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}

# tuple_list = list(d1.items())

# print(tuple_list)

# sample_dict = {
#     'Physics': 82,
#     'Math': 65,
#     'history': 75,
#     'chemistry': 89,
#     'GK': 50
    
# }

# total = sum(sample_dict.values())
            
# print(total)

# 6

# asc_dc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
# des_dc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

# print(asc_dc)
# print(des_dc)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)

# # print(dict1)
# def sum(a, b): a + b

# (name = "m", function = lambda a, b : a + b)





# sam_dict = {
#     "name": 'Alice',
#     "age": '25',
#     "city": 'New_York'
# }

# print(sam_dict)

# print(sam_dict ['age'])

# print(sam_dict.get("age"))

# sam_dict['age'] = 26

# print(sam_dict)

# 12

# sam_dict["job"] = "enginer"

# print(sam_dict)

# 13

# del sam_dict["city"]

# print(sam_dict)

# 14

# sam_dict.pop("city")
# print(sam_dict)

# sam_dict.popitem()

# print(sam_dict)

# print(sam_dict.keys())

# print(sam_dict.values())

# for key, value in sam_dict.items():
#     print(key,value)

# print(list(sam_dict.items()))

# print("name" in sam_dict)

# sam_dict.clear()
# print(sam_dict)

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# sample_set.update(sample_list)

# print(sample_set)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1 | set2  # takes every item
# set4 = set1 & set2  # takes only identical
# set5 = set1.intersection(set2)  # also identical item

# print(set3)
# print(set4)
# print(set5)

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# sample_set.update(sample_list)

# print(sample_set)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# sample1 = set1.union(set2)
# sample2 = set1.intersection(set2)

# print(sample1)
# print(sample2)

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set1.update(set2)

# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})

# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# # set1.union(set2)
# # print(set1)

# set1.symmetric_difference(set2)
# print(set1)

# set1 = {10, 20, 30, 40, 50}

# set1.difference_update({10,20,30})
# print(set1)

a = ['a', 'b', 'c', 'd']

string = ''

for char in a:
    string += char

# print(string)

string = ''.join(a)
print(string)
