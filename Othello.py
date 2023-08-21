# Author: Blake Jennings
# GitHub username: BlakeJenn
# Date: 6/1/2023
# Description: Creates a game of Othello with a player list, board, and methods to
# make the game playable

class Player:
    """
    Represents a player in the Othello game.
    """

    def __init__(self, player_name, piece_color):
        """
        Initializes a Player object with a name and
        piece color (either white or black).
        """
        self._player_name = player_name
        self._piece_color = piece_color

    def get_name(self):
        """
        Returns the name of the Player Object. Used by
        return_winner function in Othello Class.
        """
        return self._player_name


class Othello:
    """
    Represents an Othello board with a list of players.
    """

    def __init__(self):
        """
        Initializes an Othello game object with an
        initial board setup and player dictionary. Takes no parameters.
        """
        self._board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]
        self._player_dict = {}

    def print_board(self):
        """
        Prints the Othello board in its current state.
        """
        for row in self._board:
            print(*row)

    def get_player_list(self):
        """
        Returns a list of Othello players by their name
        """
        final = []
        for person in self._player_dict:
            final.append(person.get_name())
        return final

    def create_player(self, player_name, color):
        """
        Creates a player object with the given name and color. It then
        adds that player to the player dictionary.

        """
        if color.lower() == "white":
            self._player_dict['White'] = Player(player_name, color)
        if color.lower() == "black":
            self._player_dict['Black'] = Player(player_name, color)

    def return_winner(self):
        """
        Determines which piece color shows up the most on the Othello board and
        returns a message stating who has won the game. If it is a tie,
        returns that a tie has occurred. Used by play_game function
        """
        X_score = 0
        O_score = 0
        for row in self._board:
            for item in row:
                if item == 'X':
                    X_score += 1
                if item == 'O':
                    O_score += 1
        if O_score > X_score:
            return f"Winner is white player: {self._player_dict['White'].get_name()}! "
        if X_score > O_score:
            return f"Winner is black player: {self._player_dict['Black'].get_name()}! "
        if X_score == O_score:
            return f"It's a tie!"

    def return_available_positions(self, color):
        """
        Looks for every piece on the board that is the opposite of the given color.
        It then determines if there are any empty positions immediately in one direction and
        a piece with the given color in the opposite direction either immediately or after
        a chain of pieces of the opposite color. If this occurs, it adds the empty position to
        the list of valid moves. Once this has occurred for every opposite color piece, it
        sorts and returns the list of valid moves.
        """
        available = []
        if color.lower() == "black":
            current = 'X'
            not_current = 'O'
        if color.lower() == "white":
            current = 'O'
            not_current = 'X'
        for row, rows in enumerate(self._board):
            for column, item in enumerate(rows):
                if self._board[row][column] == not_current:

                    # check right of position
                    if self._board[row][column + 1] == '.':
                        column_save = column  # placeholder to not affect column variable
                        while self._board[row][column_save] == not_current:
                            column_save -= 1  # move left in row until current piece color, '.', or '*' is found
                        if self._board[row][column_save] == current:
                            if (row, column + 1) not in available:
                                available.append((row, column + 1))

                    # check left of position
                    if self._board[row][column - 1] == '.':
                        column_save = column
                        while self._board[row][column_save] == not_current:
                            column_save += 1
                        if self._board[row][column_save] == current:
                            if (row, column - 1) not in available:
                                available.append((row, column - 1))

                    # check below position
                    if self._board[row + 1][column] == '.':
                        row_save = row
                        while self._board[row_save][column] == not_current:
                            row_save -= 1
                        if self._board[row_save][column] == current:
                            if (row + 1, column) not in available:
                                available.append((row + 1, column))

                    # check above position
                    if self._board[row - 1][column] == '.':
                        row_save = row
                        while self._board[row_save][column] == not_current:
                            row_save += 1
                        if self._board[row_save][column] == current:
                            if (row - 1, column) not in available:
                                available.append((row - 1, column))

                    # check lower right of position
                    if self._board[row + 1][column + 1] == '.':
                        row_save = row
                        column_save = column
                        while self._board[row_save][column_save] == not_current:
                            row_save -= 1
                            column_save -= 1
                        if self._board[row_save][column_save] == current:
                            if (row + 1, column + 1) not in available:
                                available.append((row + 1, column + 1))

                    # check upper right of position
                    if self._board[row - 1][column + 1] == '.':
                        row_save = row
                        column_save = column
                        while self._board[row_save][column_save] == not_current:
                            row_save += 1
                            column_save -= 1
                        if self._board[row_save][column_save] == current:
                            if (row - 1, column + 1) not in available:
                                available.append((row - 1, column + 1))

                    # check lower left of position
                    if self._board[row + 1][column - 1] == '.':
                        row_save = row
                        column_save = column
                        while self._board[row_save][column_save] == not_current:
                            row_save -= 1
                            column_save += 1
                        if self._board[row_save][column_save] == current:
                            if (row + 1, column - 1) not in available:
                                available.append((row + 1, column - 1))

                    # check upper left of position
                    if self._board[row - 1][column - 1] == '.':
                        row_save = row
                        column_save = column
                        while self._board[row_save][column_save] == not_current:
                            row_save += 1
                            column_save += 1
                        if self._board[row_save][column_save] == current:
                            if (row - 1, column - 1) not in available:
                                available.append((row - 1, column - 1))
        available.sort()
        return available

    def make_move(self, color, piece_position):
        """
        Assumes move is made in valid position.
        Looks for every position immediately around placed piece for piece
        of opposite color. If one is found, looks to see if there is a piece of
        the same color later in the direction either immediately after the
        opposite color piece or after a chain of opposite color pieces. If piece
        is found, it changes all the opposite color pieces within the two color pieces
        to the piece color given. After this occurs in all directions, returns the
        updated board.
        """
        # setup
        (row, column) = piece_position
        if color.lower() == "black":
            self._board[row][column] = 'X'
            current = 'X'
            not_current = 'O'
        if color.lower() == "white":
            self._board[row][column] = 'O'
            current = 'O'
            not_current = 'X'

        # change right
        if self._board[row][column + 1] == not_current:  # if piece to the right is opposite color
            column_save = column + 1  # create placeholder for column to not affect column variable
            while self._board[row][column_save] == not_current:
                # move right until current piece color, '.', or '*' is found
                column_save += 1
            if self._board[row][column_save] == current:  # if piece of current color is found
                for item in range(column + 1, column_save):  # move stepwise in opposite direction
                    self._board[row][item] = current  # change color of piece to current piece

        # change left
        if self._board[row][column - 1] == not_current:
            column_save = column - 1
            while self._board[row][column_save] == not_current:
                column_save -= 1
            if self._board[row][column_save] == current:
                for item in range(column_save + 1, column):
                    self._board[row][item] = current

        # change above
        if self._board[row - 1][column] == not_current:
            row_save = row - 1
            while self._board[row_save][column] == not_current:
                row_save -= 1
            if self._board[row_save][column] == current:
                for item in range(row_save + 1, row):
                    self._board[item][column] = current

        # change below
        if self._board[row + 1][column] == not_current:
            row_save = row + 1
            while self._board[row_save][column] == not_current:
                row_save += 1
            if self._board[row_save][column] == current:
                for item in range(row + 1, row_save):
                    self._board[item][column] = current

        # change lower right
        if self._board[row + 1][column + 1] == not_current:
            row_save = row + 1
            column_save = column + 1
            while self._board[row_save][column_save] == not_current:
                row_save += 1
                column_save += 1
            if self._board[row_save][column_save] == current:
                for num in range(1, row_save - row):
                    self._board[row + num][column + num] = current

        # change upper left
        if self._board[row - 1][column - 1] == not_current:
            row_save = row - 1
            column_save = column - 1
            while self._board[row_save][column_save] == not_current:
                row_save -= 1
                column_save -= 1
            if self._board[row_save][column_save] == current:
                for num in range(1, row - row_save):
                    self._board[row - num][column - num] = current

        # change upper right
        if self._board[row - 1][column + 1] == not_current:
            row_save = row - 1
            column_save = column + 1
            while self._board[row_save][column_save] == not_current:
                row_save -= 1
                column_save += 1
            if self._board[row_save][column_save] == current:
                for num in range(1, row - row_save):
                    self._board[row - num][column + num] = current

        # change lower left
        if self._board[row + 1][column - 1] == not_current:
            row_save = row + 1
            column_save = column - 1
            while self._board[row_save][column_save] == not_current:
                row_save += 1
                column_save -= 1
            if self._board[row_save][column_save] == current:
                for num in range(1, row_save - row):
                    self._board[row + num][column - num] = current
        return self._board

    def play_game(self, player_color, piece_position):
        """
        Determines if player_color is a valid option, then determines if piece_position is
        within the list of valid moves for that piece color based on the current board by calling the
        return_available_positions method. If move is not valid, returns the list of valid moves.
        If a valid move is selected, calls on make_move method to place the piece and
        change the board accordingly. Then checks if the board is filled and if it is, calls on
        return_winner method to count the pieces on the board and find out who the winner is.
        """
        if player_color.lower() != 'black' and player_color.lower() != 'white':
            print("Not a valid piece color")
        if piece_position in self.return_available_positions(player_color):
            self.make_move(player_color, piece_position)
        else:
            print(f"Here are the valid moves:{self.return_available_positions(player_color)}")
            return "Invalid move"
        space_count = 0
        for row in self._board:
            for item in row:
                if item == '.':
                    space_count += 1
        if space_count == 0:
            print(self.return_winner())


def get_players(game):
    game.create_player(input("Name of White Player: "), "white")
    game.create_player(input("Name of Black Player: "), "black")


def game_start(game):
    space_count = 60
    player = 'black'
    game.print_board()
    while space_count > 0:
        print(game.return_available_positions(player))
        myStr = input(f'{player} player pick a position: ')
        myStr = myStr.replace("(", "")
        myStr = myStr.replace(")", "")
        myStr = myStr.replace(",", " ")
        myList = myStr.split()
        myList = list(map(int, myList))
        myTuple = tuple(myList)
        game.play_game(player, myTuple)
        if player == 'black':
            player = 'white'
        else:
            player = 'black'
        space_count -= 1
        game.print_board()


game = Othello()
get_players(game)
game_start(game)
