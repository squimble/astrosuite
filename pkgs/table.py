#!/usr/bin/env python3

import pandas as pd
from pathlib import Path

def savetoconfig(table_path):
    
    #take the table path and put it in a config file
    table=table_path
    path=Path(table)
    if table is None:
        raise FileNotFoundError("Path doesn't exist! No data")
    if not path.exists():
        raise FileNotFoundError("Path doesn't exist! Directory is nonexistent")
        
    with open('conf.txt', 'w', encoding="UTF-8") as file:
        file.write(table)
        print("Table saved!")
