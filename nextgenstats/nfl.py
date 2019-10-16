#!/usr/bin/env python3
'''
A module for NFL classes
'''
from nextgenstats.constants import GAME_CONSTANTS, PLAY_CONSTANTS, POSITIONAL_CONSTANTS
from nextgenstats.constants import PLAYER_ID, RUSHER_PLAYER_ID, PLAYER_POSITION, POSITIONAL_X, POSITIONAL_Y, POSITIONAL_ORIENTATION, POSITIONAL_ANGLE
from nextgenstats.constants import YARD_LINE, POSSESSION_TEAM, FIELD_POSITION, PLAY_DIRECTION
from nextgenstats.utils import compute_distance

class NgsObject(object):
    '''
    A NgsObject class
    '''
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)

class Game(NgsObject):
    '''
    A Game consists of Drives of Plays between two NFL teams
    '''
    def __init__(self, game, plays): 
        '''
        Game constructor
        @param {dict}       game
        @param {list<dict>} plays
        '''
        for constant in GAME_CONSTANTS:
            self[constant] = game[constant]
        
        self.plays = plays

class Drive(object):
    '''
    A Drive consists of Plays during the duration of an offensive team's possession
    '''
    pass

class Play(NgsObject):
    '''
    A Play consists of Play Positionals for each Player on the field
    '''
    def get_running_back_positional(self):
        '''
        Get the running back's positions for the play
        @return {dict} the running back's positional data as a dict
        '''
        return self.positionals_df.loc[self.positionals_df[PLAYER_ID] == self.positionals_df[RUSHER_PLAYER_ID]].to_dict('r')[0]

    def get_positionals_for_position(self, position):
        '''
        Get the positionals for a particular NFL position for the play
        @return {list<dict>} a list of each player's positional data as a dict for that position
        '''
        return self.positionals_df.loc[self.positionals_df[PLAYER_POSITION] == position].to_dict('r')
    
    def get_distinct_positions(self):
        '''
        Get the positions of the players on the field
        @return {list<string>}
        '''
        return sorted(list(self.positionals_df[PLAYER_POSITION].unique()))
    
    def get_distinct_player_ids(self):
        '''
        Get the player IDs for all the players on the field
        @return {list<string>}
        '''
        return sorted(list(self.positionals.keys()))

    def get_distance_between_two_players(self, player_id_1, player_id_2):
        '''
        Given two player IDs, look up the players on the field and return their distance from one another
        @param   {int} player_id_1
        @param   {int} player_id_2
        @returns {int}
        '''
        if player_id_1 not in self.positionals or player_id_2 not in self.positionals:
            return

        return compute_distance(self.positionals[player_id_1].coordinates, self.positionals[player_id_2].coordinates)

    def __init__(self, positionals_df): 
        '''
        Play constructor
        @param {DataFrame} positionals_df
        '''
        self.positionals_df = positionals_df
        first_positional = positionals_df.iloc[0]
        
        for constant in PLAY_CONSTANTS:
            self[constant] = first_positional[constant]

        self.own_territory = self[POSSESSION_TEAM] == self[FIELD_POSITION]
        self.yards_until_endzone = round(100 - self[YARD_LINE], 2) if self.own_territory else self[YARD_LINE]

        self.positionals = dict()
        for positional in positionals_df.to_dict('r'):
            player_id = positional[PLAYER_ID]
            if player_id not in self.positionals:
                self.positionals[player_id] = Positional(positional)
                self.positionals[player_id].set_adjusted_fields(self.own_territory, self[PLAY_DIRECTION])
    
class Positional(NgsObject):
    '''
    A Positional is an individual Player's positional at a given point of time during a Play
    '''
    def __get_yards_from_endzone(self, own_territory, play_direction):
        '''
        Get the number of yards from the endzone for a positional's coordinate
        @param {boolean} own_territory - whether the play started in the possession team's territory
        @param {string}  play_direction - 'left' (towards home endzone) or 'right' (towards away endzone)
        '''
        adjusted_x_coordinate = self[POSITIONAL_X] - 20 if own_territory else 120 - self[POSITIONAL_X]
        if play_direction == 'left':
            return round(100 - adjusted_x_coordinate, 2)
        else:
            return adjusted_x_coordinate

    def __get_yards_from_home_sideline(self, play_direction):
        '''
        Get the number of yards from the home sideline, or 'left' sideline along the short axis of the field
        @param {string} play_direction - 'left' (towards home endzone) or 'right' (towards away endzone)
        '''
        if play_direction == 'left':
            return round(53.3 - self[POSITIONAL_Y], 2)
        else:
            return self[POSITIONAL_Y]

    def __set_adjusted_coordinates(self, own_territory, play_direction):
        '''
        Set the adjusted positional coordinates given play characteristics
        @param {boolean} own_territory - whether the play started in the possession team's territory
        @param {string}  play_direction - 'left' (towards home endzone) or 'right' (towards away endzone)
        '''
        self.adjusted_positional_x = self.__get_yards_from_endzone(own_territory, play_direction)
        self.adjusted_positional_y = self.__get_yards_from_home_sideline(play_direction)
        self.adjusted_coordinates = (self.adjusted_positional_x, self.adjusted_positional_y)

    def __set_adjusted_angles(self, play_direction):
        '''
        Set the adjusted orientation of player and angle of player motion given the play direction
        @param {string} play_direction - 'left' (towards home endzone) or 'right' (towards away endzone)
        '''
        if play_direction == 'left':
            self.adjusted_orientation = round(180 - self[POSITIONAL_ORIENTATION], 2)
            self.adjusted_angle = round(180 - self[POSITIONAL_ANGLE], 2)
        else:
            self.adjusted_orientation = self[POSITIONAL_ORIENTATION]
            self.adjusted_angle = self[POSITIONAL_ANGLE]

    def set_adjusted_fields(self, own_territory, play_direction):
        '''
        Set the adjusted fields given play characteristics
        @param {boolean} own_territory - whether the play started in the possession team's territory
        @param {string}  play_direction - 'left' (towards home endzone) or 'right' (towards away endzone)
        '''
        self.__set_adjusted_coordinates(own_territory, play_direction)
        self.__set_adjusted_angles(play_direction)

    def __init__(self, positional_dict): 
        '''
        Positional constructor
        @param {dict} positional_dict
        '''
        for constant in POSITIONAL_CONSTANTS:
            self[constant] = positional_dict[constant]

        self.coordinates = (self[POSITIONAL_X], self[POSITIONAL_Y])
