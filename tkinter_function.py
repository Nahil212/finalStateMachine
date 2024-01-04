import customtkinter as ctk
import FSM_Function as fsm
import tkinter_file
from PIL import Image, ImageTk
# ce fichier permet de faire le back end de l'interface graphique
# il permet de faire le lien entre les fonctions de FSM_Function.py et l'interface graphique

global image_label  
image_label = None
print("------------------------------------------------------")
def Generer_AEF_PNG(aef, window):
    global image_label
    print("on creer une image avec cette aef:")
    print(aef)
    fsm.generer_aef_png_modifie(aef)
    image = Image.open("aef.png")
    global photo
    photo = ImageTk.PhotoImage(image)

    if image_label is not None:
        image_label.destroy()

    image_label = ctk.CTkLabel(window, image=photo)
    image_label.image = photo  
    image_label.pack(pady=20)
    
def FenetreError(texte):
    popup = ctk.CTk()
    popup.wm_title("Error")
    label = ctk.CTkLabel(popup, text=texte)
    label.pack(side="top", fill="x", pady=10)
    B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
    B1.pack(pady=(10, 10))
    popup.mainloop()

def Button_Modifier_AEF():
     # on creer une nouvelle fenetre pour faire notre choix de saisie 
     # attention on peux appuyer dessus a l'infinie et ca recreer des nouveaux bouttons. a corriger

    global aef


    try:
   
        aef
    except NameError:

        aef = {}
    #on creer aef
    # on verifie que si aef n'est pas vide



    print(aef)
    #on verifie si les boutons existent déjà :

    global BoutonExiste
    try:
        BoutonExiste
    except NameError:
   
        BoutonExiste = True

        bouton_creer_etat = ctk.CTkButton(tkinter_file.barre_navigation_bis, text="Créer un état", command=Button_Creer_Etat)
        bouton_creer_etat.pack(side=ctk.LEFT, padx=10)

        bouton_supprimer_etat = ctk.CTkButton(tkinter_file.barre_navigation_bis, text="Supprimer un état", command=Button_Supprimer_Etat)
        bouton_supprimer_etat.pack(side=ctk.LEFT, padx=10)
        
        bouton_change_nom=ctk.CTkButton(tkinter_file.barre_navigation_bis,text="Changer nom", command=Button_Change_Nom)
        bouton_change_nom.pack(side=ctk.LEFT, padx=10)

        bouton_ajouter_transi = ctk.CTkButton(tkinter_file.barre_navigation_bis, text="Ajouter transi", command=Button_Ajouter_Transi)
        bouton_ajouter_transi.pack(side=ctk.LEFT, padx=10)
        
        bouton_supp_transi = ctk.CTkButton(tkinter_file.barre_navigation_bis, text="Supprimer transi", command=Button_Supprimer_Transi)
        bouton_supp_transi.pack(side=ctk.LEFT, padx=10)
        
        bouton_change_init=ctk.CTkButton(tkinter_file.barre_navigation_bis,text="Changer initiaux", command=Button_initiaux)
        bouton_change_init.pack(side=ctk.LEFT, padx=10)
        
        bouton_change_final=ctk.CTkButton(tkinter_file.barre_navigation_bis,text="Changer Final", command=Button_Final)
        bouton_change_final.pack(side=ctk.LEFT, padx=10)
        print("Bouton clique!")

def Button_Liste_AEF():

    popup = ctk.CTk()
    popup.wm_title("Liste des états")

    for state in aef.keys():
        label = ctk.CTkLabel(popup, text=state)
        label.pack(side="top", fill="x", pady=10)


    B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
    B1.pack(pady=(10, 10))
    popup.mainloop()

def Button_Supprimer_AEF():
    from tkinter_file import window
    global aef
    aef = {}
    print(aef)
    print("Bouton clique!")
    Generer_AEF_PNG(aef,window)

