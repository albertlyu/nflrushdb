#!/usr/bin/env python3
'''
A module for reading Next Gen Stats data
'''
import pandas as pd
import csv

class NextGenStatsReader(object):
    '''
    A class for reading and manipulating Next Gen Stats data in a DataFrame
    '''
    def load_ngs_data_into_dataframe(self, file_path):
        '''
        Load a CSV file of Next Gen Stats data into a DataFrame
        @param {string} file_path, e.g. '/data/train.csv'
        @return {DataFrame}
        '''
        self.ngs_df = pd.read_csv(file_path, low_memory=False)

    def load_ngs_data_into_dict_reader(self, file_path):
        '''
        Load a CSV file of Next Gen Stats data into a DictReader
        @param {string} file_path, e.g. '/data/train.csv'
        @return {DictReader}
        '''
        with open(file_path, newline='') as csvfile:
            return csv.DictReader(csvfile)
        
    def get_positionals_dataframe_for_play(self, play_id):
        '''
        Get each player's positions for a play as a dataframe
        @param {int} play_id
        @return {DataFrame}
        '''
        return self.ngs_df.loc[self.ngs_df['PlayId'] == int(play_id)]
        
    def get_positionals_dict_for_play(self, play_id):
        '''
        Get each player's positions for a play as a dictionary
        @param {int} play_id
        @return {dict<dict>} a dict of each player's positional data as a dict, keyed by NflId
        '''
        play_positionals_df = self.get_positionals_dataframe_for_play(play_id)
        
        play_positionals_dict = dict()
        for index, dict_row in play_positionals_df.iterrows():
            if dict_row['NflId'] not in play_positionals_dict:
                play_positionals_dict[dict_row['NflId']] = dict_row

        return play_positionals_dict

    def __init__(self): 
        '''
        Constructor
        '''
        self.ngs_df = pd.DataFrame()
