class AssistantDAO:
    def __init__(self):  # Generates hardwired parameters by default on AssistantDAO initialization
        P1 = ['CC100', 'Coralis', 'Camacho', '7871234567',True, 'Coraliscamacho1@upr.edu', '872g73g92']
        P2 = ['LS101', 'Luis', 'Santiago', '7872345678', True, 'Luis.santiago56@upr.edu', '8afadvaz5q34']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)

    def getAllAssistant(self):
        return self.data

    def getAssistantByID(self,aid):
        result = []
        for r in self.data:
            if aid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result