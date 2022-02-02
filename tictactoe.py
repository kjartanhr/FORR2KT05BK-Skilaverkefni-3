class MissingPropertiesException(Exception):
    pass

class TicTacToe:
    def __init__(self, player_a, player_b):
        if "mark" not in player_a or "mark" not in player_b:
            raise MissingPropertiesException("Mark is not defined for one or more players")
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]
        self.players = [player_a, player_b]
        self.active_player = self.players[0]
    def play(self, p, x, y):
        player = self.players[p]
        try:
            if self.matrix[x][y] != 0:
                return {"error": "Invalid coordinate", "code": 1}
            else:
                self.matrix[x][y] = player["mark"]
                self.active_player = self.players[0] if p == 1 else self.players[1]
        except IndexError:
            return {"error": "Coordinate out of bounds, values range from 0-2 for x & y.", "code": 2}
    def get_winner(self):
        m = self.matrix
        def t(p, x, y):
            return m[x][y] == p["mark"]
        for p in self.players:
            if t(p, 0, 0) and t(p, 1, 1) and t(p, 2, 2) or t(p, 0, 2) and t(p, 1, 1) and t(p, 2, 0):
                return p
            for i in range(0, 3):
                if t(p, i, 0) and t(p, i, 1) and t(p, i, 2):
                    return p
            for i in range(0, 3):
                if t(p, 0, i) and t(p, 1, i) and t(p, 2, i):
                    return p
        return None

def visualise(matrix):
    for i in matrix:
        for x in i:
            print(x, end = " ")
        print()
    print()

def main():
    engine = TicTacToe({"name": "Player 1", "mark": "x"}, {"name": "Player 2", "mark": "y"})
    visualise(engine.matrix)
    engine.play(1, 0, 0)
    engine.play(1, 1, 1)
    engine.play(1, 2, 0)
    visualise(engine.matrix)
    print(engine.get_winner())

if __name__ == '__main__':
    main()