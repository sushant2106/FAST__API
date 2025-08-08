class Model:
    Employe=[]
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    
    def add_into_List(self):
        list=[]
        list.append(self.id)
        list.append(self.name)
        list.append(self.age)
        Model.Employe.append(list)


    def show_empl(self):
        for x in Model.Employe:
            print(x)




obj1=Model(1,'ram',23)
obj1.add_into_List()
obj2=Model(2,'shyam',24)
obj2.add_into_List()

print(obj1.name)


# for index,emp in enumerate(Model.Employe):
#     print(index,emp[index+1])
#     break





if __name__=='__main__':
    pass

    


