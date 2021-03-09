# -*- coding: utf-8 -*-
import pandas as pd
from __future__ import print_function
from argparse import ArgumentParser, Action
import os

class Parameters(Action):
    @staticmethod
    def parse_parameters():
        # required = True, then if no arguments then throws error and shows help
        parser = ArgumentParser(description='all things about the files')
        parser.add_argument("--path", 
                            help="please upload or attach the file or dir")
        return vars(parser.parse_args())


class Regress(object):
    def __init__(self):
        self.params = Parameters.parse_parameters()
        return
    
    def read_files(self, dirname, num=0):
        # IF ONLY ONE FILE
        if num == 1:
            files = pd.read_csv(dirname)
            return files
        
        # ELSE ALL FILES
        files = []
        for file in os.listdir(dirname):
            files.append(pd.read_csv(file))
        
        # MERGE
        merge = input("Do you want to merge files?")
        if merge == "Yes":
            files = pd.concat(files)
        else:
            pass
        
        return files
    
    def read_pathname(self, pathname):
        # IS DIR
        if os.path.isdir(pathname): 
            data = self.read_files(pathname)
        # IS FILE
        elif os.path.isfile(pathname):
            data = self.read_file(pathname, 1)
        # IS UNRECOGNIZED
        else:
            print("The uploaded data is not a file or folder.")
            raise Exception
        return data
    
    def get_new_columns(self, columns, data):
        print(columns)
        new_columns = {columns[i]: columns[i] for i in range(len(columns))} 
        edit = input("Edit or continue?")
        if edit == "continue":
            return new_columns
        
        
        
        for col in new_columns.keys():
            new_name = input("Input new column name or pass")
            if new_name != None:
                new_columns[col] = new_name
        
        return new_columns
    
    def rename_columns(self, data):
        try:
            column_names = self.rename_columns(data.columns, data.head())
            data.rename(columns = column_names)

        except:
            for df in data:
                column_names = self.rename_columns(df.columns, df.head())
                df.rename(columns = column_names)
        return data
    
    def main(self):
        pathname = self.param['dir']
        data = self.read_pathname(pathname)
        data = self/rename_columns(data)
        
        
        
        
        
        