def Button_Exporter_AEF():
    window = ctk.CTk()
    #title
    window.title("Exporter un  AEF")
    #resolution
    window.geometry("300x100")
    #input on utilise la classe Entry
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
        print("On exporte le fichier :", entered_text)

        if fsm.existFile(entered_text) == True:
            print(f"Le fichier {entered_text} existe déjà (Debug : tkinter_function.py lines 47)")
            # on affiche une pop up d'erreur
            popup = ctk.CTk()
            popup.wm_title("Error")
            label = ctk.CTkLabel(popup, text="Le fichier existe déjà, choisis un autre nom")
            label.pack(side="top", fill="x", pady=10)
            B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
            B1.pack(pady=(10, 10))
            popup.mainloop()

        else:
            try:
                aef
                if aef != {}:
                    fsm.saveFile(aef, entered_text)
                    print("on sauvegarde le fichier car il existe pas ")
                else:
                    popup = ctk.CTk()
                    popup.wm_title("Error")
                    label = ctk.CTkLabel(popup, text="Votre AEF est vide, veuillez saisir un AEF avant de l'exporter")
                    label.pack(side="top", fill="x", pady=10)
                    B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
                    B1.pack(pady=(10, 10))
                    popup.mainloop()
            except NameError:
                print("aef n'est pas definie ")
                print("Error: empty FSM (Debug : tkinter_function.py lines 59)")
                popup = ctk.CTk()
                popup.wm_title("Error")
                label = ctk.CTkLabel(popup, text="Votre AEF est vide, veuillez saisir un AEF avant de l'exporter")
                label.pack(side="top", fill="x", pady=10)
                B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
                B1.pack(pady=(10, 10))
                popup.mainloop()


     
        window.quit()
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))

    window.mainloop()
    print("Bouton clique test!")
    print(aef)

def Button_Importer_AEF():
    window = ctk.CTk()
    #title
    window.title("Importer un  AEF")
    #resolution
    window.geometry("300x100")
    #input on utilise la classe Entry
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
        print("On import le fichier :", entered_text)

        if fsm.existFile(entered_text) == True:

           # if fsm.canOpen(entered_textz".fsm") == True:
            print("on peut ouvrir le fichier")
            global aef
            aef = fsm.openFile(entered_text+".fsm")
            print(aef)
                # a faire, mettre a jour l'interface graphique avec le aef qu'on a importé



        else:
            print("le fichier n'existe pas")
        # on affiche une pop up d'erreur
            popup = ctk.CTk()
            popup.wm_title("Error")
            label = ctk.CTkLabel(popup, text="Le fichier existe pas, choisis un autre nom")
            label.pack(side="top", fill="x", pady=10)
            B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
            B1.pack(pady=(10, 10))
            popup.mainloop()


        #Generer_AEF_PNG(aef, window)
        window.quit()
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))

    window.mainloop()
    print("Bouton clique test!")
    print(aef)


def Button_Ajouter_Transi():
    global image_label
    new_window = ctk.CTk()
    new_window.title("Add a trans")
    new_window.geometry("300x400")

    options =[]
    for state in aef:
        options.append(state)
    combo_box1 = ctk.CTkComboBox(master=new_window, values=options)
    #combo_box.set("Aucunes trans")  
    combo_box1.pack(pady=20, padx=10)
    combo_box2 = ctk.CTkComboBox(master=new_window, values=options)
    #combo_box.set("Aucunes trans")  
    combo_box2.pack(pady=20, padx=10)
        
    input_entry_name_trans = ctk.CTkEntry(new_window, width=200)
    input_entry_name_trans.pack(pady=(10, 10))
    from tkinter_file import window
    
    def on_enter_click():
        
   
        entered_text_name_trans = input_entry_name_trans.get()
        selected_value1 = combo_box1.get()
        selected_value2 = combo_box2.get()

 

        if fsm.canAddTrans(aef,selected_value1,selected_value2,entered_text_name_trans) is True:

            fsm.addTrans(aef,selected_value1,selected_value2,entered_text_name_trans)
            print(aef)
            Generer_AEF_PNG(aef, window)
        else:
            FenetreError("Erreur, la transition existe surement déjà")

        new_window.quit()
        try:
            new_window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
