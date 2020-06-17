from abc import ABC, abstractmethod
import random

class Parent(ABC): 

#Чтение файла my_alfabet

    def read_alpha(self):
        alphabet = []
        with open('my_alphabet.alph', 'r', encoding='utf-8') as file_alp :
            string =file_alp.readline()
            while  string:
                if  string[0]!='\n':
                    if len(string)<3:
                        if alphabet.count(string[0])<1:
                            alphabet.append(string[0])
                string=file_alp.readline()
        return alphabet
    #Чтение файла  my_text
    
    def read_text(self):
         with open('my_text.txt', 'r', encoding='utf-8') as file_text :
             line = file_text.readline()
             return line 
    #Чтение файла my_text.txt
    
    def read_text_txt (self):
        string = []
        with open('my_text.txt.encrypt', 'r', encoding='utf-8') as file_text :
           while True :
              line = file_text.readline()
              string= line 
              return string 

  
    #Чтение файла my_key 

    def read_key (self):
        dict_key = dict()
        with open('my_key.key', 'r', encoding='utf-8') as key_file:
             line = key_file.readline()
             while line:
                 line = line.replace('\n', ' ')  
                 line = line.split(' ', 1)
                 dict_key[line[0]]=line[1]  
                 line = key_file.readline()
             return dict_key
          

class Replacement (Parent):
   #Метод замены
   #Шифровка
   def encryption(self) : 
        obj = Parent ()
        text = obj.read_text()
        key = obj.read_alpha()
        crypt =''
        for i in text :
            if i in key :
                crypt += key[i]
                print ('Шифрование прошло успешно\n'+ cript)
                print("Введите путь для файла с кодированием текста")
                with open(self._enter_way("encode"),'w',encoding='utf-8') as encode_file:
                    encode_file.write("method of encryption: 2 - Transpositions!\n")
                    for index in range(0,len(line),length):
                        if index<=len(line):
                            my_list=list(line[index:index+length])
                        i=0
                        list_none=[None]*len(key_list)
                        for item in my_list:
                            if len(my_list)<length:
                                my_list.append("q")
                            list_none[int(key_list[i])-1]=item              
                            i+=1
                        string=''
                        for item in list_none:
                            if item==None:
                                item=''
                            string=string+item
                        encode_file.write(string)
    #Дешифровки 
   def revers(self):
        obj = Parent ()
        text = obj.read_text_txt()
        key = obj.read_alpha()
        descrypt = ''
        for i in text :
            if i in key :
                descrypt += key[i]
                print ('Дешифрование прошло успешно\n' + descrypt)
                with open(self._enter_way("txt"),'a',encoding='utf-8') as decode_file:
                    for index in range(0,len(line),length):
                        if index<=len(line):
                            my_list=list(line[index:index+length])
                        i=0
                        string=''
                        for item in my_list:
                            ch=my_list[int(key_list[i])-1]
                            i+=1
                            string=string+ch
                        decode_file.write(string)


class TRANSPOS(Parent):
    #Метод перестановки
   #Генерирование ключа 
    def gener_key(self):   
        try:
            length=0
            while length<2:
                length=int(input("Введите длину ключа "))
                if length<2:
                    print("Длинна ключа слишком маленькая")
            length+=1
            key_list=[x for x in range(1, length)]
            random.shuffle(key_list)
            with open(self._enter_way("key"),'w',encoding='utf-8') as gen_key:
                gen_key.write(str(length)+'\n')
                i=0
                string=''
                while i<len(key_list):                   
                    string=string+str(key_list[i])+' '
                    i+=1 
                gen_key.write(string)
                gen_key.write('\nmethod - :Transposition')
        except Exception:
            print("Попробуйте ввести длину ключа заново")
    #Шифровка
    def encrypt(self):    
        key_list=self.read_key()
        while key_list==None:
            print("Не правильный ключь")
            key_list=self.read_key()
        file_txt=self.read_txt()
        if key_list[-1]=='':
            key_list.pop()
        length=len(key_list)-1
        line=file_txt.read()
        list_block_length=[]
        i=0
        my_list=list()
        print("Введите путь для файла с кодированием текста")
        with open(self._enter_way("encode"),'w',encoding='utf-8') as encode_file:
            encode_file.write("method of encryption: 2 - Transpositions!\n")
            for index in range(0,len(line),length):
                if index<=len(line):
                    my_list=list(line[index:index+length])
                i=0
                list_none=[None]*len(key_list)
                for item in my_list:
                    if len(my_list)<length:
                        my_list.append("q")
                    list_none[int(key_list[i])-1]=item              
                    i+=1
                string=''
                for item in list_none:
                    if item==None:
                        item=''
                    string=string+item
                encode_file.write(string)
   #Дешифровки 
    def revers(self):
            key_list=self.read_key()
            while key_list==None:
                print("Неправильный ключ - вы вводите путь к ключу для другого метода")
                key_list=self.read_key()
            encrypt_file=self.read_encrypt()
            line=encrypt_file.readline()
            while confirm[5]!='Transpositions!\n':
                print('Не правильно кодированный файл, укажите корректный файл')
                encrypt_file=self.read_encrypt()
                line=encrypt_file.readline()
                confirm=line.split(' ')
            line=encrypt_file.read() 
            if key_list[-1]=='':
               key_list.pop()
            length=len(key_list)-1
            print("Введите путь к файлу с засшифрованным текстом ")
            with open(self._enter_way("txt"),'a',encoding='utf-8') as decode_file:
                for index in range(0,len(line),length):
                    if index<=len(line):
                        my_list=list(line[index:index+length])
                    i=0
                    string=''
                    for item in my_list:
                        ch=my_list[int(key_list[i])-1]
                        i+=1
                        string=string+ch
                    decode_file.write(string)


