class person:
    def __init__(self, name, address, age, phonenumber):
        self.name = name
        self.address = address 
        self.age = age
        self.phonenumber = phonenumber

    def __str__(self):
        return f"{self.name}, ({self.age}), {self.address}, ({self.phonenumber})"

    def my_name(nam):
        print("My name is " + nam.name + ", " + "I live in " + nam.address + ", " + "My age is " + str(nam.age))     
per= person("tess", "nairobi", 22, "0728168422")

per.my_name()