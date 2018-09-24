from tkinter import*
from tkinter import messagebox, colorchooser, filedialog
from tkinter.messagebox import *
import postgresql

class CL:
    resultat = []
    def Cl (self):
        global cl
        cl = Toplevel ()
        cl.geometry('315x320')
        cl.iconbitmap("bin\esri.ico")
        cl.title('Connexion locale au serveur')
        cl['bg'] = 'light blue'
        Label(cl, text= "Saisissez les paramètres de connexion", fg='black', bg='light blue').place(x=1, y=15)

        label_user = Label(cl, text="Nom d'utilisateur :", fg='black', bg='light blue').place(x=10, y=55)
        global saisie1
        saisie1 = Entry(cl, width =26)
        saisie1.place(x=130, y=55)

        label_password = Label(cl, text="Mot de passe :", fg='black', bg='light blue').place(x=10, y=100)
        global saisie2
        saisie2 = Entry(cl, width =26)
        saisie2.place(x=130, y=100)

        abel_host = Label(cl, text="Hôte :", fg='black', bg='light blue').place(x=10, y=145)
        global saisie3
        saisie3 = Entry(cl, width =26)
        saisie3.place(x=130, y=145)

        label_port = Label(cl, text="Port :", fg='black', bg='light blue').place(x=10, y=190)
        global saisie4
        saisie4 = Entry(cl, width =26)
        saisie4.place(x=130, y=190)

        label_bdd = Label(cl, text="Base de donnée :", fg='black', bg='light blue').place(x=10, y=235)
        global saisie5
        saisie5 = Entry(cl, width =26)
        saisie5.place(x=130, y=235)
        
        Button(cl, text="Tester", command=self.Test_Cl).place(x=178, y=280) #self.ok_cl command
        Button(cl, text="Annuler", command=quit).place(x=238, y=280) #self.ok_cl command
        cl.mainloop()
    def Test_Cl(self):
        CL.resultat.append(saisie1.get () )
        CL.resultat.append ( saisie2.get () )
        CL.resultat.append ( saisie3.get () )
        CL.resultat.append ( saisie4.get () )
        CL.resultat.append ( saisie5.get () )
        user = CL.resultat[0]
        password = CL.resultat[1]
        host = CL.resultat[2]
        port = CL.resultat[3]
        bdd = CL.resultat[4]
        db ='pq://%s:%s@%s:%s/%s' %(user, password, host, port, bdd)
        try:
            conn = postgresql.open(db)
            showinfo ('Infos connnexion', 'Connexion réussie')
        except Exception:
            showerror("Infos connnexion", 'Echec de connexion! Veuillez vérifier les paramètres')
            print (db)
            cl.destroy()
            return self.Cl()
            
root = Tk()
a = Button (text= "Connexion", command = CL().Cl).pack()
b = Button (text= "afficher", command = CL().Test_Cl).pack()
root.mainloop()
