from django.db import models

# Create your models here.


class Specialite(models.Model):
    Specialite = models.CharField(max_length = 200 , null=True)
    




class Medecin(models.Model):
    Nom = models.CharField(max_length = 100 , null=True)
    Prenom = models.CharField(max_length = 100 , null=True)
    Adresse = models.CharField(max_length = 200 , null=True)
    Ville = models.CharField(max_length = 100 , null=True)
    Pays = models.CharField(max_length = 100 , null=True)
    Tel1 = models.CharField(max_length = 50 , null=True)
    Tel2 = models.CharField(max_length = 50 , null=True)
    Fax = models.CharField(max_length = 50 , null=True)
    Email = models.CharField(max_length = 200 , null=True)
    IDSpecialite = models.ForeignKey(Specialite , null=True , on_delete=models.SET_NULL)
    ParDefaut = models.BooleanField(null=True)
    INPE = models.CharField(max_length = 50 , null=True)
    Photo = models.CharField(max_length = 200 , null=True)





class Patient(models.Model):
    #Civilite
    Nom = models.CharField(max_length = 100 , null=True)
    Prenom = models.CharField(max_length = 100 , null=True)
    DateNaissance = models.DateTimeField(null=True)
    Poids = models.FloatField(null=True)
    Taille = models.FloatField(null=True)
    Adresse = models.CharField(max_length = 200 , null=True)
    Ville = models.CharField(max_length = 100 , null=True)
    Pays = models.CharField(max_length = 100 , null=True)
    CodePostal = models.CharField(max_length = 100 , null=True)
    Tel1 = models.CharField(max_length = 50 , null=True)
    Tel2 = models.CharField(max_length = 50 , null=True)
    # Sexe
    # GrpSanguin
    Mutuelle = models.CharField(max_length = 100 , null=True)
    Photo = models.CharField(max_length = 200 , null=True)
    DateCreation = models.DateTimeField(auto_now_add=True , null=True)
    DateModification = models.DateTimeField(auto_now_add=True , null=True)



class RDV(models.Model):
    DateDebut = models.DateTimeField(null=True)
    DateFin = models.DateTimeField(null=True)
    Etat = models.BooleanField(null=True)
    IDPatient = models.ForeignKey(Patient , null=True , on_delete=models.SET_NULL)
    IDMedecin = models.ForeignKey(Medecin , null=True , on_delete=models.SET_NULL)





class TypeConsultation(models.Model):
    TypeConsultation = models.CharField(max_length = 100 , null=True)
    




class Consultation(models.Model):
    DateConsultation = models.DateTimeField(auto_now_add=True , null=True)
    MontantConsultation = models.FloatField(null=True)
    Gratuit = models.BooleanField()
    IDTypeConsultation = models.ForeignKey(TypeConsultation , null=True , on_delete=models.SET_NULL)
    IDPatient = models.ForeignKey(Patient , null=True , on_delete=models.SET_NULL)
    DetailConsultation = models.CharField(max_length = 100 , null=True)
    IDMedcin =  models.ForeignKey(Medecin , null=True , on_delete=models.SET_NULL)
    Regle = models.BooleanField(null=True)
    RestantDu = models.FloatField(null=True)
    DateCreation = models.DateTimeField(auto_now_add=True , null=True)
    DateModification = models.DateTimeField(auto_now_add=True , null=True)
    



class TypeActe(models.Model):
    TypeActe = models.CharField(max_length = 500 , null=True)
    CodeActe = models.CharField(max_length = 50 , null=True)
    



class Acte(models.Model):
    DateActe = models.CharField(max_length = 500 , null=True)
    CodeActe = models.CharField(max_length = 50 , null=True)
    IDPatient =  models.ForeignKey(Patient , null=True , on_delete=models.SET_NULL)
    RapportActe = models.CharField(max_length = 500 , null=True)
    MontantActe = models.FloatField(max_length = 500 , null=True)
    Gratuit = models.BooleanField()
    IDTypeActe =  models.ForeignKey(TypeActe , null=True , on_delete=models.SET_NULL)
    IDMedecin =  models.ForeignKey(Medecin , null=True , on_delete=models.SET_NULL)
    DateCreation = models.DateTimeField(auto_now_add=True , null=True)
    DateModification = models.DateTimeField(auto_now_add=True , null=True)