class XOR(Parent):
   
    def read_XORkey(self):
        exit=0
        index=0
        i=0
        list_alph=list()
        list_key=list()
        flag=True
        print("Pleas, enter way to key file")
        while flag:
                with open(self._enter_way("key"),'r',encoding='utf-8') as key_file: 
                    for line in key_file:
                         try:
                             if line=='Key\n':
                                 j=0
                                 line=key_file.readline()
                                 list_key=line.split()
                                 if len(list_key)==1:
                                    list_alph.append(list_key[0])
                                    j+=1
                                 elif len(list_key)==2:
                                     index=int(list_key[1])
                                     j+=1
                                     i+=1
                                 if j==0 and line!='\n':
                                     list_key=line.split()
                                     if list_key[-1]=='XOR':
                                        break
                                     else:
                                         exit+=1
                                         break
                             if i==1 and line!='\n':
                                 if list_alph.count(line[0])==0:
                                    list_alph.append(line[0])
                             if i==0:
                                 list_second_line=line.split()
                                 if list_alph.count(line[0])==0:
                                    list_alph.append(line[0])
                                 if len(list_second_line)>1:
                                    index=int(list_second_line[1])
                                 else:
                                     index=0
                                 del(list_second_line)
                                 i+=1
                         except ValueError:
                             pass
                all_list=list()
                if exit==0:
                   all_list.append(list_alph)
                   all_list.append(list_key)
                   all_list.append(index)
                else:
                    return None
                return all_list
           

    def _alphabet(self):
        list_alph=list()
        i=0
        list_second_line=list()
        print("Pleas, enter way for file with alphabet ")
        alphabet=open(self._enter_way("alph"),"r",encoding='utf-8')
        return alphabet
        
    def gen_key(self): 
        list_key=list()
        alphabet_file=self._alphabet()
        list_alph=alphabet_file.read()
        gamma=0
        print("Pleas, enter gamma. The number must be greater than 1 ")
        while gamma<2:
            gamma=int(input(".>> "))
            if gamma<2:
                print("The number is smoll ")
        i=0
        list_alph=list_alph.split('\n')
        list_key=[x for x in range(1, gamma+1)]
        random.shuffle(list_key)
        print("Pleas, enter way for key file")
        list_key.append('XOR')
        with open(self._enter_way("key"),"w", encoding='utf-8') as key_file:
            for ellement in list_alph:
                key_file.write(str(ellement)+'\n')
            key_file.write("\n\nKey\n")
            for ellement in list_key:
                key_file.write(str(ellement))
                key_file.write(' ')
            key_file.write('\nmethod - :XOR')
        print("Key succesfull complete")



    def encrypt(self):
        text_file=self.read_txt()
        list_alph=list()
        list_key=list()
        index=0
        i=0
        all_list=self.read_XORkey()
        while all_list==None:
            print("Wrong key - you enter way to key for another method")
            all_list=self.read_XORkey()
        list_alph=all_list[0]
        list_key=all_list[1]
        if list_key[-1]=='XOR':
            list_key.pop()
        index=all_list[2]
        print("Pleas, enter way for encode file ")
        string_line=''
        index_encode=0
        encode_ellement=''
        exit=0
        with open(self._enter_way("encode"),'w',encoding='utf-8') as encode_file:
            encode_file.write("method of encryption: 3 - XOR!\n")
            while exit!=100:
                text=text_file.read(len(list_key))
                i=0
                string_block=''
                new_index=0
                if text=='':
                    exit+=1
                for ch in text:
                    try:
                        if 0<list_alph.count(ch):
                            index_encode=list_alph.index(ch)+index
                            key_ellement=list_key[i]
                            encode_ellement=list_alph[(index_encode+int(key_ellement))%len(list_alph)]
                            i+=1
                            string_block=string_block+encode_ellement
                        else:
                            string_block=string_block+ch
                    except ValueError:
                        pass
                string_line=string_line+string_block
            encode_file.write(string_line)
        print("Succesfull")


    def revers(self):
        encrypt_file=self.read_encrypt()
        line=encrypt_file.readline()
        confirm=line.split(' ')
        while confirm[5]!='XOR!\n':
                print('Wrong encode file, pleas enter correct encode file')
                encrypt_file=self.read_encrypt()
                line=encrypt_file.readline()
                confirm=line.split(' ')
        list_alph=list()
        list_key=list()
        i=0
        all_list=self.read_XORkey()
        while all_list==None:
            print("Wrong key - you enter way to key for another method")
            all_list=self.read_XORkey()
        list_alph=all_list[0]
        list_key=all_list[1]
        index=all_list[2]
        if list_key[-1]=='XOR':
            list_key.pop()
        index=all_list[2]
        string_line=''
        index_encode=0
        encode_ellement=''
        exit=0
        print("Pleas, enter way for file with decrypt text ")
        with open(self._enter_way("txt"),'w',encoding='utf-8') as decrypt_file:            
            while exit!=100:
                text=encrypt_file.read(len(list_key))
                i=0
                string_block=''
                new_index=0
                if text=='':
                    exit+=1
                for ch in text:
                    try:
                        if 0<list_alph.count(ch):
                            index_encode=list_alph.index(ch)-index 
                            key_ellement=list_key[i]
                            j=(index_encode-int(key_ellement))%(len(list_alph))
                            encode_ellement=list_alph[j]
                            i+=1
                            string_block=string_block+encode_ellement
                        else:
                            string_block=string_block+ch
                    except ValueError:
                        pass
                string_line=string_line+string_block
            decrypt_file.write(string_line)
        print("Succesfull")


