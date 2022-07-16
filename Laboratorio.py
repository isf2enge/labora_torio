"""
Alunos:Isaias Soares Figueiredo,Moisés Alves Cardoso
Programa para simular um laborátorio,realizando o cadastro de exames com seus respectivos métodos de acrescentar,remover,ou adicionar algum exame,ou consultar
o preço do exame,além de no final estar calculando o preco total dos exames
obs:O programa realiza o trabalho por meio de uma tabela fixa de exames que são:Hemograma,Ureia,Creatinina,Urocultura,Glicose,Testosterona
"""
from abc import ABC,abstractmethod #Importando biblioteca para abstrair a classe

class Labagreste(ABC): #Classe LabAgreste abstrata

    def __init__(self,nomecompleto,nascimento,posto,exames): #Aqui foram atributos privados:nomecompleto,posto(de coleta),exames.Portanto Todos estão encapsulados
        self.__nomecompleto=nomecompleto
        self.__nascimento=nascimento
        self.__posto=posto
        self.__exames=exames
#-------------------------------------------------------------------
    #Os metodos aqui foram abstraidos,portanto tornando-se apenas um modelo para ser alterado   
    @abstractmethod 
    def removerexames(self,remove): #Metodo abstrato para remover o exame da lista
        pass
    @abstractmethod
    def adicionarexames(self,adicionar): #Metodo abstrato para adicionar o exame na lista
        pass
    
    @abstractmethod
    def trocardeexame(self,trocar,examess): #Metodo abstrato para trocar o exame 
        pass
    
    @abstractmethod
    def calcularprecodosexames(self): #Metodo abstrato para calcular o preco individual de cada exame
        pass

    @abstractmethod
    def trocardeexame(self): #Metodo abstrato para trocar de exame
        pass

#----------------------------------------------------------------
    #Get e set público para nomecompleto
    def getnomecompleto(self):
        return self.__nomecompleto
    def setnomecompleto(self,nomes):
        self.__nomecompleto=nomes
    #Get e set público para nascimento
    def getnascimento(self):
        return self.__nascimento
    def setnascimento(self,nascimentos):
        self.__nascimento=nascimentos
    #Get e set público para posto
    def getposto(self):
        return self.__posto
    def setposto(self,postos):
        self.__posto=postos
    #Get e set público para exames
    def getexames(self):
        return self.__exames
    def setexames(self,exame):
        self.__exames=exame

class Cadastrodepacientes(Labagreste): #Classe Herança de Labagreste criada
    
    def __init__(self,nomecompleto,nascimento,posto,exames): #Herdando os atributos da Labagreste
        
        super(Cadastrodepacientes,self).__init__(nomecompleto,nascimento,posto,exames) #Comando 'super()' para importar os metodos e atributos de Labagreste
        
    def removerexames(self,remove): #Metodo que sobrepõe o Metodo abstrato da classe  Labagreste.Portanto um polimorfismo realizado
        n=-1
        for i in self.getexames(): #Ciclo de repetição que vai percorrer a lista e ir removendo conforme o elemento desejado
            n+=1
            if i==remove:
                del(self.getexames()[n])
                
   
    def adicionarexames(self,adicionar):#Metodo que sobrepõe o Metodo abstrato da classe Labagreste.Portanto um polimorfismo realizado.
    
    	#Ciclo de repetição para ir adicionando os elementos a lista
        for i in ['Hemograma','Ureia','Creatinina','Urocultura','Glicose','Testosterona']:  
            if i==adicionar:
               return (self.getexames().append(adicionar))
            
        return print('Erro {} não  está na lista!'.format(adicionar)) #Caso o elemento não esteja na lista fixa, retorna mensagem de erro
            
       
        
   
    def trocardeexame(self,trocar,examess): #Metodo que sobrepõe o Metodo  abstrato da classe Labagreste.Portanto um polimorfismo realizado.
        n=-1
        for i in self.getexames():
            n+=1
            if i==examess:
                self.getexames()[n]=trocar
                
    def calcularprecodosexames(self): #Metodo que sobrepõe o Metodo  abstrato da classe Labagreste.Portanto um polimorfismo realizado.
        conta=0
      
        for i in self.getexames(): #Ciclo de repetição para percorrer a lista e calcular a soma,dos preços
            if i=='Hemograma':
                conta=conta+50
            if i=='Ureia':
                conta=conta+10
            if i=='Creatinina':
                conta=conta+5
            if i=='Urocultura':
                conta+=3
            if i=='Glicose':
                conta+=2
            if i=='Testosterona':
                conta+=7
        return ('O preco total é {}R$'.format(conta))
    
    def consultarpreco_de_exame_individual(self,consulta): #Metodo próprio da classe Cadastrodepacientes,aqui não foi importado nenhum metodo
        for i in self.getexames():
            if i=='Hemograma' and i==consulta: #Ciclo de repetição para percorrer o exame desejado e consultar o seu preço
                return print(i,'custa','50R$')
            elif i=='Ureia' and i==consulta:
                return print(i,'custa','10R$')
            elif i=='Creatinina' and i==consulta:
                return print(i,'custa','5R$')
            elif i=='Urocultura' and i==consulta:
                return print(i,'custa','3R$')
            elif i=='Glicose' and i==consulta :
                return print(i,'custa','2R$')
            elif i=='Testosterona' and i==consulta:
                return (print(i,'custa','7R$'))
        return (print('Alternativa invalida')) #Caso escolha um exame inválido da lista ele retorna a mensagem


    

