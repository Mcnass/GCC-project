from tkinter import*
from tkinter import font
from tkinter import messagebox, colorchooser, filedialog
from tkinter.messagebox import *
import postgresql

class CL: # Local Connexion

    def Cl (self):   # Init CL values
        global cl
        cl = Toplevel ()
        cl.geometry('315x320')
        #cl.iconbitmap("bin\esri.ico")
        cl.title('Connexion locale au serveur')
        cl['bg'] = 'light blue'
        Label(cl, text= "Saisissez les paramètres de connexion", fg='black', bg='light blue').place(x=1, y=15)

        label_user = Label(cl, text="Nom d'utilisateur :", fg='black', bg='light blue').place(x=10, y=55)
        global s1
        s1 = StringVar()
        saisie1 = Entry(cl, textvariable=s1, width =26)
        saisie1.place(x=130, y=55)

        label_password = Label(cl, text="Mot de passe :", fg='black', bg='light blue').place(x=10, y=100)
        global s2
        s2 = StringVar()
        saisie2 = Entry(cl, textvariable=s2, width =26)
        saisie2.place(x=130, y=100)

        label_host = Label(cl, text="Hôte :", fg='black', bg='light blue').place(x=10, y=145)
        global s3
        s3 = StringVar()
        saisie3 = Entry(cl, textvariable=s3, width =26)
        saisie3.place(x=130, y=145)

        label_port = Label(cl, text="Port :", fg='black', bg='light blue').place(x=10, y=190)
        global s4
        s4 = IntVar()
        s4.set(5432)
        saisie4 = Entry(cl, textvariable=s4, width =26)
        saisie4.place(x=130, y=190)

        label_bdd = Label(cl, text="Base de donnée :", fg='black', bg='light blue').place(x=10, y=235)
        global s5
        s5 = StringVar()
        saisie5 = Entry(cl, textvariable=s5, width =26)
        saisie5.place(x=130, y=235)
        
        Button(cl, text="Tester", cursor="watch", command=self.Test_Cl).place(x=178, y=280) #self.ok_cl command
        Button(cl, text="Annuler", command=quit).place(x=238, y=280) #self.ok_cl command
        cl.mainloop()
    def Test_Cl(self):   # Test_Local Connexion (get values and test connexion)
        user = s1.get()
        password = s2.get()
        host = s3.get()
        port = s4.get()
        self.database = s5.get()
        db ='pq://%s:%s@%s:%s/%s' %(user, password, host, port, self.database)
        try:
            conn = postgresql.open(db)
            showinfo ('Infos connnexion', 'Connexion réussie')
            cl.destroy()
            print(db)
            label_conn = Label(self, textvariable="Vous êtes connecté", bg='light blue').place(x=355,y=385)
        except Exception:
            print(db)
            print ('echec de connexion')
            showerror("Infos connnexion", 'Echec de connexion! Veuillez vérifier les paramètres')
    #def __init__(self):
        #self.database =
            
#root = Tk()
#a = Button (text= "Connexion", command = CL().Cl).pack()
#b = Button (text= "afficher", command = CL().Test_Cl).pack()
#root.mainloop()
