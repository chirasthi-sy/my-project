#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#Change Added
print("Welcome to the application ")

# Chirasthi Amarasingha - 206009L

# This algorithm takes a list of donations and ensures that the non-neighbour donations are maximized

donation = []
total_odd = 0
total_even = 0
has_donated_odd = []
has_donated_even = []
not_done = True

while not_done == True:
    prompt = input("Continue? (y/n): ")
    if prompt == "y":
        x = input("Enter donation: ")
        donation.append(int(x))
        
    else:
        not_done = False
    

for i, v in enumerate(donation):
    if (i==0) or (i%2 == 0):
        total_even = total_even + v
        has_donated_even.append(v)
    
    else:
        total_odd = total_odd + v
        has_donated_odd.append(v)


if total_even > total_odd:
    print(has_donated_even, "donations provide the maximum  of %d." %total_even)

else:
    print(has_donated_odd, "donations provide the maximum  of %d." %total_odd)

for x in range(0,20):
    print(x)
