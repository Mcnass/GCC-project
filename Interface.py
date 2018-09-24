import time
from login import *

class Fonction_interface: # class interface (fontion principale de l'interface)
    def couleur(self): # gestion des couleurs de fond (#renommer preference)
        global color
        color = colorchooser.askcolor(); self['bg'] = color[1]
        if self['bg'] == color[1]:
            self.label_pseudo == Label(root, text="Identifiant :", fg='black', bg=root['bg']).place(x=50, y=215)
            self.label_md5 == Label(root, text ="Mot de passe :", fg='black', bg=root['bg']).place(x=50, y=245)
            self.case_md5 == Checkbutton(root, text ="enregistrer le mot de passe", variable=self.var3, bg=root['bg']).place(x=145, y=270)
            self.label_accueil1 == Label(root, text= "Bienvenue dans l'utilitaire de gestion de connexion aux bases de données.", fg='black', bg=root['bg']).place(x=5, y=115)
            self.label_accueil2 == Label(root, text= "Une authentification est requise", fg='black', bg=root['bg']).place(x=5, y=135)
    def default_couleur(self):
        root['bg'] = 'light blue'
        self.label_pseudo == Label(root, text="Identifiant :", fg='black', bg=root['bg']).place(x=50, y=215)
        self.label_md5 == Label(root, text ="Mot de passe :", fg='black', bg=root['bg']).place(x=50, y=245)
        self.case_md5 == Checkbutton(root, text ="enregistrer le mot de passe", variable=self.var3, bg=root['bg']).place(x=145, y=270)
        self.label_accueil1 == Label(root, text= "Bienvenue dans l'utilitaire de gestion de connexion aux bases de données.", fg='black', bg=root['bg']).place(x=5, y=115)
        self.label_accueil2 == Label(root, text= "Une authentification est requise", fg='black', bg=root['bg']).place(x=5, y=135)
    def files(self):   # ouvrir un fichier (#ajouter le type de fichier à ouvrir)
        file = filedialog.askopenfile()
    def directory(self):   # ouvrir un repertoire
        file = filedialog.askdirectory()
    def save_files(self):   # enrgistrer un fichier
        file = filedialog.asksaveasfile()
    def ok_authentification(self):   # gestionnaire d'authentification (#ok!!mais definir un dictionnaire\)
        root = self.var1.get()
        md5 = self.var2.get()
        if root =="admin" and md5 =="refgcc":
            self.label_accueil1["text"] = "Vous vous connectez comme super administrateur"
            self.label_accueil2["text"] = "Vous accéder à l'ensemble des fonctionnalités de l'application"
            showinfo("Authentification infos", "Authentification réussie")
            self.menu.entryconfig(1, state=NORMAL)
            self.menu.entryconfig(2, state=NORMAL)
            self.menu.entryconfig(3, state=NORMAL)
            self.menu.entryconfig(4, state=NORMAL)
            self.menu.entryconfig(5, state=ACTIVE)
            self.menu.entryconfig(6, state=ACTIVE)
            self.sousmenu2.entryconfig(0, state=ACTIVE)
            self.sousmenu2.entryconfig(2, state=DISABLED)
        elif root =="ref_caro" and md5 =="refcaro":
            self.label_accueil1["text"] = "Vous vous connectez en tant que référent de la CARO"
            self.label_accueil2["text"] = "Vos droits d'accès à l'application sont spécifiés dans le menu"
            showinfo("Authentification infos", "Authentification réussie")
            self.menu.entryconfig(1, state=NORMAL)
            self.menu.entryconfig(2, state=NORMAL)
            self.menu.entryconfig(3, state=NORMAL)
            self.menu.entryconfig(4, state=NORMAL)
            self.menu.entryconfig(5, state=ACTIVE)
            self.menu.entryconfig(6, state=ACTIVE)
            self.sousmenu2.entryconfig(0, state=DISABLED)
            self.sousmenu2.entryconfig(2, state=ACTIVE)
        elif root =="ref_cdchs" and md5 =="refcdchs":
            self.label_accueil1["text"] = "Vous vous connectez en tant que référent de la CDCHS"
            self.label_accueil2["text"] = "Vos droits d'accès à l'application sont spécifiés dans le menu"
            showinfo("Authentification infos", "Authentification réussie")
            self.menu.entryconfig(1, state=NORMAL)
            self.menu.entryconfig(2, state=NORMAL)
            self.menu.entryconfig(3, state=NORMAL)
            self.menu.entryconfig(4, state=NORMAL)
            self.menu.entryconfig(5, state=ACTIVE)
            self.menu.entryconfig(6, state=ACTIVE)
            self.sousmenu2.entryconfig(0, state=DISABLED)
            self.sousmenu2.entryconfig(2, state=ACTIVE)
        else:
            self.label_accueil1["text"] = "Bienvenue dans l'utilitaire de gestion de connexion aux bases de données."
            self.label_accueil2["text"] = "Une authentification est requise"
            showerror("Authentification infos", "Echec de l'authentification")
            self.menu.entryconfig(1, state=DISABLED)
            self.menu.entryconfig(2, state=DISABLED)
            self.menu.entryconfig(3, state=DISABLED)
            self.menu.entryconfig(4, state=DISABLED)
            self.menu.entryconfig(5, state=DISABLED)
            self.menu.entryconfig(6, state=DISABLED)
    def maj(self):
        self.heure.set(time.strftime('%H:%M:%S'))
        self.after(1000, self.maj)

