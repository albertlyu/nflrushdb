#!/usr/bin/env python3
'''
A module for NFL classes
'''
import pandas as pd

from nextgenstats.constants import PLAY_CONSTANTS, PLAY_POSITIONAL_CONSTANTS, PLAYER_ID, RUSHER_PLAYER_ID, PLAYER_POSITION, POSITIONAL_X, POSITIONAL_Y
from nextgenstats.utils import compute_distance

class Game(object):
    '''
    A Game consists of Drives of Plays between two NFL teams
    '''
    pass

class Drive(object):
    '''
    A Drive consists of Plays during the duration of an offensive team's possession
    '''
    pass

class Play(object):
    '''
    A Play consists of Play Positionals for each Player on the field
    '''
    def get_running_back_positional(self):
        '''
        Get the running back's positions for the play
        @return {dict} the running back's positional data as a dict
        '''
        return self.play_positionals_df.loc[self.play_positionals_df[PLAYER_ID] == self.play_positionals_df[RUSHER_PLAYER_ID]].to_dict('r')[0]

    def get_positionals_for_position(self, position):
        '''
        Get the positionals for a particular NFL position for the play
        @return {list<dict>} a list of each player's positional data as a dict for that position
        '''
        return self.play_positionals_df.loc[self.play_positionals_df[PLAYER_POSITION] == position].to_dict('r')
    
    def get_distinct_positions(self):
        '''
        Get the positions of the players on the field
        @return {list<string>}
        '''
        return sorted(list(self.play_positionals_df[PLAYER_POSITION].unique()))
    
    def get_distinct_player_ids(self):
        '''
        Get the player IDs for all the players on the field
        @return {list<string>}
        '''
        return sorted(list(self.play_positionals.keys()))

    def get_distance_between_two_players(self, player_id_1, player_id_2):
        '''
        Given two player IDs, look up the players on the field and return their distance from one another
        @param   {int} player_id_1
        @param   {int} player_id_2
        @returns {int}
        '''
        if player_id_1 not in self.play_positionals or player_id_2 not in self.play_positionals:
            return

        return compute_distance(self.play_positionals[player_id_1].coordinates, self.play_positionals[player_id_2].coordinates)

    def __init__(self, play_positionals_df): 
        '''
        Play constructor
        '''
        first_play_positional = play_positionals_df.iloc[0]
        self.play_positionals_df = play_positionals_df
        self.play_positionals = dict()
        for play_positional in play_positionals_df.to_dict('r'):
            player_id = play_positional[PLAYER_ID]
            if player_id not in self.play_positionals:
                self.play_positionals[player_id] = PlayPositional(play_positional)

        for constant in PLAY_CONSTANTS:
            self[constant] = first_play_positional[constant]

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)
    
class PlayPositional(object):
    '''
    A PlayPositional is an individual Player's positional at a given point of time during a Play
    '''
    def __init__(self, play_positional_dict): 
        '''
        PlayPositional constructor
        '''
        for constant in PLAY_POSITIONAL_CONSTANTS:
            self[constant] = play_positional_dict[constant]

        self.coordinates = (self[POSITIONAL_X], self[POSITIONAL_Y])
    
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)
