from piece import Piece, COLORS, BLACK, WHITE
from empty import Empty


CONSOLE_IMAGE = {
    BLACK: '\33[94m♜',
    WHITE: '\33[93m♖'
}


class Rook(Piece):
    """ Rook """

    def make_move(self, piece_to):
        if self.can_move(piece_to):
            self.board.history.append('{0}({1}) --> {2}({3})'.format(self, self.position, piece_to, piece_to.position))
            self.board[self.position], self.board[piece_to.position] = Empty(None, self.board), self.board[self.position]
            if self.first_move:
                self.first_move = False
            if not isinstance(piece_to, Empty):
                self.board.deleted_pieces.append(piece_to)
        else:
            raise Exception('Rook can\'t move there')

    def can_move(self, piece_to):
        pos_from, pos_to = self.board.get_coords(self.position), self.board.get_coords(piece_to.position)

        if self.side != piece_to.side:
            if pos_from[1] == pos_to[1]:
                space = range(pos_to[0] + 1, pos_from[0]) if pos_from[0] > pos_to[0] else range(pos_from[0] + 1, pos_to[0])
                for item in space:
                    if not isinstance(self.board[self.board.get_pos((item, pos_to[1]))], Empty):
                        return False
                return True
            elif pos_from[0] == pos_to[0]:
                space = range(pos_to[1] + 1, pos_from[1]) if pos_from[1] > pos_to[1] else range(pos_from[1] + 1, pos_to[1])
                for item in space:
                    if not isinstance(self.board[self.board.get_pos((pos_to[0], item))], Empty):
                        return False
                return True
        return False

    def __str__(self):
        return CONSOLE_IMAGE[self.side]

    def __repr__(self):
        return f'<Rook ({COLORS[self.side]})>'
