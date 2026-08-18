#!/usr/bin/env python3

import pandas as pd
#thank you Caltech!
from astroquery.ipac.irsa import Irsa
#thanks CDS!
from astroquery.vizier import Vizier
import astropy.units as u 
from astropy.coordinates import SkyCoord

def IRSA_search(mission, ra, dec, radius):
    
    spatial="Cone"
    
    coord = SkyCoord(ra, dec, unit="deg", frame="galactic")
    catalogs=Irsa.list_catalogs(filter=mission)
    print("Catalogs for selected Mission (must choose one)")
    selected_catalog=input(catalogs)
    table = Irsa.query_region(coordinates=coord, spatial=spatial, catalog=selected_catalog, radius=radius * u.arcmin)
    print(table)
    df = table.to_df('pandas')
    save= input("Would you like to save the output? [y/N]")
    if save == "y" or save == 'yes':
        df.to_csv("/home/dylanw/AstroSuite/querioutput.csv")
    else:
        print("Result not saved.")
        
#def VizieR_search(mission, ra, dec, radius):
    
    
     #catalog= Vizier.find_catalogs(f"mission:{mission}")
     #print("Select a catalog")
     #selected_catalog=input(catalog)
     #coord = SkyCoord(ra, dec, unit="deg", frame="galactic")
     #v = Vizier(row_limit=-1)

     
     #table = v.query_region(coordinates=coord, catalog=selected_catalog, radius=radius * u.arcmin)
     #tables=table[0].pprint_all()
     
     #df = pd.DataFrame(tables)
     #save= input("Would you like to save the output? [y/N]")
     #if save == "y" or save == 'yes':
         #df.to_csv("/home/dylanw/AstroSuite/querioutput.csv")
     #else:
         #print("Result not saved.")