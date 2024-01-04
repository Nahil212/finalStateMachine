#This file contains all the necessary functions to manipulate a Finite State Machine (FSM)
#FSM = {'state1':{'transition':[ {'name': '', 'dest':' '}, {'name': '', 'dest':' '} , ...], 'initial': bool, 'final': bool},   'state2': ...}
import json
import os
from graphviz import Digraph
from itertools import combinations
#--- STATE FUNCTIONS ---

def initState(initial_state, final_state):
    """This function takes a name and a boolean as arguments and initialize a state"""
    
    state = {'transition': [],'initial': initial_state, 'final': final_state}
    return state

def canAppendState(Fsm, state_name, initial_state):
    """This function is necessary to use appendState() as it verifies that the state can be added without problem"""
    
    for state, carac in Fsm.items():
        if state == state_name:
            print("Error: already existing state")
            return False
        elif (carac['initial']==True and initial_state==True):
            print("Error: fsm already has an initial state")
            return False
    return True
        
def appendState(Fsm, state_name, initial_state, final_state):
    """This function takes a FSM structure, a name and booleans as arguments and add a new state to the final state machine"""
    
    Fsm[state_name]=initState(initial_state, final_state)
    return Fsm

def existState(Fsm, state_name):
    """This function is necessary to use other function(s) as it verifies if the state exists"""
    
    if state_name in Fsm.keys():
        return True
    else:
        print("Error: no existing state(s)")
        return False
 
def delState(Fsm, state_name):
    """This function takes a FSM structure and a name as arguments and delete the concerned state from the FSM"""
    
    # removing the state
    Fsm.pop(state_name)
    # removing transitions leading to this state
    for state, carac in Fsm.items():
        for trans in carac['transition']:
            if trans['dest'] == state_name:
                Fsm[state]['transition'].remove(trans)
    return Fsm
    
def setInitial(Fsm, state_name):
    """This function takes a FSM structure and a name as arguments and change the initial state of the FSM"""
    
    # removing the previous initial state
    for state in Fsm.keys():
        if(Fsm[state]['initial']):
            Fsm[state]['initial'] = False
    # setting the new initial state
    Fsm[state_name]['initial'] = True
    return Fsm

def setFinal(Fsm, state_name, setting):
    """This function takes a FSM structure, a name and a bool as arguments and sets the 'final' key of the state according to the setting"""

    Fsm[state_name]['final'] = setting
    return Fsm

def changeStateName(Fsm, state_name, new_name):
    """This function takes a FSM structure and two names as arguments and changes the name of the state"""

    Fsm[new_name] = Fsm.pop(state_name)

    for state,carac in Fsm.items():
        for i in range(len(carac['transition'])):
            if carac['transition'][i]['dest'] == state_name:
                Fsm[state]['transition'][i]={'name':carac['transition'][i]['name'], 'dest': new_name}
    return Fsm
    
#--- TRANSITION FUNCTIONS ---

def initTrans(trans_name, destination):
    """This function takes a name and a state as arguments and initialize a transition"""
    
    trans = {'name': trans_name, 'dest': destination}
    return trans
    
def canAddTrans(Fsm, state1, state2, trans_name):
    """This function is necessary to use addTrans() as it verifies that the transition can be added without problem"""
    
    if (state1 not in Fsm.keys()) or (state2 not in Fsm.keys()):
        print("Error: no existing state(s)")
        return False
    else:
        start = Fsm[state1]
        for trans in start["transition"]:
            if(trans["name"]== trans_name and trans["dest"]==state2):
                print("Error: already existing transition")
                return False
    return True

def addTrans(Fsm, state1, state2, trans_name):
    """This function takes a FSM structure, two states and a name as arguments to create a transition between them, the first state is the start and the second is the destination"""
    
    start = Fsm[state1]
    new_trans = initTrans(trans_name, state2)
    start["transition"].append(new_trans)
    Fsm[state1]=start
    return Fsm

def canDelTrans(Fsm, state1, state2, trans_name):
    """This function is necessary to use addTrans() as it verifies that the transition can be added without problem"""
    
    if (state1 not in Fsm.keys()) or (state2 not in Fsm.keys()):
        print("Error: no existing state(s)")
        return False
    else:
        start = Fsm[state1]
        for trans in start["transition"]:
            if(trans["name"]== trans_name and trans["dest"]==state2):
                return True
        print("Error: no existing transition")
        return False
    
