
import sys
from urlparse import urlparse
import os
import re

def createLabel(filepath):

    label = os.path.basename(filename)
    try:
      m = re.search('(?<=L2.)\w+', label)
    except AttributeError:
      print "regex failed to find L2 in " + label 
      sys.exit(1) 

    label = label.replace(m.group(0),"QCSUB" + m.group(0).upper())
    return label 

# Which variables are available for screening and which group they belong to. This was retrieved from useperl.pl
hash = {}
hash["CO_Variables"] = {"CO_total_column":1,"COVMRLevStd":1}
hash["Cloud_Variables"] = ("CldFrcStd","CldFrcTot","PCldTop","TCldTop",)
hash["Radiation_Variables"] = ("olr3x3","olr","clrolr",)
hash["Methane_Variables"] = ("CH4VMRLevStd","CH4_total_column",)
hash["Ozone_Variables"] = ("O3VMRLevStd","O3VMRStd","totO3Std",)
hash["Full_Swath_Data_Fields_Variables"] = ("GP_Surface","EmisMWStd","GP_Height","GP_Tropopause","GP_Height_MWOnly","sfcTbMWStd","emisIRStd",)
hash["Temperature_Variables"] = ("TSurfStd","TAirStd","TAirMWOnlyStd","TSurfAir",)
hash["Moisture_Variables"] = ("H2OMMRStd","H2OMMRLevStd","H2OMMRSat","RelHumSurf","totCldH2OStd","totH2OMWOnlyStd","totH2OStd","RelHum","RelHumSurf_liquid","RelHum_liquid","H2OMMRSatSurf_liquid","H2OMMRSatLevStd_liquid","H2OMMRSatSurf","H2OMMRSurf","H2OMMRSat_liquid","H2OMMRSatLevStd")

# SUPPORTING DATA: Leave these alone: 
support = {}
support["Moisture_Variables"]  = ('H2OMMRLevStd_QC', 'H2OMMRSat_QC', 'H2OMMRSat_liquid_QC', 'H2OMMRStd_QC', 'totCldH2OStd_QC',
           'totH2OMWOnlyStd_QC', 'totH2OStd_QC', 'RelHumSurf_QC', 'RelHum_QC', 'RelHumSurf_liquid_QC', 
           'RelHum_liquid_QC', 'H2OMMRSatSurf_QC', 'H2OMMRSatSurf_liquid_QC', 'H2OMMRSatLevStd_QC' , 'H2OMMRSatLevStd_liquid_QC',
           'H2OMMRSurf_QC', 'pressStd' )
Temperature = ['TAirMWOnlyStd_QC', 'TAirStd_QC', 'TSurfAir_QC', 'TSurfStd_QC', 'pressStd'],
Cloud       =  ['CldFrcTot_QC', 'CldFrcStd_QC', 'PCldTop_QC', 'TCldTop_QC'],
Radiation = [ 'clrolr_QC', 'olr_QC', 'olr3x3_QC' ],
support["CO_Variables"]       = ('COVMRLevStd_QC',  'CO_total_column_QC')
Methane   = ['CH4VMRLevStd_QC', 'CH4_total_column_QC' ],
Full_Swath_Data_Fields = ['EmisMWStd_QC', 'sfcTbMWStd_QC', 'emisIRStd_QC', 'GP_Height_QC', 'GP_Height_MWOnly_QC', 'GP_Surface_QC', 'GP_Tropopause_QC' ],
Ozone = [ 'O3VMRStd_QC', 'totO3Std_QC', 'O3VMRLevStd_QC']

# SCREENABLE DATA BACKUP LIST
screenable = \
 ("CO_total_column","COVMRLevStd", "CldFrcStd","CldFrcTot","PCldTop","TCldTop", "olr3x3","olr","clrolr", "CH4VMRLevStd","CH4_total_column", "O3VMRLevStd","O3VMRStd","totO3Std", "GP_Surface","EmisMWStd","GP_Height","GP_Tropopause","GP_Height_MWOnly","sfcTbMWStd","emisIRStd", "TSurfStd","TAirStd","TAirMWOnlyStd","TSurfAir", "H2OMMRStd","H2OMMRLevStd","H2OMMRSat","RelHumSurf","totCldH2OStd","totH2OMWOnlyStd","totH2OStd","RelHum","RelHumSurf_liquid","RelHum_liquid","H2OMMRSatSurf_liquid","H2OMMRSatLevStd_liquid","H2OMMRSatSurf","H2OMMRSurf","H2OMMRSat_liquid","H2OMMRSatLevStd")

# ANCILLARY DATA BACKUP LIST
ancillary = ('AMSU_Chans_Resid', 'CC1_Resid', 'CC1_noise_eff_amp_factor', 'CC_noise_eff_amp_factor', 'CCfinal_Noise_Amp', 'CCfinal_Resid', 'Cloud_Resid_Ratio', 'EmisMWStd', 'EmisMWStdErr', 'GP_Height', 'GP_Height_MWOnly', 'GP_Surface', 'GP_Tropopause', 'Initial_CC_score', 'MW_ret_used', 'PTropopause', 'Qual_Guess_PSurf', 'RetQAFlag', 'Startup', 'Surf_Resid_Ratio', 'TSurfdiff_IR_4CC1', 'TSurfdiff_IR_4CC2', 'T_Tropopause', 'Tdiff_IR_4CC1', 'Tdiff_IR_MW_ret', 'Temp_Resid_Ratio', 'TotCld_4_CCfinal', 'Water_Resid_Ratio', 'all_spots_avg', 'demgeoqa', 'dust_flag', 'ftptgeoqa', 'glintgeoqa', 'glintlat', 'glintlon', 'landFrac', 'landFrac_err', 'moongeoqa', 'nadirTAI', 'numHingeSurf', 'num_clear_spectral_indicator', 'retrieval_type', 'sat_lat', 'sat_lon', 'satazi', 'satgeoqa', 'satheight', 'satpitch', 'satroll', 'satyaw', 'satzen', 'scan_node_type', 'sfcTbMWStd', 'solazi', 'solzen', 'spectral_clear_indicator', 'sun_glint_distance', 'topog', 'topog_err', 'zengeoqa')



