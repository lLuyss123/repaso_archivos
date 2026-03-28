import csv
import os


archi_name= "riwi_studens.csv"


#Metoh Write
def Metoh_Write(lis):
    with open (archi_name, mode="w",newline="") as file:
        writer= csv.DictWriter(file,fieldnames=["Name","Clan"])
        writer.writeheader()
        for dic in lis:
            writer.writerow(
                dic
            )
  
  
#Metoh Reader
def Metoh_Reader():
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        header= reader.fieldnames
        return header
        
        
#Metoh Print CSV
def Print_csv():
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        for dic in reader:
            print (dic)
        
#Metoh Adding 
def Metoh_Adding(name,clan):
    with open (archi_name, mode="a",newline="") as file:
        add= csv.DictWriter(file,fieldnames=Metoh_Reader())
        add.writerow(
            {
                "Name":name,
                "Clan":clan
            }
        )

#Metoh Searching 
def Metoh_Searching(name=None,clan=None):
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        for dic in reader:
            if clan is None and name is not None:
                if  dic["Name"]==name:
                    print(dic)
            else:
                if  dic["Clan"]==clan:
                    print(dic)
                    
                    
#Metoh Deleting 
def Metoh_Deleting(name=None,clan=None):
    lista=[]
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        
        for dic in reader:
            if  dic["Name"]==name or dic["Clan"]==clan:
                continue    
            lista.append(dic) 
    Metoh_Write(lista)
    print("----- DELETED -----")
    

#Metoh Updating 
def Metoh_Updating(name):
    lista=[]
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        
        for dic in reader:
            if dic["Name"]== name:
                name=input("Nuevo nombre")
                clan=input("Nuevo clan")
                lista.append({
                    "Name":name,
                    "Clan":clan
                })
                continue
            lista.append(dic)    
    Metoh_Write(lista)
    print("+++++ UPDATED ++++++")
                
            


        
op=int(input("Menú de opciones \n 1. Reescribre el archivo \n 2. Muestra el archivo \n 3. Agrega en el archivo \n 4. Busca en el archivo \n 5. Eliminar en el archivo \n 6. Actualizar en el archivo \n : "))
while op<=6:
    if op == 1:
        name= input("What's your name: ")
        clan = input("Clan's name: ")
        Metoh_Write([{
                "Name":name,
                "Clan":clan
            },])
    elif op == 2:
        Print_csv()
    elif op == 3:
        name= input("What's your name: ")
        clan = input("Clan's name: ")
        Metoh_Adding(name,clan)
    elif op == 4:
        op2= int( input("Search by \n 1. Name \n 2. Clan \n : "))
        if op2==1:
            name= input("What's the name: ")
            Metoh_Searching(name,None)
        else:
            clan= input("What's the Clan: ")
            Metoh_Searching(None,clan)
    elif op == 5:
        op2= int( input("Delet by \n 1. Name \n 2. Clan \n : "))
        if op2==1:
            name= input("What's the name: ")
            Metoh_Deleting(name,None)
        else:
            clan= input("What's the Clan: ")
            Metoh_Deleting(None,clan)
    elif op == 6:
        name= input("What's the name: ")
        Metoh_Updating(name)
        
    elif op == 7:
        archivo_existe = os.path.exists(archi_name)
        if archivo_existe:
            print("Existe")
        else:
            print("no existe")
    
    op=int(input("Menú de opciones \n 1. Reescribre el archivo \n 2. Muestra el archivo \n 3. Agrega en el archivo \n 4. Busca en el archivo \n 5. Eliminar en el archivo \n 6. Actualizar en el archivo \n : "))
    