def delTrans(Fsm, state1, state2, trans_name):
    """This function takes a FSM structure, two states and a name as arguments to delete the transition between them, the first state is the start and the second is the destination"""
    
    to_del = {'name':trans_name, 'dest':state2}
    Fsm[state1]['transition'].remove(to_del)
    return Fsm

def changeTransName(Fsm, state1, state2, trans_name, new_name):
    """This function takes a FSM structure, two states and two names as arguments to change the name of the transition going from 'state1' to 'state2' """
    
    conc_state = Fsm[state1]['transition']
    for i in range( len(conc_state) ):
        if (conc_state[i]['name'] == trans_name and conc_state[i]['dest'] == state2):
            new_trans = conc_state[i]
            new_trans['name'] = new_name
            Fsm[state1]['transition'][i] = new_trans
            return Fsm
        
def allTrans(Fsm):
    """
    Args:
        Fsm (dictionnary): fsm structure
    Returns:
        list: contains all existing transition name
    """
    trans_name = []
    for carac in Fsm.values():
        for trans in carac['transition']:
            if trans['name'] not in trans_name:
                trans_name.append(trans['name'])
    return trans_name
        
        
#--- DEBUGGING FUNCTIONS ---

def IsStateInitial(Fsm,state_name):
    """This function takes a FSM structure and a name as arguments and return True if the state is initial"""

    if Fsm[state_name]['initial']==True:
        print("The state is initial")
        return True
    else:
        print("The state is not initial")
        return False

def IsStateFinal(Fsm,state_name):
    """This function takes a FSM structure and a name as arguments and return True if the state is final"""

    if Fsm[state_name]['final']==True:
        print("The state is final")
        return True
    else:
        print("The state is not final")
        return False
    
#--- FILE FUNCTIONS ---

def saveFile(Fsm, file_name):
    """This function takes a Fsm structure and a name as arguments and saves it in a '.fsm' file """
    
    fsm_json = json.dumps(Fsm, indent = 2)
    save_name = file_name+".fsm"
    with open(save_name, 'w') as file:
        file.write(fsm_json)
    return True


def isEmpty(aef):
    """This function takes a Fsm structure as arguments and return True if the fsm is empty"""
    
    try:
        # Essayez d'accéder à la variable
        aef
    except NameError:
        # Exécuté si la variable n'est pas définie
        True
    else:
        # Exécuté si la variable est définie
        False


def canOpen(file_name):
    """This function is necessary to use openFile() as it verifies that the file exists and has the right format"""
    try:
        open(file_name, 'r')
    except FileNotFoundError:
        print("Error: no existing file")
        return False
    if(file_name.endswith(".fsm")):
        return True
    else:
        print("Error: wrong format")
        return False
    # A FINIR AVEC LE FORMAT .fsm
        
# on verifie si le fichier existe déjà

def existFile(file_name):
    """This function takes a name as argument and return True if the file exists"""
    if os.path.exists(file_name+".fsm"):
        return True
    else:
        print("le file existe pas ")
        return False

def openFile(file_name):
    """This function takes an empty Fsm structure and a file name as arguments and return the fsm saved in the file """
    file = open(file_name, 'r')
    Fsm = json.loads(file.read())
    return Fsm
    
#--- FSM FUNCTIONS ---
#a faire
def recognWord(Fsm, word):
    """This function verifies if a word is recognized by a specific fsm structure. It returns the followed states if it can or False if it can not. IT ONLY WORKS FOR DETERMINIST FSM.
    Args:
        Fsm (list): fsm structure
        word (char): the word to recognize
    """
    for state in Fsm:
        if(Fsm[state]["initial"]):
            current_state = state
            break
    followed_path = [current_state]
    
    for carac in word:
        found_dest = False
        
        for trans in Fsm[current_state]["transition"]:
            if trans['name'] == carac :
                found_dest = True
                current_state = trans['dest']
                followed_path.append(current_state)
                break
            
        if found_dest is False:
            return False
        
    if Fsm[current_state]['final']:
        return followed_path
    else:
        return False
    
def isComplete(Fsm):
    """This functions verifies if a fsm is complete, it returns True if it is and False if it's not.
    Args:
        Fsm (dictionnary): fsm structure
    """
    
    all_trans = allTrans(Fsm)
    for carac in Fsm.values():
        state_trans = []
        for trans in carac['transition']:
            if trans['name'] not in state_trans:
                state_trans.append(trans['name'])
                
        for name in all_trans:
            if name not in state_trans:
                return False
    
    return True

