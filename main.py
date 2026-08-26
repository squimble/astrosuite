#!/usr/bin/env python3

#import the packages
import argparse
import pkgs.xfind as xfind
import pkgs.xtable as xtable
import pkgs.queri as queri

parser=argparse.ArgumentParser(description="Suite of astronomy-research focused tools, launchable via terminal")
parser.add_argument("--xfind",action="store_true",help="Tool to help find whether an object fits within a Right Ascension and Declination limit.")
parser.add_argument("--xtable",action="store_true",help="Table Management tool to globalize tables across AstroSuite Python programs (will not work with included Java JRE programs)")
parser.add_argument("--queri",action="store", choices=["IRSA"], help="Built-in Querying system, supporting IRSA.")

args= parser.parse_args()

print(args.xfind)
print(args.xtable)
print(args.queri)

if args.xfind is True:
    table=input("Table Path? (.csv) [if already in XTables, then skip\n")
    if "conf.txt" != None:
        print("Xtables file found!")
        with open("conf.txt","r", encoding='utf-8') as file:
            
            table=file.read()
            table=str(table)
            print(table)
            
    if "conf.txt" == None:
        if table != None:
            print("Path given!")
            
        else:
            raise FileNotFoundError("No path given, and no Xtables file found!")
            
    ra_upper=float(input("Upper RA limit in degrees (not HMS)\n"))
    ra_lower=float(input("Lower RA limit in degrees (not HMS)\n"))
    northbool=input("Northern Hemisphere? (y/n)")
    if northbool in ["yes","y"]:
        north=True
    if northbool in ["no",'n']:
        north=False
   # else:
        #raise TypeError("Xfind cannot process any other input for xfind.search.north than yes, y, no, n")
    
    #pass to pkgs.xfind to find objects
    xfind.search(table, ra_upper, ra_lower, north)
    
if args.xtable is True:
    table=input("Table Path? (.csv)\n")
    xtable.savetoconfig(table)
    print("Saved!")

if args.queri is not None:
    # if args.queri == "VizieR":
    #     print("Queri v1.00-r\n")
    #     print("VizieR Mode\n")
    #     mission=input("What VizieR mission do you want to use?\n")
    #     ra=float(input("Right Ascension? (degrees)"))
    #     dec=float(input("Declination? (degrees)"))
    #     radius=float(input("Radius of Search Cone? (arcmin)"))
        
    #     queri.VizieR_search(mission, ra, dec, radius)
        
    if args.queri == "IRSA":
        print("Queri v1.00-r\n")
        print("IRSA Mode\n")
        mission=input("What IRSA mission do you want to use?\nSpitzer\nWISE\nEuclid\nSPHEREx\nIRTF\n2MASS\nZTF\nSOFIA\nPlanck\nHerschel\nIRAS\nMSX\nISO\nSWAS\nAKARI\nCOSMOS\nBLAST\nBOLOCAM\nIRTS\n")
        ra=float(input("Right Ascension? (degrees)"))
        dec=float(input("Declination? (degrees)"))
        radius=float(input("Radius of Search Cone? (arcmin)"))
        
        queri.IRSA_search(mission, ra, dec, radius)

print("Welcome to AstroSuite")
