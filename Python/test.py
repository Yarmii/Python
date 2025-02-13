#Делает первую букву заглавной 
a = "привет как дела норм?"
print(a.capitalize()) 


b= "привет как дела норм?"
print(b.swapcase())
#Делает все маленькие буквы
c = "Привет Как Дела Норм?"
print(c.title())  

d = "привет как дела норм?"
print(d.lower()) 
#Делает все большые буквы
i = "привет как дела норм?"
print(i.upper()) 

f="abcde"
f1 ="ab"
if f1.find(f):
 print("ok")
else:
 print("no")

text = input(("Введите строку: "))
if text.endswith("."):
 text = text[:-1]
words = text.split()
words_count = len(words)
print(words_count)





