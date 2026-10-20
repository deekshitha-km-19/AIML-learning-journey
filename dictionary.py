student={
"name": "deeksha",
"age": 19,
"college": "VTU university",
"city": "mandya",
}
print(type(student))
print(student)
print(student["city"])
print(student["age"])
print(student["name"])
print(student["college"])
student["name"]="chintu"
print(student)
student.pop("age")
print(student)
print(student.keys())
print(student.items())
print(student.values())
print(student.get(dict))
student.update({"age": 19})

profile={
    "username":"deeksha",
    "details":{
        "followers":180,
        "verified":True
    }
}
print(profile["details"]["followers"])
print(profile)
