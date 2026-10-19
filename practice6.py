my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}


print(karnataka_food["Mysuru"])  

print(karnataka_food.get("Mangaluru"))  
print(karnataka_food.get("Shivamogga", "Not Found"))  

karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)


karnataka_food["Bengaluru"] = "Ragi Mudde"

mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  

del karnataka_food["Mangaluru"]

karnataka_food.clear()

print(karnataka_food.keys())  
print(karnataka_food.values())  
print(karnataka_food.items())  
  
new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)