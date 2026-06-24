# Dictionry
phone_book = {}
phone_book02 = dict()

# สร้างค่าใน Dict
student = {
    "name": "John",
    "Gender" : "koy",
    "age": 24,
    "tel": "090-748-4444"
}
########################################
# แก้ไขค่า
#student["age"] = "23"
#student["Gender"] = "kay"
#print(student)["age"]
#print(student)["Gender"]
#######################################

#######################################
# ลบค่า
#del student["age"]
#data_pop = student.pop("age","no data")
#print(student)
#######################################

# print(student["name"])
#name_student = student.get("name","ไม่มีข้อมูล")
#print(name_student)

# room_number,capacity,equipment,teacher,
class_room = {
    "room_number" :"R302",
    "capacity" : 30,
    "equipment" : ["Computer","projector","Microphone"],
    "teacher" : {
        "name" : "kannasut Buranasing",
        "subject" : "programing",
        "tel" : "090-748-4444"
    }
} 
class_room_check = class_room.get("room_number","ไม่มีข้อมูล")