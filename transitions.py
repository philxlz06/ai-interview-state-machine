from state import State, Event

TRANSITIONS ={
    (State.INIT, Event.START): State.INTRO,
    (State.INTRO, Event.ANSWER): State.EXPERIENCE,
    (State.EXPERIENCE, Event.ANSWER): State.END,
    (State.INTRO, Event.TIMEOUT): State.END,
    (State.EXPERIENCE, Event.TIMEOUT): State.END,

}

