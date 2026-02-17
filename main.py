from state import State, Event
from engine import StateMachine

sm = StateMachine(State.INIT)

sm.handle(Event.START)
sm.handle(Event.ANSWER)
sm.handle(Event.ANSWER)
sm.handle(Event.ANSWER)

