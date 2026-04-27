class patient:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    
    def afficher(self):
        print(f"Nom: {self.nom} | Age:{self.age}")
    
    def priorite(self):
        pass
    
    def __gt__(self,autre):
        if self.priorite()>autre.priorite():
            return True
        else:
            return False
    def __str__(self):
        return f'Nom: {self.nom} | Age:{self.age} | Type:{type(self).__name__}'
    def cout_Traitement(self):
        return 100 if(type(self).__name__==patientNormale) else(if type(self).__name__==patientNormale return 150 else return 200)

    def stats(patients):
        nbr_normale=0
        nbr_urgent=0
        nbr_vip=0
        cout_totale=0
        patient_plus_prioritaire=[]
        plus_prioritaire=patients[0]
        patientsResults={}
        for i in patients:
            if isinstance(i,patientNormale):
                nbr_normale+=1
            elif isinstance(i,patientUrgent):
                nbr_urgent+=1
            else:
                nbr_vip+=1
            cout_totale+=i.cout_Traitement()
            if plus_prioritaire.priorite()<i.priorite:
                plus_prioritaire=i

        for p in patients:
            if isinstance(p,type(plus_prioritaire)):
                patient_plus_prioritaire.append(p)
        #patient_plus_prioritaire=[p for p in patients if isinstance(p,type(plus_prioritaire))]

        patientsResults["Types des Patients"]={"nbr_normale":nbr_normale,"nbr_urgent":nbr_urgent,"nbr_vip":nbr_vip}
        patientsResults["cout Totale"]=cout_totale
        patientsResults["patients la plus prioritaire"]=patient_plus_prioritaire
    
class patientNormale(patient):
    pass
    def priorite(self):
        return 1
    
class patientUrgent(patient):
    pass
    def priorite(self):
        return 1
    
class patientVIP(patient):
    pass
    def priorite(self):
        return 1

def traiter_patient(patient):
    patient.afficher()
    patient.priorite()

l_patient=[patientUrgent("nom01",19),
            patientNormale("nom02",24),
            patientVIP("nom03",42),
            patientUrgent("nom04",14),]

for p in l_patient:
    traiter_patient(p)


            

