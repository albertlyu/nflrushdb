#!/usr/bin/env python3
'''
A module for handy utils
'''
import math

def get_game_id_from_play_id(play_id):
    '''
    A util to get a game_id from a play_id, simple string splitting
    @param  {string} play_id
    @return {string} game_id
    '''
    return play_id[0:10]

def compute_distance(coordinates_1, coordinates_2):
    '''
    Compute the distance between two sets of coordinates
    @param  {tuple<int>} coordinates_1
    @param  {tuple<int>} coordinates_2
    @return {int}
    '''
    return math.sqrt((coordinates_2[1] - coordinates_1[1])**2 + (coordinates_2[0] - coordinates_1[0])**2)
