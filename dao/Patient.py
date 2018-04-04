class PatientDAO:
    def __init__(self):  # Generates hardwired parameters by default on PatientDAO initialization
        P1 = ['P00000001','5557778888', 'Juan', 'Del Barrio Rivera', '25/Dec/1980','Male',7879876543, True, 'Ejemplo2@gmail.com', 'fvsfgstg68904']
        P2 = ['P00000002','5557775431', 'Miguel', 'Rosario Campos', '04/Jan/1975','Male',7879874137, False, 'Ejemplo3@gmail.com', 'fsefsdfv54455']
        P3 = ['P00000003','5553465431', 'Margarita', 'Rivera Rodriguez', '21/Mar/1964','Female',9399875630, True, 'Ejemplo4@gmail.com', 'fse4rvsfvs72']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)

    def getAllPatient(self):
        return self.data

    def getPatientByID(self,pid):
        result = []
        for r in self.data:
            if pid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result