#a faire
def makeComplete(Fsm):
    """This function makes a fsm complete by adding necessary states
    Args:
        Fsm (dictionnary): fsm structure

    Returns:
        dictionnary: completed fsm structure
    """
    
    Fsm = appendState(Fsm,"φ",False,False)
    
    all_trans=allTrans(Fsm)
    for state,carac in Fsm.items():
        state_trans = []
        for trans in carac['transition']:
            if trans['name'] not in state_trans:
                state_trans.append(trans['name'])
                
        for name in all_trans:
            if name not in state_trans:
                Fsm = addTrans(Fsm,state,"φ",name)
        
    return Fsm


#a faire

def makeDeterminist(Fsm):
  """This function create a new determinist fsm able to read the same language as the original one
  Args:
      Fsm (dictionnary): fsm structure
  Returns:
      dictionnary: determinist fsm
  """
  det_fsm = {}
  #ADDING STATES
  for state, carac in Fsm.items():
    det_fsm = appendState(det_fsm, state, carac['initial'], carac['final'])
  for i in range(len(Fsm.keys()) - 1):
    comb = list(combinations(Fsm.keys(), i + 2))
    for name in comb:
      new_state = ','.join(name)
      det_fsm = appendState(det_fsm, new_state, False, False)
      state_list = new_state.split(',')
      for states in state_list:
        if Fsm[states]['final']:
          det_fsm = appendState(det_fsm, new_state, False, True)
          break
  det_fsm = appendState(det_fsm, "∅", False, False)

  #ADDING TRANSITIONS
  all_trans = allTrans(Fsm)
  for det_state, det_carac in det_fsm.items():
    for trans_name in all_trans:

      det_list = det_state.split(',')
      wanted_list = []
      for state in det_list:
        if state != "∅":
          for trans in Fsm[state]['transition']:
            if trans['name'] == trans_name:
              wanted_list.append(trans['dest'])
      wanted_list = sorted(list(set(wanted_list)))
      if len(wanted_list) > 1:
        dest_name = ",".join(wanted_list)
      elif len(wanted_list) == 1:
        dest_name = wanted_list[0]
      else:
        dest_name = "∅"
      det_fsm = addTrans(det_fsm, det_state, dest_name, trans_name)

  return det_fsm


def isDeterminist(Fsm):
    """This function verifies if a FSM is determinist or not, that is to say if two transitions with the same name go from the same state to two different states
    Args:
        Fsm (dictionnary): fsm structure
    """
    for carac in Fsm.values():
        state_trans=[]
        for trans in carac['transition']:
            if trans['name'] in state_trans:
                return False
            else:
                state_trans.append(trans['name'])
    return True


def MirrorAEF(aef):
    new_aef = {}

    # on soccupe d'abords des etats finaux et initiaux
    for state, properties in aef.items():
        if properties['initial']==True and properties['final']==True:
            new_aef[state] = {'transition': [], 'initial': True, 'final': True}
        elif properties['final']:
            new_aef[state] = {'transition': [], 'initial': True, 'final': False}
        elif properties['initial']:
            print("test")
            new_aef[state] = {'transition': [], 'initial': False, 'final': True}
        else:
            # le else est le dernier cas quand c'est False /False
            new_aef[state] = {'transition': [], 'initial': properties['initial'], 'final': properties['final']}

    # transition:

    for state, properties in aef.items():
        for transition in properties['transition']:
            # eske la transition est vide ? si oui on la laisse vide
            if transition['dest'] != '':
                # on prends la transi on linverse et on ajoute
                new_aef[transition['dest']]['transition'].append({'name': transition['name'], 'dest': state})

    # a la fin si tu veux que les transitions [] soit remplies rajoutes ce commentaire :
    '''for state in aef:
        if new_aef[state]['transition'] == []:
            new_aef[state]['transition'].append({'name': '', 'dest': ''})
    '''
    return new_aef

def isInitialStateExist(aef):
    for state in aef:
        if aef[state]['initial'] == True:
            return True
    return False



def generer_aef_png_modifie(aef):
    dot = Digraph(comment='Mon AEF Modifié')

    for state, properties in aef.items():
    
        if properties['initial']:
            fake_initialstate = "start" + state
            dot.node(",kjengle", '', shape='point')
            dot.edge(",kjengle", state, label='')

     
        if properties['final']:
            dot.node(state, state, shape='doublecircle')
        else:
            dot.node(state, state)

        for transition in properties['transition']:
            label = transition.get('name', '')  
            dot.edge(state, transition['dest'], label=label)

  
    file_path = 'aef'

    try:
        dot.render(file_path, view=False, format='png')
        return file_path + '.png'
    except Exception as e:
        print("Une erreur est survenue lors de la génération du fichier PNG :", e)
        return None

