class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, '_title'):
            print('title is already set')
            return    
        if not isinstance(new_title, str):
            print('title must be string')
            return
        if len(new_title) == 0:
            print('title must be string > 0 chars')
            return
        self._title = new_title

    def results(self):
        result_list = []
        for result in Result.all:
            if result.game is self:
                result_list.append(result)
        return result_list

    def players(self):
        player_list = []
        for result in self.results():
            player_list.append(result.player)
        return list(set(player_list))

    def average_score(self, player):
        total = 0
        count = 0
        for result in self.results():
            if result.player is player:
                total += result.score
                count += 1
        return total / count


    def __repr__(self):
        return f'<Game {self.title}>'

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        # if isinstance(new_username, str) and len(new_username) >=2 and len(new_username <= 16):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            print('error username')

    def results(self):
        result_list = []
        for result_obj in Result.all:
            if result_obj.player is self:
                result_list.append(result_obj)
        return result_list
        # return [result_obj for result_obj in Result.all if result_obj.player is self]

    def games_played(self):
        games = []
        for result in self.results():
            games.append(result.game)
        return list(set(games))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for result in self.results():
            if result.game is game:
                count += 1
        return count
                
    def __repr__(self):
        return f'<Player {self.username}>'

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if hasattr(self, '_score'):
            print('score has already been set')
            return
        if not isinstance(new_score, int):
            print('score must be integer')
            return
        if not (1 <= new_score <= 5000):
            print('must be between 1 < 5000')
            return
        self._score = new_score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            print('invalid player')

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            print('invalid game')

    def __repr__(self):
        return f'<Result (self.score), {self.game.title}, {self.player.username}>'