# bouton
    enter_button = ctk.CTkButton(new_window, text="Enter", command=on_enter_click)
    enter_button.pack(pady=(10, 10))

    
    new_window.mainloop()

def Button_Creer_Etat():
    global image_label
    new_window = ctk.CTk()
    new_window.title("Enter a state name")
    new_window.geometry("300x400")

    #input
    input_entry = ctk.CTkEntry(new_window, width=200)
    input_entry.pack(pady=(10, 10))

    #on creer les cases a cocher False par default
    initial_state_var = ctk.BooleanVar(value=False)
    final_state_var = ctk.BooleanVar(value=False)

    # on creer les checkbox
    if fsm.isInitialStateExist(aef) == False:
        initial_state_checkbox = ctk.CTkCheckBox(new_window, text="Initial State", variable=initial_state_var)
        initial_state_checkbox.pack(pady=(10, 10))

        final_state_checkbox = ctk.CTkCheckBox(new_window, text="Final State", variable=final_state_var)
        final_state_checkbox.pack(pady=(10, 10))
    else:
        final_state_checkbox = ctk.CTkCheckBox(new_window, text="Final State", variable=final_state_var)
        final_state_checkbox.pack(pady=(10, 10))


    #FAIRE LES TRANSITIONS

    



    if fsm.isInitialStateExist(aef)== False:
        options =[]
        for state in aef:
            options.append(state)
        options.append("Elle-même")
        options.append("Aucune Trans")
    else: 
    
        options =[]
        for state in aef:
            options.append(state)
            #options.append("Aucune Trans")
   
    combo_box = ctk.CTkComboBox(master=new_window, values=options)
    #combo_box.set("Aucunes trans")  
    combo_box.pack(pady=20, padx=10)

 

        
    input_entry_name_trans = ctk.CTkEntry(new_window, width=200)
    input_entry_name_trans.pack(pady=(10, 10))
    from tkinter_file import window
    
    def on_enter_click():
        
        # on recup tout
        is_initial = initial_state_var.get()
        is_final = final_state_var.get()
        entered_text = input_entry.get()
        entered_text_name_trans = input_entry_name_trans.get()
        print("initial state :", is_initial)
        print("final state :", is_final)
        print("On crée le state comme nom :", entered_text)

        selected_value = combo_box.get()
        print("La valeur sélectionnée est :", selected_value)

 
        if fsm.existState(aef, entered_text) == True:
            print("Error: already existing state name (Debug : tkinter_function.py lines 231)")
            # on affiche une pop up d'erreur
            FenetreError("Le state existe déjà, choisis un autre nom")
        elif entered_text == "":
            print("Error: empty state name (Debug : tkinter_function.py lines 235)")
            # on affiche une pop up d'erreur
            FenetreError("VEuillez saisir un nom de state")
        else:
            fsm.appendState(aef,entered_text,is_initial, is_final)

    
        if selected_value == "Elle-même":
            print("on ajoute la transition")
            fsm.addTrans(aef,entered_text,entered_text,entered_text_name_trans)
        elif selected_value == "Aucune Trans":
            pass
        elif selected_value != "Elle-même":
            fsm.addTrans(aef,selected_value,entered_text,entered_text_name_trans)
        print(aef)
        Generer_AEF_PNG(aef, window)

        new_window.quit()
        try:
            new_window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
# bouton
    enter_button = ctk.CTkButton(new_window, text="Enter", command=on_enter_click)
    enter_button.pack(pady=(10, 10))

    new_window.mainloop()
    print("Bouton clique test!")
    print(aef)

