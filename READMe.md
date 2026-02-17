# AI Interview State Machine

This project demonstrates a minimal, explicit state machine used to control
a multi-stage interview flow.

## Why
AI should not control state. This system enforces explicit transitions to
prevent state drift, double transitions, and undefined behavior.

## States
- INIT
- INTRO
- EXPERIENCE
- END

## Events
- START
- ANSWER
- TIMEOUT

## Transition Table
(INIT, START) → INTRO  
(INTRO, ANSWER) → EXPERIENCE  
(EXPERIENCE, ANSWER) → END  
(INTRO, TIMEOUT) → END  
(EXPERIENCE, TIMEOUT) → END  

Illegal transitions are ignored.

## Failure Handling
- Duplicate events → safe (idempotent)
- Silence → handled via TIMEOUT
- Late events → ignored
- User spam → no state drift

## Key Rule
State transitions are centralized and deterministic.
AI is used only for response generation, never for control flow.
