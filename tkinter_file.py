import customtkinter as ctk
import tkinter_function as tkf
import FSM_Function as fsm
from PIL import Image, ImageTk

window = ctk.CTk()


# Setting theme and color
window.configure(fg_color="#FFFFFF")

#title
window.title("Textual Editor")


#resolution
window.geometry("1920x1080")

#background color
#on ecrit le texte


# on creer la barre de menu tout en haut d'une hauteur de 30px
barre_navigation = ctk.CTkFrame(window,  height=500,corner_radius=50)
# on place la barre de menu en haut de la fenetre et on choisit de la remplir horizontalement
barre_navigation.pack(side='top', fill='x',padx=15,pady=15)
#on creer une deuxieme barre de menu en rouge pour la différencier pour les sous-choix

#on creer une deuxieme barre de menu en rouge pour la différencier pour les sous-choix
barre_navigation_trois = ctk.CTkFrame(window,  height=30,corner_radius=50)
# on place la barre de menu en haut de la fenetre et on choisit de la remplir horizontalement
barre_navigation_trois.pack(side='top', fill='x',padx=15,pady=15)

barre_navigation_bis = ctk.CTkFrame(window,  height=30,corner_radius=50)
# on place la barre de menu en haut de la fenetre et on choisit de la remplir horizontalement
barre_navigation_bis.pack(side='top', fill='x',padx=15,pady=15)


# on place un boutton dans la barre de menu
bouton = ctk.CTkButton(barre_navigation,corner_radius=35, text='Modifier un AEF', command=tkf.Button_Modifier_AEF)
bouton.pack(side=ctk.LEFT, padx=10)

bouton = ctk.CTkButton(barre_navigation,corner_radius=35, text='Liste Etat', command=tkf.Button_Liste_AEF)
bouton.pack(side=ctk.LEFT, padx=10)

bouton = ctk.CTkButton(barre_navigation,corner_radius=35, text='Supprimer un AEF', command=tkf.Button_Supprimer_AEF)
bouton.pack(side=ctk.LEFT, padx=10)


bouton = ctk.CTkButton(barre_navigation,corner_radius=35, text='Verifier un AEF', command=tkf.Button_Verifier_AEF)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation,corner_radius=35, text='Actualiser AEF', command=tkf.Button_Actualiser_AEF)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Rendre Complete', command=tkf.Button_Make_Complete)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Rendre Determinist', command=tkf.Button_Make_Determinist)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Complement', command=tkf.Button_Complement)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Mirror', command=tkf.Button_Mirror)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Product', command=tkf.Button_Product)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Concatenation', command=tkf.Button_Concatenation)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='RecognWord', command=tkf.Button_RecognWord)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Excise', command=tkf.Button_Excise)
bouton.pack(side=ctk.LEFT, padx=10)
bouton = ctk.CTkButton(barre_navigation_trois,corner_radius=35, text='Minimize', command=tkf.Button_Minimize)
bouton.pack(side=ctk.LEFT, padx=10)


bouton = ctk.CTkButton(barre_navigation, corner_radius=35,text='Exporter un AEF', command=tkf.Button_Exporter_AEF)
bouton.pack(side=ctk.RIGHT, padx=10)

bouton = ctk.CTkButton(barre_navigation,corner_radius=35, text='Importer un AEF', command=tkf.Button_Importer_AEF)
bouton.pack(side=ctk.RIGHT, padx=10)






window.mainloop()