def Button_Supprimer_Etat():
    #create a new window
    window = ctk.CTk()
    #title
    window.title("Enter a state name to delete")
    #resolution
    window.geometry("300x100")
    #input 
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
        print("On supprimer le state comme nom :", entered_text)
        
        if fsm.IsStateInitial(aef,entered_text)==True:
            new_window = ctk.CTk()
            #title
            new_window.title("Choissisez quel etat qui devient initial")
            #resolution
            new_window.geometry("300x300")
            options =[]
            for state in aef:
                options.append(state)
            options.remove(entered_text)
            combo_box1 = ctk.CTkComboBox(master=new_window, values=options)
            #combo_box.set("Aucunes trans")  
            combo_box1.pack(pady=20, padx=10)
            def on_enter_click():
                selected_value1 = combo_box1.get()
                global aef
                aef=fsm.setInitial(aef,selected_value1)
                if fsm.existState(aef, entered_text) == True:
                    fsm.delState(aef, entered_text) 

                new_window.quit()
                try:
                    new_window.destroy()
                except ctk.TclError as e:
                    print("la fenetre a déjà été détruite:", e)

            # creer le boutton
        # bouton
            enter_button = ctk.CTkButton(new_window, text="Enter", command=on_enter_click)
            enter_button.pack(pady=(10, 10))

            
            new_window.mainloop()
            
        else:
            if fsm.existState(aef, entered_text) == True:
                fsm.delState(aef, entered_text)
                
            else:
            # on affiche une pop up d'erreur
                popup = ctk.CTk()
                popup.wm_title("Error")
                label = ctk.CTkLabel(popup, text="Le state existe pas dans l'AEF, choisis un autre nom")
                label.pack(side="top", fill="x", pady=10)
                B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
                B1.pack(pady=(10, 10))
                popup.mainloop()

        
        window.quit()
        
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite : ", e)
        
        
    
    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))
    
    window.mainloop()
    
    print("Bouton clique test!")
    print(aef)


def Button_Verifier_AEF():

    #create a new window
    window = ctk.CTk()
    #title
    window.title("Verifier un AEF")
    #resolution
    window.geometry("400x800")

   #on creer les cases a cocher False par default
    isDeterminist_state_var = ctk.BooleanVar(value=False)
    is_Complete_state_var = ctk.BooleanVar(value=False)

    # on creer les checkbox
    isDeterminist_state_checkbox = ctk.CTkCheckBox(window, text="isDeterminist", variable=isDeterminist_state_var)
    isDeterminist_state_checkbox.pack(pady=(10, 10))

    isComplete_state_checkbox = ctk.CTkCheckBox(window, text="isComplete", variable=is_Complete_state_var)
    isComplete_state_checkbox.pack(pady=(10, 10))
    

    #FAIRE LES TRANSITIONS
    def on_enter_click():
        # on recup tout
        print(isDeterminist_state_var)
        print(is_Complete_state_var)
        dict_to_display={}
        dict_to_display['is_Determinist']=isDeterminist_state_var.get()
        dict_to_display['is_Complete'] = is_Complete_state_var.get()

        print(dict_to_display)
        result_to_display=[]
        for key in dict_to_display:
            if dict_to_display[key]==True:
                result_to_display.append(key)

        
        window = ctk.CTk()
        #title
        window.title("Resultat de la verification")
        #resolution
        window.geometry("400x400")
        global aef

        try:
    
            aef
        except NameError:

            aef = {}
        if 'is_Determinist' in result_to_display:
            label = ctk.CTkLabel(window, text=f"Determinist : {fsm.isDeterminist(aef)}")
            label.pack(pady=(10, 10))
            print("caac")
        if 'is_Complete' in result_to_display:
            label = ctk.CTkLabel(window, text=f"Complete : {fsm.isComplete(aef)}")
            label.pack(pady=(10, 10))
      
            
        window.quit()
        window.mainloop()
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

        

        


    window.quit()
  
    # creer le boutton
# bouton
    enter_button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    enter_button.pack(pady=(10, 10))
    window.mainloop()

def Button_Actualiser_AEF():
    from tkinter_file import window
    """   global aef
    aef = fsm.makeDeterminist(aef)
    print(aef)
    print("l'aef est devenue Determinist!")
    Generer_AEF_PNG(aef,window)"""
    global aef
    Generer_AEF_PNG(aef,window)