class Laboratoire(models.Model):
    Laboratoire = models.CharField(max_length = 50 , null=True)
    Adresse = models.CharField(max_length = 200 , null=True)
    Ville = models.CharField(max_length = 100 , null=True)
    Pays = models.CharField(max_length = 100 , null=True)
    CodePostal = models.CharField(max_length = 50 , null=True)
    Tel1 = models.CharField(max_length = 50 , null=True)
    Tel2 = models.CharField(max_length = 50 , null=True)
    Fax = models.CharField(max_length = 50 , null=True)
    Email = models.CharField(max_length = 200 , null=True)
    NomContact = models.CharField(max_length = 200 , null=True)
    



class TypeAnalyse(models.Model):
    TypeAnalyse = models.CharField(max_length = 200 , null=True)
    



class AnalyseMedical(models.Model):
    DateAnalyse = models.DateTimeField( null=True)
    LibelleAnalyse = models.CharField(max_length = 200 , null=True)
    IDConsultation =  models.ForeignKey(Consultation , null=True , on_delete=models.SET_NULL)
    IDLaboratoire =  models.ForeignKey(Laboratoire , null=True , on_delete=models.SET_NULL)
    DateCreation = models.DateTimeField(auto_now_add=True , null=True)
    DateModification = models.DateTimeField(auto_now_add=True , null=True)
    



class DetailAnalyseMedical(models.Model):
    IDAnalyseMedical =  models.ForeignKey(AnalyseMedical , null=True , on_delete=models.SET_NULL)
    IDTypeAnalyse =  models.ForeignKey(Consultation , null=True , on_delete=models.SET_NULL)
    ResultatAnalyse = models.CharField(max_length = 200 , null=True)
    Positif = models.BooleanField()




class Antecedent(models.Model):
    Antecedent = models.CharField(max_length = 500 , null=True)
    Observation = models.CharField(max_length = 500 , null=True)
    CodeAntecedent = models.CharField(max_length = 50 , null=True)
    



class AntecedentPatient(models.Model):
    IDAntecedent  =  models.ForeignKey(Antecedent , null=True , on_delete=models.SET_NULL)
    Observation = models.CharField(max_length = 500 , null=True)
    IDPatient  =  models.ForeignKey(Patient , null=True , on_delete=models.SET_NULL)



class Document(models.Model):
    LibelleDocument = models.CharField(max_length = 200 , null=True)
    Document = models.CharField(max_length = 200 , null=True)
    IDPatient  =  models.ForeignKey(Patient , null=True , on_delete=models.SET_NULL)



class TypeDocumentFourni(models.Model):
    TypeDocumentFourni = models.CharField(max_length = 200 , null=True)
    Contenue = models.CharField(max_length = 500 , null=True)






class DocumentFourni(models.Model):
    IDTypeDocumentFourni = models.ForeignKey(TypeDocumentFourni , null=True , on_delete=models.SET_NULL)
    IDPatient  =  models.ForeignKey(Patient , null=True , on_delete=models.SET_NULL)
    Contenue = models.CharField(max_length = 500 , null=True)
    DateDocument = models.DateTimeField(auto_now_add=True , null=True)

    



class Prescription(models.Model):
    DatePrescription = models.DateTimeField( null=True)
    IDConsultation =  models.ForeignKey(Consultation , null=True , on_delete=models.SET_NULL)
    Observation = models.CharField(max_length = 500 , null=True)
    DateCreation = models.DateTimeField(auto_now_add=True , null=True)
    DateModification = models.DateTimeField(auto_now_add=True , null=True)
    




class Medicament(models.Model):
    Designation = models.CharField(max_length = 200 , null=True)
    CodeBarre = models.CharField(max_length = 50 , null=True)
    Tableau = models.BooleanField()




class PrescriptionMedicament(models.Model):
    IDPrescription =  models.ForeignKey(Prescription , null=True , on_delete=models.SET_NULL)
    IDMedicament =  models.ForeignKey(Medicament , null=True , on_delete=models.SET_NULL)
    Posologie = models.CharField(max_length = 200 , null=True)
