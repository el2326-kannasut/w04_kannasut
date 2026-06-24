#[]
#f = {
 #   "a" : "dsfdsf"
#}
#t = {"f","d"}

# SET
music_club = {"ruckchart","somying","somhai","arnon"}
color = {"red","green","blue","orange"}
friut = {"orange","banana","watermelon","givi"}

#print("รายชื่อ", music_club)
#print(f"รายชื่อ {music_club}{color}{friut}")

#Union = รวมกัน  |
all_member = music_club | color | friut
#print(f"รายชื่อ{all_member}")

#Intersection หาสมาชิกร่วม (&)
color_friut = color & friut
print(f"รายชื่อ{color_friut}")


# Difference = ส่วนต่าง (-)
dif_color_fruit = friut - color
#print(f"รายชื่อ {dif_color_fruit}")

# Symmetric Difference = อยู่ในกลุ่มใดกลุ่มหนึ่ง
sym_color_fruit = color ^ friut
print(f"รายชื่อ{sym_color_fruit}")

# การตรวจสอบสมาชิกอยู่ใน set หรือไม่
set_check = {"orange","banana"}
if set_check.issubset(friut):
    print("มี")
else:
    print("ไม่มี")