#faire bouton pour les chaques

def complement(Fsm):
  """This function make final states non-final and non-final states final
  Args:
      Fsm (dictionnary): fsm structure
  Returns:
      dictionnary: complement of the initial fsm
  """

  new_fsm = Fsm
  for state, carac in new_fsm.items():
    if carac['final']:
      new_fsm[state]['final'] = False
    else:
      new_fsm[state]['final'] = True
  return new_fsm


def mirror(Fsm):
  """This function inverses initial and final states, and the sens of transitions
  Args:
      Fsm (dictionnary): fsm structure
  Retruns:
      dictionnary: mirror of the original fsm
  """

  new_fsm = {}

  #INVERSING INITIAL AND FINAL BOOL
  for state, carac in Fsm.items():
    if (carac['initial'] and carac['final']) or (carac['initial'] is False
                                                 and carac['final'] is False):
      new_fsm = appendState(new_fsm, state, False, False)
    else:
      if carac['initial']:
        new_fsm = appendState(new_fsm, state, False, True)
      elif carac['final']:
        new_fsm = appendState(new_fsm, state, True, False)

  #INVERSING TRANSITIONS' SENS
  for state, carac in Fsm.items():
    for trans in carac['transition']:
      new_fsm = addTrans(new_fsm, trans['dest'], state, trans['name'])

  #INITIALIZATION OF THE NEW INITIAL STATE
  new_fsm = appendState(new_fsm, 'φ', True, False)
  for state, carac in new_fsm.items():
    if carac['initial'] and state != 'φ':
      new_fsm[state]['initial'] = False
      if carac['final']:
        new_fsm = setFinal(new_fsm, 'φ', True)
      for trans in carac['transition']:
        new_fsm = addTrans(new_fsm, 'φ', trans['dest'], trans['name'])
        print(trans)
  return new_fsm


def isInitialStateExist(aef):
  for state in aef:
    if aef[state]['initial'] == True:
      return True
  return False


def concatenation(Fsm_A, Fsm_B):
  """This function creates a new fsm where A's transitions are followed by B's transitions. Final states are B's final states and the initial state is A's one.

  Args:
      Fsm_A (dictionnary): fsm structure
      Fsm_B (dictionnary): fsm structure

  Returns:
      dictionnary: concatenation of Fsm A and B
  """

  conc_fsm = {}
  final_A = []
  #ADDING STATES
  for state_A, carac_A in Fsm_A.items():
    if (carac_A['final']):
      final_A.append(state_A)
    conc_fsm = appendState(conc_fsm, state_A, carac_A['initial'],
                           carac_A['final'])
  for state_B, carac_B in Fsm_B.items():
    if (carac_B['initial']):
      if state_B in Fsm_A.keys():
        initial_B = 'B(' + state_B + ')'
      else:
        initial_B = state_B
    if canAppendState(conc_fsm, state_B, False):
      conc_fsm = appendState(conc_fsm, state_B, False, carac_B['final'])
    else:
      conc_fsm = appendState(conc_fsm, 'B(' + state_B + ')', False,
                             carac_B['final'])

  #ADDING TRANSITIONS
  for state_A, carac_A in Fsm_A.items():
    for trans in carac_A['transition']:
      conc_fsm = addTrans(conc_fsm, state_A, trans['dest'], trans['name'])
  for state_B, carac_B in Fsm_B.items():
    for trans in carac_B['transition']:
      if state_B in Fsm_A.keys():
        B_name = 'B(' + state_B + ')'
      else:
        B_name = state_B
      if trans['dest'] in Fsm_A.keys():
        conc_fsm = addTrans(conc_fsm, B_name, 'B(' + trans['dest'] + ')',
                            trans['name'])
      else:
        conc_fsm = addTrans(conc_fsm, B_name, trans['dest'], trans['name'])

  #PUTTING IN RELATION A'S FINALS WITH B'S INITIAL STATE
  for state in final_A:
    conc_fsm = setFinal(conc_fsm, state, False)
    for trans in conc_fsm[initial_B]['transition']:
      conc_fsm = addTrans(conc_fsm, state, trans['dest'], trans['name'])
  conc_fsm[initial_B]['initital'] = False

  return conc_fsm


