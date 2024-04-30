import copy

from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
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

        #terminale
        if len(pos)==0:
            print("*")
            #CONTEGGIO CLIENTI
            self._solBest=copy.deepcopy(parziale)

        else:

            for elem in pos:

                somma = elem._date_event_finished-elem._date_event_began
                for i in range(len(parziale)):
                    somma += (parziale[i]._date_event_finished - parziale[i]._date_event_began)  # MANCANO ORE

                if parziale==[] or (elem._date_event_finished - parziale[0]._date_event_began < maxY  and somma < maxH):
                    parziale.append(elem)
                    rimanenti=copy.deepcopy(pos)
                    rimanenti.remove(elem)
                    self.ricorsione(parziale, maxY, maxH, rimanenti)
                    parziale.pop()



    def loadEvents(self, nerc):
        a=DAO.getAllEvents(nerc)
        self._listEvents = a
        i=0

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()



    @property
    def listNerc(self):
        return self._listNerc