# Создание меню
flag = True
obj_1=Replacement()
obj_2=TRANSPOS()
obj_3=XOR()
while flag :
    print ('Главное меню')
    print ('1) Зашифровка\Расшифровка\n2) Сгенерировать ключ')
    asd = input ()
    if asd == '1' :
        print ('Ваш вабор : 1 ')
    elif asd == '2' :
        print ('Ваш вабор : 2')
    else :
        print ('Error404')
    print ('Подменю')
    if asd == '1' :
        print('Зашифровка\Расшифровка')
        print ('1) Зашифровка\n2) Расшифровка')
        val_1 = input ()
        
        if val_1 == '1' :
            print ('Выберете метод зашифровки\n 1)замены\n 2)перестановки\n 3)гаммирования')
            val_3 = input ()
            if val_3 == '1':
                print ('Ваш выбор - замены')
                method= obj_1.encryption()
            elif val_3 == '2' :
                print ('Ваш выбор - перестановки')
                method= obj_2.encryption()
            elif val_3 == '3' :
                print ('Ваш выбор - гаммирования')
                method= obj_3.encryption()
            else :
                print ('Error404')
        elif val_1 == '2' :
            print ('Выберете метод расшифровки\n 1)замены\n 2)перестановки\n 3)гаммирования')
            val_3 = input ()
            if val_3 == '1':
                print ('Ваш выбор - замены')
                method= obj_1.revers()
            elif val_3 == '2' :
                print ('Ваш выбор - перестановки')
                method= obj_2.revers()
            elif val_3 == '3' :
                print ('Ваш выбор - гаммирования')
                method= obj_3.revers() 
            else :
                print ('Error404')
        else :
            print ('Error404')
    elif asd == '2' :
        print ('Выберете алгоритм шифра')
        print ('1) Шифр замены\n2) Шифр перестановки')
        val_2 = input ()
        if val_2 == '1' :
            print ('Сгенерировать ключ/шифр замены')
            method= obj_1.gen_key() 
        elif val_2 == '2' :
            print ('Сгенерировать ключ/шифр перестановки')
            method= obj_2.gener_key()
        else :
            print ('Error404')
    else :
        print ('Error404')
    

   
        
