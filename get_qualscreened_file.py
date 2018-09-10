#!/usr/bin/env python
from __future__ import print_function
import sys
from urlparse import urlparse
import os
import re
import VariableSelection 
from VariableSelection import DQSS_FORMAT
from VariableSelection import PRODUCT_SHORTNAME
from VariableSelection import DQSS_URL_LOCATION
import urllib2
import subprocess

'''
Author: Richard Strub
        richard.f.strub@nasa.gov

Purpose: Creates DQSS URLS by reading a user edited VariableSelection.py
         Then submits them to DQSS for screening
	 Returns the screened file

Synopsis: python ./get_qualscreened_file.py URL

Further documentation at the top of VariableSelection.py

'''

def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)


def wget(url,label):

   cmd = ['wget', '--content-disposition',    \
          '--load-cookies', '~/.urs_cookies', \
	  '--save-cookies', '~/.urs_cookies', \
	  '--auth-no-challenge=on',           \
	  '--keep-session-cookies',           \
	     url  , "-O", label]

   p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
   out = p.communicate()[0]
   print (p.returncode)

def createLabel(filepath):

    label = os.path.basename(filename)
    try:
      m = re.search('(?<=L2.)\w+', label)
    except AttributeError:
      print ("regex failed to find L2 in " + label)
      sys.exit(1) 

    label = label.replace(m.group(0),"QCSUB" + m.group(0).upper())

    if (DQSS_FORMAT == "NetCDF"): 
        label = label.replace(".hdf",".nc")

    return label 

def checkOne(thislist,sublist):
    for var in sublist:
	try:
	   thislist.remove(var)
        except ValueError:
	    print ("[ERROR] Variable: " + var + "'s use has been duplicated in two screening levels " )
	    sys.exit()

def checkAll(screenlist,ancillary_list):
        screenable_master = len(screenlist)
	ancillary_master  = len(ancillary_list)
        checkOne(screenlist,VariableSelection.best) 
        checkOne(screenlist,VariableSelection.good) 
        checkOne(screenlist,VariableSelection.noscreening) 
        checkOne(screenlist,VariableSelection.donotinclude) 
        checkOne(ancillary_list,VariableSelection.ancillary_include) 
        checkOne(ancillary_list,VariableSelection.ancillary_donotinclude)

        missing = 0
        for item in screenlist:
	    eprint ("[ERROR] " + item +  " is missing from screenable variable lists")
	    missing += 1
        for item in ancillary_list:
	    eprint ("[ERROR] " + item +  " is missing from ancillary lists")
	    missing += 1
	if (missing > 0):
            sys.exit()
	
	eprint ("best:                   " + str(len(VariableSelection.best)))
	eprint ("good:                   " + str(len(VariableSelection.good)))
	eprint ("noscreening:            " + str(len(VariableSelection.noscreening)))
	eprint ("donotinclude:           " + str(len(VariableSelection.donotinclude)))
	eprint ("ancillary include:         " + str(len(VariableSelection.ancillary_include)))
	eprint ("ancillary donotinclude:    " + str(len(VariableSelection.ancillary_donotinclude)))
	eprint ("screenable should be:" + str(screenable_master) + \
	" and is:" + str(len(VariableSelection.best) + len(VariableSelection.good) + len(VariableSelection.noscreening) + len(VariableSelection.donotinclude)))
	eprint ("ancillary  should be:" + str(ancillary_master) + \
	" and is:" + str(len(VariableSelection.ancillary_include) + len(VariableSelection.ancillary_donotinclude)))
     
def checkProductAgainstURL(Url):
    
    m = re.search(PRODUCT_SHORTNAME, Url.path)
    if (m == None):   
      print ("launcher failed to find " + PRODUCT_SHORTNAME + " in " +  Url.path)
      print ("Make sure your PRODUCT_SHORTNAME designation corresponds to the granule URL")
      sys.exit(1) 




VariableTypes = ('CO_Variables',
                 'Cloud_Variables',
	         'Radiation_Variables',
		 'Methane_Variables',
		 'Ozone_Variables',
		 'Full_Swath_Data_Fields_Variables',
		 'Temperature_Variables',
		 'Moisture_Variables')

