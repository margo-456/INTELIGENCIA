class automaticaCocina():
    def __init__(self,dato, posicion_automaticalavavajilla):
        #Asignamos la variable para guardar los datos
        self.dato=dato
        #Asignamos la variable para la posicion de la cocina
        self.posicion_automaticalavavajilla=posicion_automaticalavavajilla
        #Asignamos el costo de realización de una tarea
        self.costo=0
    
    #Muestra las cocinas que se encontraron
    def mostrarCocinasEncontrados(self):
        print('La maquina ha identificado unos productos ')
        for x in self.dato:
             print("La "+str(x)+" esta "+("sucia" if ((self.dato[x])[0]==1) else "limpia"))
    
    #Vamos a identificar las cocinas sucias
    def identificarCocinasSucias(self):
       self.cocinasSuciasEncontradas=[]
       for k, v in self.dato.items():
        if(v[0]==1):
            self.cocinasSuciasEncontradas.append(v[1]) 
    
    #nos redigiremos a la posición más a la izquierda
    def redirigirPosicion(self):
      if(self.posicion_automaticalavavajilla==self.cocinasSuciasEncontradas[0]):
        pass
      else:
        for i in range(int(self.posicion_automaticalavavajilla),int(self.cocinasSuciasEncontradas[0]),-1):
         print('girando de zona '+str(i)+' a posicion '+str(i-1))
         self.costo+=1
        
        self.posicion_automaticalavavajilla=self.cocinasSuciasEncontradas[0]   
    #Define si una zona es contenida como sucia
    def contienZona(self, numero):
        keys = list(self.dato.keys())
        for x in self.cocinasSuciasEncontradas:
            if(numero==x):
                print('Limpiando cocina : '+keys[x-1])
                return True
            
        return False
    #se procede a limpiar la cocina
    def LimpiandoCocinas(self):
        print('Se procederá a identificar las cocinas')
        self.mostrarCocinasEncontrados()
        self.identificarCocinasSucias()
        print('Se redirigir a una mejor posicion: ')
        self.redirigirPosicion()
        for i in range(self.posicion_automaticalavavajilla ,self.cocinasSuciasEncontradas[len(self.cocinasSuciasEncontradas)-1]+1,+1):
            if(self.contienZona(i)):
                self.costo+=1
                print('Moviendo')
            else:
                self.costo+=costo
                print('Moviendo')
        
        print('Ya no hay areas que limpiar ')
        print('El costo seria '+str(self.costo))

#Ingresamos las cocinas sucias y limpias, además la posición en la que se encuentra el limpiador
Cocina= automaticaCocina({"Cocina 1":[1, 1],"Cocina 2":[0, 2],"Cocina 3":[0, 3]}, 2)
Cocina.LimpiandoCocinas()