def Button_Make_Complete():
    from tkinter_file import window
    global aef 
    aef = fsm.makeComplete(aef)
    print(aef)
    FenetreError("La fonction MakeComplete à été appliqué à l'AEF!")

def Button_Make_Determinist():
    global aef
    aef = fsm.makeDeterminist(aef)
    aef = fsm.excise(aef)
    FenetreError("La fonction MakeDeterminist à été appliqué à l'AEF")

def Button_Complement():
    global aef
    aef = fsm.complement(aef)
    FenetreError("La fonction complement à été appliqué à l'AEF")

def Button_Mirror():
    global aef
    aef = fsm.mirror(aef)
    FenetreError("La fonction Mirror à été appliqué à l'AEF")

def Button_Product():

    
    window = ctk.CTk()
    #title
    window.title("Choisir avec qui product")
    #resolution
    window.geometry("300x100")
    #input on utilise la classe Entry
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
       

        if fsm.existFile(entered_text) == True:

           # if fsm.canOpen(entered_textz".fsm") == True:
           
            global aef_temp
            aef_temp = fsm.openFile(entered_text+".fsm")
            print(f"LAEF TEMP : {aef_temp}")
            global aef
            aef = fsm.product(aef,aef_temp)
            FenetreError("La fonction Product à été appliqué à l'AEF")


        else:
           FenetreError("La fonction Product n'a pas été appliqué à l'AEF car le fichier n'existe pas")


        #Generer_AEF_PNG(aef, window)
        window.quit()
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))

    window.mainloop()






def Button_Concatenation():
    window = ctk.CTk()
    #title
    window.title("Choisir avec qui Concatenation")
    #resolution
    window.geometry("300x100")
    #input on utilise la classe Entry
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
       

        if fsm.existFile(entered_text) == True:

           # if fsm.canOpen(entered_textz".fsm") == True:
           
            global aef_temp
            aef_temp = fsm.openFile(entered_text+".fsm")
            print(f"LAEF TEMP : {aef_temp}")
            global aef
            aef = fsm.concatenation(aef,aef_temp)
            FenetreError("La fonction Concatenation à été appliqué à l'AEF")


        else:
           FenetreError("La fonction Concatenation n'a pas été appliqué à l'AEF car le fichier n'existe pas")


        #Generer_AEF_PNG(aef, window)
        window.quit()
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))

    window.mainloop()


def Button_Excise():
    global aef
    aef = fsm.excise(aef)
    FenetreError("La fonction concatenation à été appliqué à l'AEF")

def Button_Minimize():
    global aef
    aef = fsm.minimize(aef)
    FenetreError("La fonction Minimize à été appliqué à l'AEF")

def Button_RecognWord():
    window = ctk.CTk()
    #title
    window.title("Reconnaitre un mot")
    #resolution
    window.geometry("300x100")
    #input on utilise la classe Entry
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
       
        global aef
        if fsm.isDeterminist(aef) is False:
            aef = fsm.makeDeterminist(aef)
            aef = fsm.excise(aef)
            
        if fsm.recognWord(aef,entered_text) != False:


            FenetreError(f"Le mot est reconnue par l'aef:{fsm.recognWord(aef,entered_text)}")


        else:
           FenetreError("Le mot n'est pas reconnue par l'aef")


        #Generer_AEF_PNG(aef, window)
        window.quit()
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))

    window.mainloop() 

def Button_Supprimer_Transi():
    global image_label
    new_window = ctk.CTk()
    new_window.title("Add a trans")
    new_window.geometry("300x400")

    options =[]
    for state in aef:
        options.append(state)
    combo_box1 = ctk.CTkComboBox(master=new_window, values=options)
    #combo_box.set("Aucunes trans")  
    combo_box1.pack(pady=20, padx=10)
    combo_box2 = ctk.CTkComboBox(master=new_window, values=options)
    #combo_box.set("Aucunes trans")  
    combo_box2.pack(pady=20, padx=10)
    input_entry_name_trans = ctk.CTkEntry(new_window, width=200)
    input_entry_name_trans.pack(pady=(10, 10))
    from tkinter_file import window
    
    def on_enter_click():
        
   
        entered_text_name_trans = input_entry_name_trans.get()
        selected_value1 = combo_box1.get()
        selected_value2 = combo_box2.get()

 

    
        if fsm.canDelTrans(aef,selected_value1,selected_value2,entered_text_name_trans) == True:
            fsm.delTrans(aef,selected_value1,selected_value2,entered_text_name_trans)
            FenetreError("Transition supprimé, veuillez actualisé")
        else:
            FenetreError("Nom de transition ou etat incorrect, recommencez")


        new_window.quit()
        try:
            new_window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
