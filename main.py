######################################
# Auteur : SAUTRON Dimitri
# Created : 04/08/2023
# Version : 1.0
# Description :
#
######################################
###################################################

import os
import platform
OS=platform.system()

if OS == str("Windows"):

    #Importation de la librairie
    import tkinter
    from tkinter import *
    from tkinter.filedialog import *
    # Pour initialiser tkinter, nous devons créer un widget root Tk
    # import fonction

    root = Tk()
    # FCT = fonction()

    # frame 1
    Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
    Frame1.pack(padx=20, pady=20)

    label = Label(Frame1, text="Un message")
    label.grid(column=0, row=1)

    button = Button(Frame1, text="Open Directory", command=root.quit)
    button.grid(column=2, row=1)

    text = Entry(Frame1,textvariable="message", width=50)
    text.grid(column=1, row=1)

    root.title("Brain Learning")
    # root.iconbitmap('E:\\Project\\Nutrition\\Nutri.ico')
    # root.iconbitmap('E:\\Project\\Nutrition\\nutrition.ico')
    # root.iconbitmap("C:\\Users\\dimitri.sautron\\Projet\\brain-learning\\icon.ico")
    # width x height
    root.geometry("700x700")

    # Ajout d'une barre de menu
    menubar = Menu(root)
    root.config(menu=menubar)

    # Menu Fichier
    menufichier = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Fichier", menu=menufichier)
    menufichier.add_command(label="Jeux")
    menufichier.add_command(label="Favoris")
    menufichier.add_separator()
    menufichier.add_command(label="Préférences")
    menufichier.add_command(label="Quitter", command=root.destroy)
    # Menu Fichier
    menufichier = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Fichier", menu=menufichier)
    menufichier.add_command(label="Jeux")
    menufichier.add_command(label="Favoris")
    menufichier.add_separator()
    menufichier.add_command(label="Préférences")
    menufichier.add_command(label="Quitter", command=root.destroy)

    # Menu Edition
    menuedition = Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Compte", menu=menuedition)
    menuedition.add_command(label="Connection")
    menuedition.add_command(label="Paramètre")
    menuedition.add_command(label="Paramètre en ligne")
    menuedition.add_command(label="Deconnection")

    #menuedition.add_separator()

    #Menu Graphique
    menugraphique = Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Configuration", menu=menugraphique)
    menugraphique.add_command(label="Couleurs")
    menugraphique.add_command(label="Mode d'affichage")
    menugraphique.add_command(label="Taille de l'application")
    menugraphique.add_command(label="Accessibilité")
    menugraphique.add_command(label="Enregistrer")
    menugraphique.add_command(label="Accessibilité")


    #Menu Graphique
    menuson = Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Son", menu=menuson)
    menuson.add_command(label="Niveau Sonore")
    menuson.add_command(label="Carte audio")
    menuson.add_command(label="Egaliseurs")


    menuimportexport = Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "Import_Export", menu=menuimportexport)
    menuimportexport.add_command(label="Importer")
    menuimportexport.add_command(label="Exporter")
    menuimportexport.add_command(label="Comparaison")


    # Menu Help
    menuhelp = Menu(menubar,tearoff=0)
    menubar.add_cascade(label= "A propos", menu=menuhelp)
    menuhelp.add_command(label="Présentation")
    menuhelp.add_command(label="FAQ")
    menuhelp.add_command(label="Contact")

    #Fin de la configuration de l'interface.
    root.mainloop()

elif OS == str("Linux"):
    LocateFile ="~/"
    Emplacement=input('Entrez la localisation des fichiers a renommer : ')
else:
    OSError
