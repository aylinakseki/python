#Önce name variableına kullanıcıdan input alarak bir değer atıyoruz.
#sonra number variable ına input olarak değer atıyoruz fakat sayıyı tanımlaması için başına integer ekliyoruz
#bu ikisini cümlede kullanmak için printliyoruz ve bunu yaparken cümlenin kullanmadığımız kısmını sabir olması için "" içine alıyoruz.
# artılardan sonra boşluk koymayı unutmuyourz, integer ve yazıyı birleştirmek için str yazarak number ve name i yarine yerleştiririz.

#ikinci soruda if ve else leri kullanarak birkaç cümlelik bir yapı oluştururuz. 
# önce if yazarak sayılara eşit mi değil mi kontolü ile fonsiyonu print ile yazmaya devam ederiz
#print içine cümleyi bir önceki gibi yerleştiririz, if ise true değil ise false
# 3.soruda a variable ını input olarak first integer değerimni atarız fakat başına sayı gireceğimiz için int i koymalıyız
#formüllere birer isim takarız ve print ile yazmaya başlarız 
# a ve b variablerri önüne string işareti koyarız ki variable tanımlasın
emre = "Hello, World!"
print(emre)

name = input("What's your name: ")
number = int(input("Tell me a number from 1 to 5: "))
print("Your favorite number is", str(number),",", str(name))

if(number==1):
    print("Hi", name,"!", "Your number is 1. True")
else:
    print("Hi", name,"!", "Your number is 1. False")
if(number==2):
    print("Hi", name,"!", "Your number is 2. True")   
else:
    print("Hi", name,"!", "Your number is 2. False") 
if(number==3):
    print("Hi", name,"!", "Your number is 3. True")
else:
    print("Hi", name,"!", "Your number is 3. False")
if(number==4):
    print("Hi", name,"!", "Your number is 4. True")
else:
    print("Hi", name,"!", "Your number is 4. False")

a= int(input("First integer: "))
b= int(input("Second integer: "))

sum= a+b
dif= a-b
multi= a*b
div= a/b
print(str(a),"+",str(b),"=",str(sum))
print(str(a),"-",str(b),"=",str(dif))
print(str(a),"*",str(b),"=",str(multi))
print(str(a),"/",str(b),"=",str(div))