def main(): #corpo do programa para realizar testes
    n=0
    a=0
    Pacientes=[] #Lista simples para armazenar os objetos pacientes com seus respectivos atributos

    print('Olá bem vindo ao Labagreste') #Imprime uma mensagem de boas vindas
    
    n=int(input('Digite o numero de pacientes: ')) #Digite o numero de pacientes para poder definir o tamanho da lista 'Pacientes'
    
    for i in range(n): #Repetição para ir criando a lista Pacientes

        #Vai criando a lista e os objetos pacientes conforme os atributos nome,data,posto,exame
        Pacientes.append(Cadastrodepacientes(input('Digite o nome  completo do paciente: '),
                                             input('Digite a data de nascimento: '),input('Digite o posto: '),[input('Digite o exame: ')]))
        
        while (a!=5): #Menu para ir realizando os metodos da classe Cadastrodepacientes
            print('O que deseja fazer? ')
            print('(1) Adicionar algum exame: ')
            print('(2) Remover algum exame: ')
            print('(3) mudar algum exame: ')
            print('(4) consultar preco de exame individual:')
            print('(5) Preco total')
            a=int(input())
            
            if a==1:
                
                n1=0
                print('Quais exames deseja adicionar: ') #Lista de exames que o laboratório realiza
                print('Hemograma')
                print('Ureia')
                print('Creatinina')
                print('Urocultura')
                print('Glicose')
                print('Testosterona')
                
            while n1!=1: #Ciclo de repetição para ir acrescentando os exames por meio do metodo adicionarexames
                
                print(Pacientes[i].getexames()) #Imprime os exames
                Pacientes[i].adicionarexames(input()) #Metodo para adicionar os exames
                print('Digite 1 para concluir ou 0 para adicionar mais')
                n1=int(input())
        
            if a==2:
                n2=0
                while n2!=1: #Ciclo de repetição para ir removendo os exames por meio do metodo removerexames
                    
                    print(Pacientes[i].getexames()) #Imprime os exames
                    Pacientes[i].removerexames(input('Qual exame deseja remover: '))
                    
                    n2=int(input("Digite 1 para concluir ou 0 para remover mais ")) #Criterio de parada
    
            if a==3:
            
                n2=0
                while n2!=1: #Ciclo de repetição para ir trocando os exames da posição da lista  por meio do metodo trocardeexames
                    
                    print(Pacientes[i].getexames())  #Imprime os exames
                    
                    Pacientes[i].trocardeexame(input('Qual exame deseja mudar:'),(input('Por qual exame quer trocar: ')))
                    
                    n2=int(input("Digite 1 para concluir ou 0 para mudar outro: ")) #Criterio de parada
            if a==4:
                n2=0
                while n2!=1: #Ciclo de repetição para ir pesquisando os preços dos exames individualmente
                    print(Pacientes[i].getexames()) #Imprime os exames
                    
                    Pacientes[i].consultarpreco_de_exame_individual(input('Qual exame deseja saber o preco:')) #Classe para pesquisar os exames
                    
                    n2=int(input("Digite 1 para concluir ou 0 para mudar outro: ")) #Critério de parada
                 
            if a==5:
                
                print(Pacientes[i].getexames()) #Imprime os exames
                
                print( Pacientes[i].calcularprecodosexames())  #Imprime o valor total dos exames e encerra o programa
   
   
  
 
if __name__ =='__main__':
    main()
               
        
        
    
    

       
        
        
            
        
    

    
    

    


            
            
        
    
    
                
        

        
