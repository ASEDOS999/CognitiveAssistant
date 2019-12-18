
import numpy as np

class CognitiveAssistant:
    def __init__(self, name = None, ScriptGraph = None):
        self.name = name
        self.ScriptGraph = ScriptGraph

    def dialogue_start(self, N):
        vert = ScriptGraph
        self.user_state = None
        while not vert is None:
            vert, user_state = vert.dialogue()

            
class ScriptGraphVert:
    def __init__(self, name = None, texts = None,
            is_terminal = False, is_start = True):
        self.name = name
        if texts is None:
            texts = []
        self.texts = texts
        self.next_states = []
        self.is_terminal = is_terminal
        self.is_start = is_start
    
    def dialogue(self, user_state):
        if user_state is None:
            if self.is_start:
                user_state = np.zeros((300,))
            else:
                return None
        self.text_generator()
        return self.make_a_choice(), user_state

    def text_generator(self):
        for text in self.texts:
            print(text)

    def add_edge(self, edge = None, name = None, text = None, cond = None):
        if is_terminal:
            print("You can not to add children into terminal vertices")
            return None
        if edge is None:
            new_child = ScriptGraphVert(name = name, text = text)
            edge = new_child, cond
        self.edge.append(new_edge)
    
    def make_a_choice(self):
        def dist(s1, s2):
            return int(s1==s2)
        if len(self.children) == 0:
            return None
        else:
            return self.edges
        s = input()
        ind = np.argmax(np.array([dist(i.cond, s) for i in self.edges]))
        return self.edges[ind].next_vert
        
class edge:
    def __init__(self, next_vert, cond):
        self.next_vert = next_vert
        self.cond = cond