# Which variables are available for screening and which group they belong to. This was retrieved from useperl.pl
VTypeHash = {}
VTypeHash["CO_Variables"] = ("CO_total_column","COVMRLevStd")
VTypeHash["Cloud_Variables"] = ("CldFrcStd","CldFrcTot","PCldTop","TCldTop",)
VTypeHash["Radiation_Variables"] = ("olr3x3","olr","clrolr",)
VTypeHash["Methane_Variables"] = ("CH4VMRLevStd","CH4_total_column",)
VTypeHash["Ozone_Variables"] = ("O3VMRLevStd","O3VMRStd","totO3Std",)
VTypeHash["Full_Swath_Data_Fields_Variables"] = ("GP_Surface","EmisMWStd","GP_Height","GP_Tropopause","GP_Height_MWOnly","emisIRStd",)
#VTypeHash["Full_Swath_Data_Fields_Variables"] = ("GP_Surface","EmisMWStd","GP_Height","GP_Tropopause","GP_Height_MWOnly","sfcTbMWStd","emisIRStd",)
VTypeHash["Temperature_Variables"] = ("TSurfStd","TAirStd","TAirMWOnlyStd","TSurfAir",)
VTypeHash["Moisture_Variables"] = ("H2OMMRStd","H2OMMRLevStd","H2OMMRSat","RelHumSurf","totCldH2OStd","totH2OMWOnlyStd","totH2OStd","RelHum","RelHumSurf_liquid","RelHum_liquid","H2OMMRSatSurf_liquid","H2OMMRSatLevStd_liquid","H2OMMRSatSurf","H2OMMRSurf","H2OMMRSat_liquid","H2OMMRSatLevStd")

# SUPPORTING DATA: Leave these alone: 
support = {}
support["Moisture_Variables"]  = ['H2OMMRLevStd_QC', 'H2OMMRSat_QC', 'H2OMMRSat_liquid_QC', 'H2OMMRStd_QC', 'totCldH2OStd_QC',
           'totH2OMWOnlyStd_QC', 'totH2OStd_QC', 'RelHumSurf_QC', 'RelHum_QC', 'RelHumSurf_liquid_QC', 
           'RelHum_liquid_QC', 'H2OMMRSatSurf_QC', 'H2OMMRSatSurf_liquid_QC', 'H2OMMRSatLevStd_QC' , 'H2OMMRSatLevStd_liquid_QC',
           'H2OMMRSurf_QC', 'pressStd' ]

support["Temperature_Variables"]   = ['TAirMWOnlyStd_QC', 'TAirStd_QC', 'TSurfAir_QC', 'TSurfStd_QC', 'pressStd']
support["Cloud_Variables"]         = ['CldFrcTot_QC', 'CldFrcStd_QC', 'PCldTop_QC', 'TCldTop_QC']
support["Radiation_Variables"]     = [ 'clrolr_QC', 'olr_QC', 'olr3x3_QC' ]
support["CO_Variables"]            = ['COVMRLevStd_QC',  'CO_total_column_QC']
support["Methane_Variables"]       = ['CH4VMRLevStd_QC', 'CH4_total_column_QC' ]
support["Ozone_Variables"]         = [ 'O3VMRStd_QC', 'totO3Std_QC', 'O3VMRLevStd_QC']
support["Full_Swath_Data_Fields_Variables"] = ['EmisMWStd_QC', 'sfcTbMWStd_QC', 'emisIRStd_QC', 'GP_Height_QC', 'GP_Height_MWOnly_QC', 'GP_Surface_QC', 'GP_Tropopause_QC' ]

# SCREENABLE DATA BACKUP LIST
screenable = \
 ["CO_total_column","COVMRLevStd", "CldFrcStd","CldFrcTot","PCldTop","TCldTop", "olr3x3","olr","clrolr", "CH4VMRLevStd","CH4_total_column", "O3VMRLevStd","O3VMRStd","totO3Std", "GP_Surface","EmisMWStd","GP_Height","GP_Tropopause","GP_Height_MWOnly","sfcTbMWStd","emisIRStd", "TSurfStd","TAirStd","TAirMWOnlyStd","TSurfAir", "H2OMMRStd","H2OMMRLevStd","H2OMMRSat","RelHumSurf","totCldH2OStd","totH2OMWOnlyStd","totH2OStd","RelHum","RelHumSurf_liquid","RelHum_liquid","H2OMMRSatSurf_liquid","H2OMMRSatLevStd_liquid","H2OMMRSatSurf","H2OMMRSurf","H2OMMRSat_liquid","H2OMMRSatLevStd"]

