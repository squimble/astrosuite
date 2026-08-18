#!/usr/bin/env python3

import pandas


def search(table, ra_upper, ra_lower, north):
   
    
    data=pandas.read_csv(table)
    if data is None:
        raise ValueError("Empty data table!")
        
    ra=data.loc[:,"ra"]
    if ra is None:
        raise ValueError("RA is not found in table! Check Table columns")
    dec_obj=data.loc[:,"dec"]
    if dec_obj is None:
        raise ValueError("Dec is not found in table! Check Table columns")
    
    ra_capable=data[(ra >= ra_lower) & (ra <= ra_upper)]
    print(ra_capable)
    
    
    dec_northcapable = data[dec_obj > 0]
    dec_southcapable= data[dec_obj < 0]
    print('Found capable targets')
    
    if north is True:
        candidates=pandas.merge(ra_capable, dec_northcapable, on=['ra', 'dec'], how='inner')
        
    
    if north is False:
        candidates = pandas.merge(ra_capable, dec_southcapable, on=['ra','dec'], how='inner')
        
        
    print(candidates)
    save= input("Would you like to save the output? [y/N]")
    if save == "y" or save == 'yes':
        candidates.to_csv("\\xfindoutput.csv")
    else:
        print("Result not saved.")
    
