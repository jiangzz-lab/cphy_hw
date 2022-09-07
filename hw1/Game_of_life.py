import numpy as np

from IPython.display import Image, clear_output, display
clear_output(True)

import matplotlib.pyplot as plt
#%matplotlib inline

# A base class
class CellularAutomaton:
    '''
    A base class for celllular automata. Subclass must implement the step method.
    
    Parameters
        n (int): The number of cells in the system
        n_states (int): The number of states in the system
        random_state (None or int): The seed for the random number generator. If None,
            the random number is not seeded.
        initial_state (None or array): The initial state of the system. If None, a random
            initial state is generated
    '''
    def __init__(self, n, n_states, random_state=None, initial_state=None):
        self.n_states = n_states
        self.n = n
        self.random_state = random_state
        
        np.random.seed(random_state)
        
        ## The universe is a ramdom array of integers
        if initial_state is None: # generate a random sample of n * n matrix 
            self.initial_state = np.random.choice(self.n_states, size=(self.n, self.n))
        else:
            self.initial_state = initial_state
        self.state = self.initial_state
        
        self.history = [self.state]
        
    def next_state(self):
        '''
        Output the next state of the entire board
        '''
        return NotImplementedError
    
    def simulate(self, n_steps):
        '''
        Iterate the dynamics for n_steps, and return the results as an array
        '''
        for i in range(n_steps):
            self.state = self.next_state()
            self.history.append(self.state)
        return self.state

class ExtinctionAutomaton(CellularAutomaton):
    '''
    A cellular automaton that simulates the extinction of a species.
    '''
    def __init__(self, n, **kwargs):
        super().__init__(n, 2, **kwargs)
        
    def next_state(self):
        '''
        Output the next states of the entire board
        '''
        next_state = np.zeros_like(self.state)
        return next_state
    
class RandomAutomaton(CellularAutomaton):
    '''
    A cellular automaton with random updates
    '''
    def __init__(self, n, random_state=None, **kwargs):
        super().__init__(n, 2, **kwargs)
        self.random_state = random_state
        
    def next_state(self):
        '''
        Output the next state of the entire booard
        '''
        next_state = np.random.choice(self.n_states, size=(self.n, self.n))
        return next_state

model = ExtinctionAutomaton(40, random_state=0)
model.simulate(200)

plt.figure()
plt.imshow(model.initial_state, cmap="gray")
plt.title("Initial state")

plt.figure()
plt.imshow(model.state, cmap="gray")
plt.title("Final")

model = RandomAutomaton(40, random_state=0)
model.simulate(200)

plt.figure()
plt.imshow(model.initial_state, cmap="gray")
plt.title("Initial state")

plt.figure()
plt.imshow(model.state, cmap="gray")
plt.title("Final")