#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, 
#открывающую файл на чтение и считывающую построчно данные. 
#При этом английские числительные должны заменяться на русские. 
#Новый блок строк должен записываться в новый текстовый файл.

f_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

l_list = []
with open("text_4_new.txt", "w", encoding='utf-8') as n:
    with open('text_4.txt', 'r') as f:
        
        for line in f:
            line = line.split(' ', 1)
           
            l_list.append(f_dict.get(line[0]) + ' ' + line[1])
            
    n.writelines(l_list)
            

            
        
        
        