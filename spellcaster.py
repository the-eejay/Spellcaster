from player import Player

p = Player()
q = Player()

p.make_gesture('F', 'F')
q.make_gesture('P', 'P')

print(p.hands)
print(q.hands)

p.hp -= 1
q.hp -= 1
