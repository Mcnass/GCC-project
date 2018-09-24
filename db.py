from login import *


class DB(CL):  # Data Base attributaire
    def __init__(self):
        CL.__init__(self)
    
    def init_DBa (self):  # Init DB attributzire values
        global ct
        ct = Toplevel ()
        ct.geometry('410x445')
        ct.iconbitmap("bin\esri.ico")
        ct.title('Connexion à PythonDb') #rajouter le nom de la BDD
        ct['bg'] = 'light blue'
        
        ct.font = font.Font(family='Arial', size= 8, weight='bold')
                                  ##################### widgets   #########################
        ct.photo = PhotoImage(file='logo_final.png')
        ct_label_photo = Label(ct, image=ct.photo).pack()
        Label(ct, text= "Ajouter une table d'attributs", fg='black', bg='light blue', font=ct.font).place(x=10, y=100)
                                              ###### widgets inclus dans notre labelframe  #####
        ct.cadre = LabelFrame(ct, width=350,  height=270, bg='light blue').place(x=30, y=125)
        cadre_nomtable = Label(ct, text="Nom de la table :", fg='black', bg='light blue').place(x=55, y=133)
        varnomtable=StringVar()
        cadre_indicqnom = Entry(ct, textvariable = varnomtable, width =28).place(x=173, y=135)
        
        cadre_projection = Label(ct, text="Projection :", fg='black', bg='light blue').place(x=55, y=164)
        varprojection=StringVar()
        varprojection.set('<Aucune>')
        cadre_projection = Entry(ct, textvariable = varprojection, state=DISABLED, width =28).place(x=173, y=166)

        cadre_geometry = Label(ct, text="Type de géométrie :", fg='black', bg='light blue').place(x=55, y=197)
        liste_geom = [1, 2, 3, 4, 5]
        cadre_indicenom = Spinbox(ct, from_= liste_geom[0], to= liste_geom[4], width =27).place(x=173, y=199)

        cadre_geometry = Label(ct, text="Schéma :", fg='black', bg='light blue').place(x=55, y=230)
        vargeometry=StringVar()
        vargeometry.set('public')
        cadre_indicenom = Entry(ct, textvariable = vargeometry, width =28).place(x=173, y=232)

        ct.cadre2 =  LabelFrame(ct, width=290,  height=110, bg='light blue').place(x=55, y=258)
        
        ct.photo_button = PhotoImage(file='plus.png')
        Button(ct, image=ct.photo_button, command=self.ajout_table_attribut).place(x=55, y=370)

    def ajout_table_attribut(self):
        act = Toplevel ()
        act.geometry('265x250')
        act.iconbitmap("bin\esri.ico")
        act.title("Ajout d'un champ")
        act.group(ct)
        act['bg'] = 'light blue'
        act.font = font.Font(family='Arial', size= 8)
        
        nomchamp = Label(act, text="Nom du champ ", fg='black', bg='light blue', font=act.font).place(x=22, y=30)
        varnomchamp=StringVar()
        indicnom = Entry(act, textvariable = varnomchamp, width =20).place(x=110, y=30)

        typechamp = Label(act, text="Type ", fg='black', bg='light blue', font=act.font).place(x=22, y=65)
        vartypechamp=StringVar()
        indictype = Entry(act, textvariable = vartypechamp, width =20).place(x=110, y=65)

        longueurchamp = Label(act, text="Longueur ", fg='black', bg='light blue', font=act.font).place(x=22, y=100)
        varlongueurchamp=IntVar()
        varlongueurchamp.set(50)
        indictype = Entry(act, textvariable = varlongueurchamp, width =20).place(x=110, y=100)

        lienchamp = Checkbutton(act, text="Générer un lien cliquable ", fg='black', bg='light blue', font=act.font).place(x=22, y=136)

        texteclicchamp = Label(act, text="Texte cliquable ", fg='black', bg='light blue', font=act.font).place(x=22, y=175)
        vartexteclicchamp=StringVar()
        indictexteclic = Entry(act, textvariable = vartexteclicchamp, width =20).place(x=110, y=175)
        
        
        """Label(cl, text= "Saisissez les paramètres de connexion", fg='black', bg='light blue').place(x=1, y=15)

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
        
        Button(cl, text="Tester", command=self.Test_Cl).place(x=178, y=280) #self.ok_cl command
        Button(cl, text="Annuler", command=quit).place(x=238, y=280) #self.ok_cl command
        cl.mainloop()
    def Test_Cl(self):
        user = s1.get()
        password = s2.get()
        host = s3.get()
        port = s4.get()
        bdd = s5.get()
        db ='pq://%s:%s@%s:%s/%s' %(user, password, host, port, bdd)
        try:
            conn = postgresql.open(db)
            showinfo ('Infos connnexion', 'Connexion réussie')
            cl.destroy()
        except Exception:
            print(db)
            print ('echec de connexion')
            showerror("Infos connnexion", 'Echec de connexion! Veuillez vérifier les paramètres')"""
            
#root= DB()
#root = Tk()
#a = Button (text= "Connexion", command = CL().Cl).pack()
#b = Button (text= "afficher", command = CL().Test_Cl).pack()
#root.init_DBa()
