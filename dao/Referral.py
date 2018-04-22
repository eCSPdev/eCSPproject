class ReferralDAO:
    def __init__(self):  # Generates hardwired parameters by default on AssistantDAO initialization
        P1 = ['P00000001','Prueba1','CN001', True, False, '29/jan/2018', '12:00pm']
        P2 = ['P00000001','Prueba2','CN002', False, True, '20/jan/2018', '8:50pm']
        P3 = ['P00000002','Prueba3', 'CN003', False, True, '21/jan/2018','10:00pm']
        P4 = ['P00000003','Prueba4', 'CN004', True, False, '20/jan/2018', '8:00pm']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

    def getAllReferral(self,rn):
        result = []
        for r in self.data:
            if rn == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getReferralByID(self,rn,rid):
        result = []
        for r in self.data:
            if rn == r[0]:
                if rid == r[1]:
                    result.append(r)
        if not result:
            return None
        else:
            return result