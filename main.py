import pickle
import json
import xml



class Student():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.studentov_kamos = None

    def __str__(self):
        return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"

    def to_json(self):
        return  json.dumps(self, default=lambda  obj:obj.__dict__)

    def to_xml(self):
        return  xml.dumps(self, default=lambda  obj:obj.__dict__)

    def uloz_do_suboru(self, nazov):
        with open(nazov, "w") as file:
            file.write(self.to_json())

    def uloz_do_suboru1(self, nazor):
        with open(nazor, "w") as file:
            file.write(self.to_xml())


patrik = Student("Patrik", 30, "Slovensko")
allan = Student("allan", 37, "Nikaragua")
patrik.studentov_kamos = allan
patrik.uloz_do_suboru("patrik.json")









""""
    @staticmethod
    def vytvor_zo_suboru(nazov_suboru):
        with open(nazov_suboru, "rb") as file:
            return pickle.load(file)
patrik_zo_suboru = Student.vytvor_zo_suboru("patrik.dat")
print(patrik_zo_suboru)

# patrik = Student("Patrik", 30, "Slovensko")
# patrik.vloz_do_suboru("patrik.dat")
   
    def vloz_do_suboru(self, nazov_suboru):
        with open(nazov_suboru, "rb") as file:
            pickle.dump(self, file)"""