# ANCILLARY DATA BACKUP LIST
ancillary = ['AMSU_Chans_Resid', 'CC1_Resid', 'CC1_noise_eff_amp_factor', 'CC_noise_eff_amp_factor', 'CCfinal_Noise_Amp', 'CCfinal_Resid', 'Cloud_Resid_Ratio', 'EmisMWStd', 'EmisMWStdErr', 'GP_Height', 'GP_Height_MWOnly', 'GP_Surface', 'GP_Tropopause', 'Initial_CC_score', 'MW_ret_used', 'PTropopause', 'Qual_Guess_PSurf', 'RetQAFlag', 'Startup', 'Surf_Resid_Ratio', 'TSurfdiff_IR_4CC1', 'TSurfdiff_IR_4CC2', 'T_Tropopause', 'Tdiff_IR_4CC1', 'Tdiff_IR_MW_ret', 'Temp_Resid_Ratio', 'TotCld_4_CCfinal', 'Water_Resid_Ratio', 'all_spots_avg', 'demgeoqa', 'dust_flag', 'ftptgeoqa', 'glintgeoqa', 'glintlat', 'glintlon', 'landFrac', 'landFrac_err', 'moongeoqa', 'nadirTAI', 'numHingeSurf', 'num_clear_spectral_indicator', 'retrieval_type', 'sat_lat', 'sat_lon', 'satazi', 'satgeoqa', 'satheight', 'satpitch', 'satroll', 'satyaw', 'satzen', 'scan_node_type',  'solazi', 'solzen', 'spectral_clear_indicator', 'sun_glint_distance', 'topog', 'topog_err', 'zengeoqa']


checkAll(screenable,ancillary)

# So algorithm is to:
# enable any ancillary
# leaveOut includes DoNotInclude selections but does not specify to remove non-needed supporting variables.
script = []
# THIS URL MAY CHANGE ONE DAY:
script.append(DQSS_URL_LOCATION)
script.append("DATASET_VERSION=006")
script.append("SERVICE=SUBAIRSL2_DQS")

if (DQSS_FORMAT == "NetCDF"): 
    script.append("FORMAT=TmV0Q0RGLw")
else:
    script.append("FORMAT=SERGLw")

script.append("LABEL=MYLABEL")
script.append("VERSION=1.02")
script.append("SHORTNAME=" + PRODUCT_SHORTNAME)
script.append("FILENAME=FILEPATH")
script.append("VARIABLES=LIST")

if (len (sys.argv) <  2):
    eprint ("\nspecify output format using DQSS_FORMAT in VariableSelection.py")
    eprint ("\nexpecting url as argument")
    sys.exit()
url = sys.argv[1]
Url = urlparse(url)
# In our case the path section of the URL is the same as the system filepath
filename = Url.path
label = createLabel(filename)
checkProductAgainstURL(Url)

cgi = ""
for item in script:
    cgi += item 
    cgi += "&" 
cgi = cgi[:-1]    

list = ""


# Include items to be screened:
for item in VariableSelection.best:
    list += item + ".Include.Best,"
for item in VariableSelection.good:
    list += item + ".Include.Good,"
for item in VariableSelection.noscreening:
    list += item + ".Include.NoScreening,"
for item in VariableSelection.donotinclude:
    list += item + ".DoNotInclude,"

already = []
# Include needed supporting variables:
for item in VariableSelection.best:
    for vtype in VariableTypes:

        if item in VTypeHash[vtype]:
	    for var in support[vtype]:
		if var not in already:
	            list += var + ".Include,";
		    already.append(var)
            break
for item in VariableSelection.good:
    for vtype in VariableTypes:

        if item in VTypeHash[vtype]:
	    for var in support[vtype]:
		if var not in already:
	            list += var + ".Include,";
		    already.append(var)
            break
for item in VariableSelection.noscreening:
    for vtype in VariableTypes:

        if item in VTypeHash[vtype]:
	    for var in support[vtype]:
		if var not in already:
	            list += var + ".Include,";
		    already.append(var)
            break


# Include arbitrary ancillary variables:
for item in VariableSelection.ancillary_include:
    list += item + ".Include,"
for item in VariableSelection.ancillary_donotinclude:
    list += item + ".DoNotInclude,"
list = list[:-1]

# Include
cgi = cgi.replace("LIST", list)
cgi = cgi.replace("FILEPATH", filename)
cgi = cgi.replace("MYLABEL", label)

wget(cgi,label)
