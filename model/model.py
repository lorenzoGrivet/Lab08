import copy

from database.DAO import DAO
from model import powerOutages


class Model:
    def __init__(self):
        self._solBest = []
        self.max_persone=-1
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()



    def worstCase(self, nerc, maxY, maxH):
        # TO FILL
        parziale=[]
        self.loadEvents(nerc)
        self.ricorsione(parziale,maxY,maxH,self._listEvents)


        pass
    def ricorsione(self, parziale, maxY, maxH, pos):

        # TO FILL
        a=False
        maxY=int(maxY)
        maxH=int(maxH)


        #terminale
        if len(pos)==0:
            print("*")
            #CONTEGGIO CLIENTI
            conto = self.calcola_persone(parziale)

            if conto > self.max_persone:
                self.max_persone=conto
                self._solBest=copy.deepcopy(parziale)

            a=""
            for i in parziale:
                a+= str(i._id)+" - "
            print(a)

        else:

            for elem in pos:

                a=False
                #VINCOLI
                somma = ((elem._date_event_finished-elem._date_event_began).total_seconds())/3600
                for i in range(len(parziale)):
                    somma += ((parziale[i]._date_event_finished - parziale[i]._date_event_began).total_seconds())/3600 # MANCANO ORE

                if parziale==[] or ( (elem._date_event_finished.year - parziale[0]._date_event_began.year) < maxY  and somma < maxH):

                    for i in parziale:
                        if i._id == elem._id:
                            a=True


                    if not a:
                        parziale.append(elem)
                        parziale= sorted(parziale, key= lambda evento: evento._date_event_began)
                        rimanenti=copy.deepcopy(pos)
                        rimanenti.remove(elem)
                        self.ricorsione(parziale, maxY, maxH, rimanenti)
                        parziale.pop()


    def calcola_persone(self,parziale):
        conto=0
        for i in range(len(parziale)):
            conto+= parziale[i]._customers_affected
        return conto



    def loadEvents(self, nerc):
        a=DAO.getAllEvents(nerc)
        self._listEvents = a
        i=0

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()



    @property
    def listNerc(self):
        return self._listNerc

