#3. Создать текстовый файл (не программно), 
#построчно записать фамилии сотрудников и величину их окладов. 
#Определить, кто из сотрудников имеет оклад менее 20 тыс., 
#вывести фамилии этих сотрудников. 
#Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
        

print((sum(map(float, workers.values())))/len(workers.values()))

 