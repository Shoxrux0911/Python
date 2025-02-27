# Functions

# def my_sum(a,b):
#     return((a +b))

# print(my_sum(7,7))

# def my_radius(rad):
#     pi = 3.14
#     return(pi * rad * rad)

# print(my_radius(3))

# def my_min(a):
#     my_list = list(a)
#     my_list.sort()
#     return my_list[0]

# print(my_min([5, 6, 8, 4, 10]))

# def my_max(n):
#     my_ls = list(n)
#     my_ls.sort()
#     return my_ls[-1]
# print(my_max([5, 6, 8, 9, 11]))

# def my_len(ol: list):
#     lens = []
#     for my_l in ol:
#         lens.append(len(my_l))
#     return lens

# print(my_len(["John", "Bek", "HI", "HEllo"]))

# °F = (°C x 9/5) + 32.

# def my_f(Cradus):
#     return((Cradus * 9/5) + 32)
# print(my_f(14))


# def check_season(month):
#     month = month.lower()  
#     if month in ("september", "october", "november"):
#         return "Autumn"
#     elif month in ("december", "january", "february"):
#         return "Winter"
#     elif month in ("march", "april", "may"):
#         return "Spring"
#     elif month in ("june", "july", "augst"):
#         return "Summer"
#     else:
#         return "Invalid month"
# print(check_season("September"))

    
# def reverse_list(my_l):
#     revers_list = []
#     for my_l1 in my_l:
#         revers_list.insert(0, my_l1)
#     return revers_list
    
# print(reverse_list(["list", "hello", "Hi", "what"]))

# def my_functionlist(liss):
#     for i in liss:
#         print(i)

# my_functionlist(["Hi", "Hello", "How", "where"])

# print(my_functionlist)

# def my_capitilize(l1):
#     return [i.capitalize() for i in l1]

   
# print(my_capitilize(["hi", "alex", "capital", "python"]))

# def add_item(a, b):
#     a.append(b)
#     return a

# number = [5, 6, 7, 8]
# print(add_item(number, 9))

# fruit = ["banana", "apple", "orange"]

# print(add_item(fruit, "strawberry"))
    
# def my_remove(my_list, mine):
#         my_list.remove(mine)
#         return(my_list)

# my_list = ['Potato', 'Tomato', 'Mango', 'Milk']

# print(my_remove(my_list, 'Potato'))

# def even_and_odd(a):
#     even_count = 0
#     odd_count = 0
#     for even in range(a):
#         if even %2 ==0:
#             even_count +=1
#         else:
#             odd_count+=1
        
#     print(f"number of even {even_count}, number of odd {odd_count}")

# even_and_odd(100)

# def factorial_function(a):
#     num = 1
#     for i in range(1, a+1):
#         num *= i
#     return num
# print(factorial_function(5))


# def are_unique(a):
#     return len(a) == len(set(a))

# print(are_unique([1, 2, 1, 30]))
# print(are_unique([1, 2, 3, 4]))

# def same_item(b):
#     return b == (b)
# print(same_item(['apple', 'banana', 'cherry']))
# print(same_item(['apple', 'apple', 'apple']))

# isinstance()
# all()

# def same_data(b):
#     return all(isinstance(item, type(b[0])) for item in b)

# print(same_data(['apple', 'banana', 'cherry']))
# print(same_data([1, 2, 'b', 4]))

# def my_prime(a):
#     prime = True
#     for i in range(2, a):
#         if a % i == 0:
#             prime = False
#     if prime:
#         print("True")
#     else:
#         print("False")

# my_prime(22)    


# def my_factorial(a):
#     num = 1
#     for i in range(1, a+1):
#         num*=i
#     return num

# print(my_factorial(5))


# def my_unique(a):
#     return len(a)== len(set(a))
# print(my_unique([1, 3, 'a', 4]))

# def same_data(a):
#     return (all(isinstance(item, type(a[0])) for item in a))


# print(same_data(["a", 2]))    

# def factorial(a):
#     if a==1:
#         return a
#     else:
#         return a * factorial(a-1)
    
# print(factorial(5))

# lamda function
# lambda arg: logic

# lst = ["Jack", "Abrahman", "David", "John"]
# result = map(lambda n: n.lower().count("a"), lst)

# print(list(result)) 

# num = [2, 3, 4, 5, 6, 7, 8, 9 , 12]

# result = filter(lambda n: n % 3 ==0, num)

# print(list(result))  


# try:
#     print("HI")
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("final")
