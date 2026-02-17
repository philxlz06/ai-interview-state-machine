from transitions import TRANSITIONS

class StateMachine:
    def __init__(self, initial_state):
        self.state= initial_state

    
    def handle(self, event):
        prev = self.state
        self.state = TRANSITIONS.get((self.state,event), self.state)
        print(f"{prev.name} --{event.name} --> {self.state.name}")

        
