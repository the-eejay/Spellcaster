class Player:
    hp = 15

    def __init__(self):
        self.hands = [[],[]]
    
    def make_gesture(self, left_gesture, right_gesture):
        self.hands[0].append(left_gesture)
        self.hands[1].append(right_gesture)
