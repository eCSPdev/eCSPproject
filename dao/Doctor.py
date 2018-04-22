class DoctorDAO:
    def __init__(self):  # Generates hardwired parameters by default on DoctorDAO initialization
        P1 = ['Doctor1', '5555555', 'Ismael', 'Segarra', 'Clinica de salud y Prevencion',7873456789, True, 'Ejemplo@gmail.com', 'fgbs577drg']
        self.data = []
        self.data.append(P1)

    def getAllDoctor(self):
        return self.data

    def getDoctorByID(self,did):
        result = []
        for r in self.data:
            if did == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result