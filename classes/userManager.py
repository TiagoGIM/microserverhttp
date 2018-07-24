import json

#file_matriculas = 'data.txt'

class Data():

    def __init__(self, jsonFile):
        self.jsonFile = jsonFile
        self.data = {}

    def creatUser(self):
        new_user={}
        dados_label = ['name','matricula','projeto','tag']
        for x in dados_label:
            new_user[x]= input('entre com '+x+' << ')
        return new_user

    def newUser(self):
        dados = self.getUsers()
        print(dados)
        print(self.data, '<')

        if 'people' in dados:
            self.data['people'] = dados['people']
        else:
            self.data['people'].append(dados)
            
        user = self.creatUser()
        self.saveUser(user)       


    def putUser(self, data_put):
        with open(self.jsonFile, 'w') as outfile:  
            json.dump(data_put, outfile)

    def getUsers(self):
        try:
            with open(self.jsonFile) as json_file:  
                data_get = json.load(json_file)
            return data_get
        except :
            self.data = {}
            self.data['people'] = []
            return []


    def saveUser(self,user):
        self.data['people'].append(user)
        self.putUser( self.data)

    def  getMatriculasTags(self):
        self.data = self.getUsers()
        mats = []
        tgs = []
        if self.data is None:
            return None, None
        elif len(self.data) > 0:

            for p in self.data['people']:

                if 'tag' in p:
                    print('tag: ' + p['tag'])
                    tgs.append(p['tag'])
                    
                if 'matricula' in p:
                    print('matricula: ' + p['matricula'])
                    mats.append(p['matricula'])
            return mats,tgs
        else:
            print('return None')
            return None, None

