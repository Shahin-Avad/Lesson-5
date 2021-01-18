#2. Создать текстовый файл (не программно), 
#сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


f = open("count.txt", "r", encoding='utf-8')
content = len(f.read())
 
print(content)

f = open("count.txt", "r", encoding='utf-8') 
content = len(f.readlines())

print(content)





    