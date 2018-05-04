
DQSS_URL_LOCATION = "https://airsl2.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?"

best=(
  )
  
good=(
  )

noscreening=(
  )

donotinclude = (
# Moisture
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
  "H2OMMRSatLevStd",

# Temperature
  "TSurfStd",
  "TAirStd",
  "TAirMWOnlyStd",
  "TSurfAir",

# Cloud
  "CldFrcStd",
  "CldFrcTot",
  "PCldTop",
  "TCldTop",

# Radiation
  "olr3x3",
  "olr",
  "clrolr",

# CO
  "CO_total_column",
  "COVMRLevStd",

# Methane
  "CH4VMRLevStd",
  "CH4_total_column",

# Ozone
  "O3VMRLevStd",
  "O3VMRStd",
  "totO3Std",

# Full Swath
  "GP_Surface",
  "EmisMWStd",
  "GP_Height",
  "GP_Tropopause",
  "GP_Height_MWOnly",
  "sfcTbMWStd",
  "emisIRStd",

  )

  
  
  
ancillary_include = (
  )
  
ancillary_donotinclude = (
# Ancillary: Along Track Data Fields
  'nadirTAI', 
  'sat_lat', 
  'satroll', 
  'glintlon', 
  'scan_node_type', 
  'glintlat', 
  'satpitch', 
  'satheight', 
  'satyaw', 
  'sat_lon', 
  'glintgeoqa', 
  'moongeoqa', 
  'satgeoqa', 
# Ancillary: Full Swath
  'demgeoqa', 
  'satazi', 
  'topog_err', 
  'sun_glint_distance', 
  'solazi', 
  'landFrac_err', 
  'landFrac', 
  'topog', 
  'solzen', 
  'ftptgeoqa', 
  'zengeoqa',
  'satzen', 
# Ancillary: Per Granule
  'GP_Surface', 
  'Tdiff_IR_4CC1', 
  'CC1_noise_eff_amp_factor', 
  'EmisMWStd', 
  'GP_Tropopause', 
  'Surf_Resid_Ratio', 
  'numHingeSurf', 
  'all_spots_avg', 
  'Cloud_Resid_Ratio', 
  'Initial_CC_score', 
  'sfcTbMWStd', 
  'TSurfdiff_IR_4CC1', 
  'CC1_Resid',
  'RetQAFlag', 
  'AMSU_Chans_Resid', 
  'spectral_clear_indicator', 
  'Water_Resid_Ratio', 
  'Tdiff_IR_MW_ret', 
  'Startup', 
  'Qual_Guess_PSurf', 
  'GP_Height_MWOnly', 
  'MW_ret_used', 
  'CCfinal_Noise_Amp', 
  'PTropopause', 
  'retrieval_type', 
  'GP_Height', 
  'TotCld_4_CCfinal', 
  'CC_noise_eff_amp_factor', 
  'CCfinal_Resid', 
  'EmisMWStdErr', 
  'T_Tropopause', 
  'Temp_Resid_Ratio', 
  'dust_flag', 
  'TSurfdiff_IR_4CC2', 
  'num_clear_spectral_indicator', 
  )