def product(Fsm_A, Fsm_B):
  """This function creates a new fsm where states are all the possible combination of A and B's states.
  
  Args:
      Fsm_A (dictionnary): fsm structure
      Fsm_B (dictionnary): fsm structure
  
  Returns:
      dictionnary: product of Fsm A and B
  """

  prod_fsm = {}

  #ADDING PRODUCT STATES
  for state_A, carac_A in Fsm_A.items():
    for state_B, carac_B in Fsm_B.items():
      prod_state = state_A + ',' + state_B
      init_val = False
      final_val = False
      if (carac_A['initial'] and carac_B['initial']):
        init_val = True
      if (carac_A['final'] and carac_B['final']):
        final_val = True
      if prod_state not in prod_fsm.keys():
        prod_fsm = appendState(prod_fsm, prod_state, init_val, final_val)

  #ADDING CORRESPONDING TRANSITIONS
  for state in prod_fsm.keys():
    state_list = state.split(',')
    for trans_A in Fsm_A[state_list[0]]['transition']:
      for trans_B in Fsm_B[state_list[1]]['transition']:
        if trans_A['name'] == trans_B['name']:
          if canAddTrans(prod_fsm, state,trans_A['dest'] + ',' + trans_B['dest'], trans_A['name']):
            prod_fsm = addTrans(prod_fsm, state, trans_A['dest'] + ',' + trans_B['dest'], trans_A['name'])

  #CHANGING STATES' NAME FOR FUTURE PRODUCTS
  rename_fsm={}
  for state,carac in prod_fsm.items():
        state_list = state.split(',')
        rename_fsm = appendState(rename_fsm,state_list[0]+'|'+state_list[1],prod_fsm[state]['initial'],prod_fsm[state]['final'])
        for trans in carac['transition']:
            dest_list = trans['dest'].split(',')
            rename_fsm = addTrans(rename_fsm,state_list[0]+'|'+state_list[1],dest_list[0]+'|'+dest_list[1],trans['name'])

  return rename_fsm



#fct pour fct emonde 

def isCoAccessible(Fsm, state_name):
  """This function verifies if ,for a given fsm structure and a state in this structure, a path exists from this state to a final state

  Args:
      Fsm (dictionnary): fsm structure
      state_name (char): the state of start

  Returns:
      bool: The state is co-accessible or not
  """
  visited_state = set()
  to_visit = [state_name]

  def loop(state_loop, to_visit):
    if (Fsm[state_loop]['final']):
      return True
    else:
      visited_state.add(state_loop)
      to_visit.remove(state_loop)
      for trans in Fsm[state_loop]['transition']:
        if (trans['dest'] not in visited_state):
          to_visit.insert(0, trans['dest'])
      if (len(to_visit) == 0):
        return False
      else:
        return loop(to_visit[0], to_visit)

  return loop(state_name, to_visit)


def isAccessible(Fsm, state_name):
  """This function verifies if ,for a given fsm structure and a state in this structure, a path exists from the initial state to this state

  Args:
      Fsm (dictionnary): fsm structure
      state_name (char): the state of end

  Returns:
      bool: The state is accessible or not
  """
  visited_state = set()
  for state, carac in Fsm.items():
    if carac['initial']:
      initial_state = state
      to_visit = [state]
      break

  def loop(state_loop, to_visit):
    if (state_loop == state_name):
      return True
    else:
      visited_state.add(state_loop)
      to_visit.remove(state_loop)
      for trans in Fsm[state_loop]['transition']:
        if (trans['dest'] not in visited_state):
          to_visit.insert(0, trans['dest'])
      if (len(to_visit) == 0):
        return False
      else:
        return loop(to_visit[0], to_visit)

  return loop(initial_state, to_visit)



#faire un bouton pour émonde 


def excise(Fsm):
  """This function remove states, and their associated transitions, that are neither accessible nor co-accessible
  
  Args:
      Fsm (dictionnary): fsm structure
  
  Returns:
      dictionnary: excised fsm structure
  """

  unval_state = []
  for state in Fsm.keys():
    if (isAccessible(Fsm, state) is False
        or isCoAccessible(Fsm, state) is False):
      unval_state.append(state)
  for state in unval_state:
    Fsm = delState(Fsm, state)

  return Fsm


def stateInGroup(Fsm, number):
  """This function is used in the minimize function and gathers states that are in one group called by a number
  
  Args:
      Fsm (dictionnary): fsm structure
      number (int): number of the group
  
  Returns:
      table: states that belong to the group
  """
  group = []
  for state,carac in Fsm.items():
      if carac['group'] == number:
          group.append(state)
  
  return group