best=(
"COVMRLevStd",
)
good=(
"CO_total_column",
)
noscreening=(
"CO_total_column",
)
screenable_edit = (
"CldFrcStd",
"CldFrcTot",
"PCldTop",
"TCldTop",
"olr3x3",
"olr",
"clrolr",
"CH4VMRLevStd",
"CH4_total_column",
"O3VMRLevStd",
"O3VMRStd",
"totO3Std",
"GP_Surface",
"EmisMWStd",
"GP_Height",
"GP_Tropopause",
"GP_Height_MWOnly",
"sfcTbMWStd",
"emisIRStd",
"TSurfStd",
"TAirStd",
"TAirMWOnlyStd",
"TSurfAir",
"H2OMMRStd",
"H2OMMRLevStd",
"H2OMMRSat",
"RelHumSurf",
"totCldH2OStd",
"totH2OMWOnlyStd",
"totH2OStd",
"RelHum",
"RelHumSurf_liquid",
"RelHum_liquid",
"H2OMMRSatSurf_liquid",
"H2OMMRSatLevStd_liquid",
"H2OMMRSatSurf",
"H2OMMRSurf",
"H2OMMRSat_liquid", 
"H2OMMRSatLevStd")



ancillary_include = (
'AMSU_Chans_Resid', 
'CC1_Resid', 
'CC1_noise_eff_amp_factor', 
'CC_noise_eff_amp_factor', 
'CCfinal_Noise_Amp', 
'CCfinal_Resid', 
'Cloud_Resid_Ratio', 
'EmisMWStd', 
'EmisMWStdErr', 
'GP_Height', 
)

ancillary_donotinclude = (
'AMSU_Chans_Resid', 
'CC1_Resid', 
'CC1_noise_eff_amp_factor', 
'CC_noise_eff_amp_factor', 
'CCfinal_Noise_Amp', 
'CCfinal_Resid', 
'Cloud_Resid_Ratio', 
'EmisMWStd', 
'EmisMWStdErr', 
'GP_Height', 
'GP_Height_MWOnly', 
'GP_Surface', 
'GP_Tropopause', 
'Initial_CC_score', 
'MW_ret_used', 
'PTropopause', 
'Qual_Guess_PSurf', 
'RetQAFlag', 
'Startup', 
'Surf_Resid_Ratio', 
'TSurfdiff_IR_4CC1', 
'TSurfdiff_IR_4CC2', 
'T_Tropopause', 
'Tdiff_IR_4CC1', 
'Tdiff_IR_MW_ret', 
'Temp_Resid_Ratio', 
'TotCld_4_CCfinal', 
'Water_Resid_Ratio', 
'all_spots_avg', 
'demgeoqa', 
'dust_flag', 
'ftptgeoqa', 
'glintgeoqa', 
'glintlat', 
'glintlon', 
'landFrac', 
'landFrac_err', 
'moongeoqa', 
'nadirTAI', 
'numHingeSurf', 
'num_clear_spectral_indicator', 
'retrieval_type', 
'sat_lat', 
'sat_lon', 
'satazi', 
'satgeoqa', 
'satheight', 
'satpitch', 
'satroll', 
'satyaw', 
'satzen', 
'scan_node_type', 
'sfcTbMWStd', 
'solazi', 
'solzen', 
'spectral_clear_indicator', 
'sun_glint_distance', 
'topog', 
'topog_err', 
'zengeoqa')


# So algorithm is to:
# enable any ancillary
# leaveOut includes DoNotInclude selections but does not specify to remove non-needed supporting variables.
script = []
script.append("http://airsl2.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?")
script.append("DATASET_VERSION=006")
script.append("SERVICE=SUBAIRSL2_DQS")
script.append("FORMAT=SERGLw")
script.append("LABEL=MYLABEL")
script.append("VERSION=1.02")
script.append("SHORTNAME=AIRX2RET")
script.append("FILENAME=FILEPATH")
script.append("VARIABLES=LIST")

if (len (sys.argv) <  2):
    print "expecting url as argument"
    sys.exit()
url = sys.argv[1]
Url = urlparse(url)
# In our case the path section of the URL is the same as the system filepath
filename = Url.path
label = createLabel(filename)

cgi = ""
for item in script:
    cgi += item 
    cgi += "&" 
cgi = cgi[:-1]    

list = ""

# Include items to be screened:
for item in best:
    list += item + ".Include.Best,"
for item in good:
    list += item + ".Include.Good,"
for item in noscreening:
    list += item + ".Include.NoScreening,"

# Include needed supporting variables:
for item in best:
    if hash['CO_Variables'].has_key(item):
	for var in support['CO_Variables']:
	    list += var + ".Include,";
        break


# Include arbitrary ancillary variables:
for item in ancillary_include:
    list += item + ".Include,"
for item in ancillary_donotinclude:
    list += item + ".DoNotInclude,"
list = list[:-1]

# Include
cgi = cgi.replace("LIST", list)
cgi = cgi.replace("FILEPATH", filename)
cgi = cgi.replace("MYLABEL", label)

print cgi