# bouton
    enter_button = ctk.CTkButton(new_window, text="Enter", command=on_enter_click)
    enter_button.pack(pady=(10, 10))

    
    new_window.mainloop()  
    
def Button_initiaux():
    new_window = ctk.CTk()
    new_window.title("Changer initiaux")
    new_window.geometry("300x400")
    global aef
    options =[]
    for state in aef:
        options.append(state)
    
    combo_box1 = ctk.CTkComboBox(master=new_window, values=options)
    combo_box1.pack(pady=20)

    from tkinter_file import window

    def on_enter_click():
        

       
        selected_value1 = combo_box1.get()
        fsm.setInitial(aef,selected_value1)
        new_window.quit()
        try:
            new_window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    # bouton
    enter_button = ctk.CTkButton(new_window, text="Enter", command=on_enter_click)
    enter_button.pack(pady=(10, 10))


    new_window.mainloop()

def Button_Final():
    new_window = ctk.CTk()
    new_window.title("Changer Finaux")
    new_window.geometry("300x400")
    global aef
    options =[]
    for state in aef:
        options.append(state)
    
    combo_box1 = ctk.CTkComboBox(master=new_window, values=options)
    combo_box1.pack(pady=20)

    from tkinter_file import window

    def on_enter_click():
        

       
        selected_value1 = combo_box1.get()
        if fsm.IsStateFinal(aef,selected_value1) is True:
            fsm.setFinal(aef,selected_value1,False)
        else:
             fsm.setFinal(aef,selected_value1,True)
        new_window.quit()
        try:
            new_window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite:", e)

    # creer le boutton
    # bouton
    enter_button = ctk.CTkButton(new_window, text="Enter", command=on_enter_click)
    enter_button.pack(pady=(10, 10))


    new_window.mainloop()
    
def Button_Change_Nom():
    #create a new window
    window = ctk.CTk()
    #title
    window.title("Enter a state name to change")
    #resolution
    window.geometry("300x300")
    #input 
    input = ctk.CTkEntry(window, width=200)
    input.pack(pady=(10, 10))
    input2 = ctk.CTkEntry(window, width=200)
    input2.pack(pady=(10, 10))

    def on_enter_click():

        entered_text = input.get()
        new_name = input2.get()
        print("On change le state comme nom :", entered_text)
        if fsm.existState(aef, entered_text) == True and fsm.existState(aef,new_name) == False:
            fsm.changeStateName(aef,entered_text,new_name)
            label = ctk.CTkLabel(popup, text="Le nom de l'état a été changé veuillez actualiser l'AEF")
            label.pack(side="top", fill="x", pady=10)
        else:
        # on affiche une pop up d'erreur
            popup = ctk.CTk()
            popup.wm_title("Error")
            label = ctk.CTkLabel(popup, text="L'état n'existe pas ou le nouveau nom est déjà utilisé'")
            label.pack(side="top", fill="x", pady=10)
            B1 = ctk.CTkButton(popup, text="Okay", command = popup.destroy)
            B1.pack(pady=(10, 10))
            popup.mainloop()
        
        window.quit()
        
        try:
            window.destroy()
        except ctk.TclError as e:
            print("la fenetre a déjà été détruite : ", e)
        
        
    
    # creer le boutton
    button = ctk.CTkButton(window, text="Enter", command=on_enter_click)
    button.pack(pady=(10, 10))
    
    window.mainloop()
    
    print("Bouton clique test!")
    print(aef)