# a faire 

def minimize(Fsm):
  """This function minimizes a fsm by following Moore's minimization algorithm 
  
  Args:
      Fsm (dictionnary): fsm structure
  
  Returns:
      dictionnary: minimized fsm
  """

  #SEPARATING FINAL AND NON-FINAL STATES IN TWO GROUPS
  all_trans = allTrans(Fsm)
  for state, carac in Fsm.items():
    if carac['final']:
      Fsm[state]['group'] = 0
    else:
      Fsm[state]['group'] = 1

  #APPLIYING MOORE'S ALGORITHM
  highest_group = 1
  error = True
  while error:
    error = False
    highest_group += 1
    for curr_state, curr_carac in Fsm.items():

      #Gathering states that are in the same group as our current state
      nb_group = curr_carac['group']
      states_group = stateInGroup(Fsm, nb_group)

      #Comparing the group of the destination state for each transition in the alphabet
      for letter in all_trans:
        #Looking at the destination state's group for our current state
        group_dest = -1
        for curr_trans in curr_carac['transition']:
          if curr_trans['name'] == letter:
            group_dest = Fsm[curr_trans['dest']]['group']
            break

        #Looking at the destination state's group for the other states of our current group
        for state in states_group:
          dest = -1
          for trans in Fsm[state]['transition']:
            if trans['name'] == letter:
              dest = Fsm[trans['dest']]['group']
              break
          if group_dest != dest or curr_carac['final'] != Fsm[state]['final']:
            Fsm[curr_state]['group'] = highest_group
            error = True
            break

  #CREATING A MINIMIZED FSM ACCORDING TO CREATED GROUPS
  dict_group = {}
  for state, carac in Fsm.items():
    if carac['group'] in dict_group.keys():
      dict_group[carac['group']].append(state)
    else:
      dict_group[carac['group']] = [state]

  minim_fsm = {}
  for name in dict_group.values():
    initial = False
    final = False
    state_name = name[0]
    if Fsm[state_name]['initial']:
      initial = True
    if Fsm[state_name]['final']:
      final = True
    for i in range(1, len(name)):
      state_name += ',' + name[i]
      if Fsm[name[i]]['initial']:
        initial = True
      if Fsm[name[i]]['final']:
        final = True
    minim_fsm = appendState(minim_fsm, state_name, initial, final)

  for state, carac in Fsm.items():
    if state in minim_fsm.keys():
      for trans in carac['transition']:
        if trans['dest'] in minim_fsm.keys():
          minim_fsm = addTrans(minim_fsm, state, trans['dest'], trans['name'])
        else:
          for group_state in minim_fsm.keys():
            list = group_state.split(',')
            if trans['dest'] in list:
              dest = group_state
              break
          if canAddTrans(minim_fsm, state, dest, trans['name']):
            minim_fsm = addTrans(minim_fsm, state, dest, trans['name'])
    else:
      for group_state in minim_fsm.keys():
        list = group_state.split(',')
        if state in list:
          start = group_state
          break
      for trans in carac['transition']:
        if trans['dest'] in minim_fsm.keys():
          if canAddTrans(minim_fsm, start, trans['dest'], trans['name']):
            minim_fsm = addTrans(minim_fsm, start, trans['dest'],
                                 trans['name'])
        else:
          for group_state in minim_fsm.keys():
            list = group_state.split(',')
            if trans['dest'] in list:
              dest = group_state
              break
          if canAddTrans(minim_fsm, start, dest, trans['name']):
            minim_fsm = addTrans(minim_fsm, start, dest, trans['name'])

  #CHANGING STATES' NAME FOR FUTURE MINIMIZATIONS
  rename_fsm = {}
  for min_state, min_carac in minim_fsm.items():
    state_list = min_state.split(',')
    new_name = state_list[0]
    for i in range(1, len(state_list)):
      new_name += '|' + state_list[i]
    rename_fsm = appendState(rename_fsm, new_name, min_carac['initial'],
                             min_carac['final'])

    for min_trans in min_carac['transition']:
      trans_list = min_trans['dest'].split(',')
      trans_dest = trans_list[0]
      for j in range(1, len(trans_list)):
        trans_dest += '|' + trans_list[j]
      rename_fsm = addTrans(rename_fsm, new_name, trans_dest,
                            min_trans['name'])

  return rename_fsm