global Interface
class Interface(Tk, Fonction_interface, CL):  # Notre interface principale rajouter tk()
    def __init__(self):
        Tk.__init__(self)
        CL.__init__(self)
        Fonction_interface.__init__(self)
        self.geometry('410x445')
        self.iconbitmap("bin\esri.ico")
        self.title('Gestionnaire de connexions clients')
        self['bg'] = 'light blue'
                                                        ###########  Widgets interface ###########
        self.photo = PhotoImage(file='logo_final.png')
        self.label_photo = Label(self, image=self.photo).pack()
        self.label_accueil1 = Label(self, text= "Bienvenue dans l'utilitaire de gestion de connexion aux bases de données.", fg='black', bg='light blue')
        self.label_accueil1.place(x=5, y=115)
        self.label_accueil2 = Label(self, text= "Une authentification est requise", fg='black', bg='light blue')
        self.label_accueil2.place(x=5, y=135)
        self.label_pseudo = Label(self, text="Identifiant :", fg='black', bg='light blue').place(x=50, y=215)
        self.var1=StringVar()
        self.var1.set('root')
        self.ligne_pseudo = Entry(self, textvariable = self.var1, width =26).place(x=150, y=215)
        self.label_md5 = Label(self, text ="Mot de passe :", fg='black', bg='light blue').place(x=50, y=245)
        self.var2 = StringVar()
        self.var2.set('*********')
        self.ligne_md5 = Entry(self, textvariable = self.var2, width = 26).place(x=150, y=245)
        self.var3= IntVar()
        self.case_md5 = Checkbutton(self, text ="enregistrer le mot de passe", variable=self.var3, bg='light blue').place(x=145, y=270)
        self.bouton_ok = Button(self, text="  OK   ", width=6, command=self.ok_authentification).place(x=195, y=340)
        self.bouton_annuler = Button(self, text="Annuler", width=6, command=quit).place(x=255, y=340)
        self.heure = StringVar()
        self.label_heure = Label(self,textvariable=self.heure, bg='light blue').place(x=355,y=405)
        self.maj()
        ################################ Menu du script  ################################
        self.menu = Menu(self)
        self.sousmenu1 = Menu(self.menu, activebackground='grey', tearoff=0)
        self.sousmenu2 = Menu(self.menu, activebackground='grey', tearoff=0)
        self.sousmenu3 = Menu(self.menu, activebackground='grey', tearoff=0)
        self.sousmenu4 = Menu(self.menu, activebackground='grey', tearoff=0)
        self.sousmenu5 = Menu(self.menu, activebackground='grey', tearoff=0)
        self.sousmenu6 = Menu(self.menu, activebackground='grey', tearoff=0)
        self.menu.add_cascade(label='Fichier', state=DISABLED, menu=self.sousmenu1,)
        self.menu.add_cascade(label='Connexion', state=DISABLED, menu=self.sousmenu2)
        self.menu.add_cascade(label='Affichage', state=DISABLED, menu=self.sousmenu3)
        self.menu.add_cascade(label='Base de donnees', state=DISABLED, menu=self.sousmenu4)
        self.menu.add_cascade(label='Parametres', state=DISABLED, menu=self.sousmenu5)
        self.menu.add_cascade(label='Aide', state=DISABLED, menu=self.sousmenu6)
                                                         ###########  sous menu 1 ###########
        self.sousmenu1.add_command(label='Nouveau                               Ctrl+N',  command=quit)
        self.sousmenu1.add_command(label='Ouvrir...                                 Ctrl+O',  command=self.files) #accelerator="Ctrl-O", underline=2 permet de faire la même chose
        self.optionmenu1 = Menu(self.sousmenu1, activebackground='grey', tearoff=0) # initialisation de l'objet
        self.sousmenu1.add_cascade(label='Fichiers recents...',  menu=self.optionmenu1)
        self.optionmenu1.add_command(label="C:Users_Nassim Sadikou_Desktop_PYTHON_Dept prog")
        self.optionmenu1.add_command(label="C:Users_Nassim Sadikou_Desktop_PYTHON_Dept prog__pycache__")
        self.sousmenu1.add_command(label='Enregistrer                             Ctrl+S', command=self.directory)
        self.sousmenu1.add_command(label='Enregistrer sous         Ctrl+Shift+S', command=self.save_files)
        self.sousmenu1.add_separator()
        self.sousmenu1.add_command(label='Fermer                                 Ctrl+F4', command=self.destroy)
        self.sousmenu1.add_command(label='Quitter                                  Ctrl+Q', command=self.destroy)
                                                                                     ##raccourci clavier##
        self.sousmenu1.bind_all('<Control-n>', quit)
        self.sousmenu1.bind_all('<Control-o>', self.files)
        self.sousmenu1.bind_all('<Control-s>', self.directory)
        self.sousmenu1.bind_all('<Control-Shift-s>', self.save_files)
        self.sousmenu1.bind_all('<Control-F4>', quit)
        self.sousmenu1.bind_all('<Control-q>', self.destroy)
                                                       ###############  sous menu 2 ##############
        self.sousmenu2.add_command(label='Connexion locale', command=main_CoL)#CL().Cl)
        self.sousmenu2.add_separator()
        self.sousmenu2.add_command(label='Connexion distante', command=self.quit)
                                                     ##############  sous menu 3 ###############
        self.sousmenu3.add_command(label='Couleur de fond', command=self.couleur)
        self.sousmenu3.add_command(label='Couleur par defaut', command=self.default_couleur)
                                                   ###############  sous menu 4 ###############
        self.optionmenu4 = Menu(self.sousmenu4, activebackground='grey', tearoff=0)
        self.sousmenu4.add_cascade(label='Tables attributaires',  menu=self.optionmenu4)
        self.sousmenu4.add_cascade(label='Tables spatiales',  menu=self.optionmenu4)
        self.optionmenu4.add_command(label='Créer une table', command=main_init_DBa)#CL().init_DBa)
        self.optionmenu4.add_command(label='Modifier une table', command=self.quit)
        self.optionmenu4.add_command(label='Supprimer une table', command=self.quit)
        self.optionmenu4.add_command(label='Vider une table', command=self.quit)
        self.optionmenu4.add_command(label='Verifier la validité des métadonnées', command=self.quit)
        
        self.sousmenu4.add_command(label='Importer une couche', command=self.quit)
        self.sousmenu4.add_command(label='Exporter une couche', command=self.quit) 
                                                   ################  sous menu 5 ###############
        self.optionmenu5 = Menu(self.sousmenu5, activebackground='grey', tearoff=0)
        self.sousmenu5.add_command(label='Debogage', command=self.quit)
        self.sousmenu5.add_command(label="Editeur de requête", command=self.quit)
        self.sousmenu5.add_cascade(label="Script", menu=self.optionmenu5)
        self.optionmenu5.add_command(label='Script CREATE', command=self.quit)
        self.optionmenu5.add_command(label='Script INSERT', command=self.quit)
        self.optionmenu5.add_command(label='Script SELECT', command=self.quit)
        self.optionmenu5.add_command(label='Script DELETE', command=self.quit)
        self.sousmenu5.add_command(label="Se deconnecter", command=self.quit)
        self.sousmenu5.add_command(label="Se deconnecter du serveur", command=self.quit)
                                                  #################  sous menu 6 ##############
        self.sousmenu6.add_command(label='Aide', command=self.quit) 
        self.sousmenu6.add_command(label='Rapport de bug', command=self.quit)
        self.sousmenu6.add_command(label='A propos', command=self.quit)
                                                  ########### config #################
        self.config(menu = self.menu)
                                                            ###########  END ###########

#root = Interface()  # Lancement de root
#root.mainloop()
