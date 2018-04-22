class MedicalRecordDAO:
    def __init__(self):  # Generates hardwired parameters by default on MedicalRecordDAO initialization
        P1 = ['P00000001']
        P2 = ['P00000002']
        P3 = ['P00000003']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllMedicalRecord(self):
        return self.data

    def getMedicalRecordByID(self,rn):
        result = []
        for r in self.data:
            if rn == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result