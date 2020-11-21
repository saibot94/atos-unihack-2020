from models import Token, Place, Transition


p1 = Place(1, 10, [Token(1)])
p2 = Place(2, 10, [Token(2)])
p3 = Place(3, 10, [])
p4 = Place(4, 10, [Token(1234)])

t1_inputs = [p1, p2]
t1_outputs = [p3]

t2_inputs, t2_outputs = [p3], [p4]


TRANSITIONS = [
    Transition("t1", t1_inputs, t1_outputs),
    Transition("t2", t2_inputs, t2_outputs),
]
