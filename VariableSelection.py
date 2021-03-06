'''
This file has 2 lists: Screen-able variables and Ancillary variables.
Put any of the screenable variables into the appropriate list by MOVING (not just copying)
the variable from the donotinclude list to the best, good, or noscreening list. (noscreening includes the variable)
e.g.:

best=(
  "RelHumSurf",              # Moisture
  "totCldH2OStd",            # Moisture
  "totH2OMWOnlyStd",         # Moisture * not in AIRS (this means if you are working with AIRS rather than AIRH or AIRX2RET, leave this in donotinclude list)
  "CldFrcStd", # Cloud
  "CldFrcTot", # Cloud
  )

and:
ancillary_include = (
  'landFrac_err',        # Ancillary:Full Swath
  'landFrac',            # Ancillary:Full Swath
  )
and then run:
python ./driver.py URL


'''

# GENERAL CONFIGURATION
# ---------------------

DQSS_URL_LOCATION = "https://airsl2.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?"

#DQSS_FORMAT       = "NetCDF"
DQSS_FORMAT = "HDF"

PRODUCT_SHORTNAME = 'AIRS2RET'
#PRODUCT_SHORTNAME = 'AIRX2RET'
#PRODUCT_SHORTNAME = 'AIRH2RET'



# VARIABLE CONFIGURATION: (ancillary is further below)
# ----------------------

best=(
  )
  
good=(
  )

noscreening=(
  )

donotinclude = (
# Moisture:16
  "H2OMMRSurf",              # Moisture
  "H2OMMRSat_liquid",        # Moisture
  "H2OMMRSatLevStd",         # Moisture
  "H2OMMRLevStd",            # Moisture
  "RelHum",                  # Moisture
  "RelHumSurf_liquid",       # Moisture
  "RelHum_liquid",           # Moisture
  "H2OMMRStd",               # Moisture
  "totH2OStd",               # Moisture
  "H2OMMRSat",               # Moisture
  "RelHumSurf",              # Moisture
  "totCldH2OStd",            # Moisture
  "totH2OMWOnlyStd",         # Moisture * not in AIRS
  "H2OMMRSatSurf_liquid",    # Moisture
  "H2OMMRSatLevStd_liquid",  # Moisture
  "H2OMMRSatSurf",           # Moisture

# Temperature:4
  "TSurfStd",      # Temperature
  "TAirStd",       # Temperature
  "TAirMWOnlyStd", # Temperature not in AIRS
  "TSurfAir",      # Temperature

# Cloud:4
  "CldFrcStd", # Cloud
  "CldFrcTot", # Cloud
  "PCldTop",   # Cloud
  "TCldTop",   # Cloud

# Radiation:3
  "olr3x3", # Radiation
  "olr",    # Radiation
  "clrolr", # Radiation

# CO:2
  "CO_total_column", # CO
  "COVMRLevStd",     # CO

# Methane:2
  "CH4VMRLevStd",     # Methane
  "CH4_total_column", # Methane

# Ozone:3
  "O3VMRLevStd", # Ozone
  "O3VMRStd",    # Ozone
  "totO3Std",    # Ozone

# Full Swath:7
  "GP_Surface",       # Full Swath
  "EmisMWStd",        # Full Swath
  "GP_Height",        # Full Swath
  "GP_Tropopause",    # Full Swath
  "emisIRStd",        # Full Swath
  "GP_Height_MWOnly", # Full Swath not in AIRS
  "sfcTbMWStd",       # Full Swath not in AIRS
  )

  
  
  
ancillary_include = (
  )
  
ancillary_donotinclude = (
# Ancillary: Along Track Data Fields:13
  'scan_node_type',  # Ancillary:Along Track
  'glintlat',        # Ancillary:Along Track
  'satpitch',        # Ancillary:Along Track
  'satheight',       # Ancillary:Along Track
  'satyaw',          # Ancillary:Along Track
  'sat_lon',         # Ancillary:Along Track
  'glintgeoqa',      # Ancillary:Along Track
  'moongeoqa',       # Ancillary:Along Track
  'satgeoqa',        # Ancillary:Along Track
  'nadirTAI',        # Ancillary:Along Track
  'sat_lat',         # Ancillary:Along Track
  'satroll',         # Ancillary:Along Track
  'glintlon',        # Ancillary:Along Track
# Ancillary: Full Swath:12
  'solazi',              # Ancillary:Full Swath
  'landFrac_err',        # Ancillary:Full Swath
  'landFrac',            # Ancillary:Full Swath
  'topog',               # Ancillary:Full Swath
  'demgeoqa',            # Ancillary:Full Swath
  'satazi',              # Ancillary:Full Swath
  'topog_err',           # Ancillary:Full Swath
  'sun_glint_distance',  # Ancillary:Full Swath
  'solzen',              # Ancillary:Full Swath
  'ftptgeoqa',           # Ancillary:Full Swath
  'zengeoqa',            # Ancillary:Full Swath
  'satzen',              # Ancillary:Full Swath
# Ancillary: Per Granule:35
  'GP_Surface',                    # Ancillary:Per Granule
  'Tdiff_IR_4CC1',                 # Ancillary:Per Granule
  'CC1_noise_eff_amp_factor',      # Ancillary:Per Granule
  'EmisMWStd',                     # Ancillary:Per Granule
  'GP_Tropopause',                 # Ancillary:Per Granule
  'Surf_Resid_Ratio',              # Ancillary:Per Granule
  'numHingeSurf',                  # Ancillary:Per Granule
  'all_spots_avg',                 # Ancillary:Per Granule
  'Cloud_Resid_Ratio',             # Ancillary:Per Granule
  'Initial_CC_score',              # Ancillary:Per Granule
  'TSurfdiff_IR_4CC1',             # Ancillary:Per Granule
  'CC1_Resid',                     # Ancillary:Per Granule
  'RetQAFlag',                     # Ancillary:Per Granule
  'AMSU_Chans_Resid',              # Ancillary:Per Granule
  'spectral_clear_indicator',      # Ancillary:Per Granule
  'Water_Resid_Ratio',             # Ancillary:Per Granule
  'Tdiff_IR_MW_ret',               # Ancillary:Per Granule
  'Startup',                       # Ancillary:Per Granule
  'Qual_Guess_PSurf',              # Ancillary:Per Granule
  'GP_Height_MWOnly',              # Ancillary:Per Granule
  'MW_ret_used',                   # Ancillary:Per Granule
  'CCfinal_Noise_Amp',             # Ancillary:Per Granule
  'PTropopause',                   # Ancillary:Per Granule
  'retrieval_type',                # Ancillary:Per Granule
  'GP_Height',                     # Ancillary:Per Granule
  'TotCld_4_CCfinal',              # Ancillary:Per Granule
  'CC_noise_eff_amp_factor',       # Ancillary:Per Granule
  'CCfinal_Resid',                 # Ancillary:Per Granule
  'EmisMWStdErr',                  # Ancillary:Per Granule
  'T_Tropopause',                  # Ancillary:Per Granule
  'Temp_Resid_Ratio',              # Ancillary:Per Granule
  'dust_flag',                     # Ancillary:Per Granule
  'TSurfdiff_IR_4CC2',             # Ancillary:Per Granule
  'num_clear_spectral_indicator',  # Ancillary:Per Granule
  )
