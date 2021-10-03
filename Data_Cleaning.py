import pandas as pd
import csv

df = pd.read_csv("")
print(df.shape)

del df["Hyperlink"]
del df["Temp_planet_mass"]
del df["Temp_planet_mass"]
del df["Pl_letter"]
del df["Pl_name"]
del df["Pl_controvflag"]
del df["Pl_pnum"]
del df["Pl_orbper"]
del df["Pl_orbpererr1"]
del df["Pl_orbpererr2"]
del df["Pl_orbperlim"]
del df["Pl_orbsmax"]
del df["Pl_orbsmaxerr1"]
del df["Pl_orbsmaxerr2"]
del df["Pl_orbsmaxlim"]
del df["Pl_orbeccen"]
del df["Pl_orbeccenerr1"]
del df["Pl_orbeccenerr2"]
del df["Pl_orbeccenlim"]
del df["Pl_orbinclerr1"]
del df["Pl_orbinclerr2"]
del df["Pl_orbincllim"]
del df["Pl_bmassj"]
del df["Pl_bmassjerr1"]
del df["Pl_bmassjerr2"]
del df["Pl_bmassjlim"]
del df["Pl_bmassprov"]
del df["Pl_radj"]
del df["Pl_radjerr1"]
del df["Pl_radjerr2"]
del df["Pl_radjlim"]
del df["Pl_denserr1"]
del df["Pl_denserr2"]
del df["Pl_denslim"]
del df["Pl_ttvflag"]
del df["Pl_kepflag"]
del df["k2flag"]
del df["Pl_nnotes"]
del df["Ra"]
del df["Dec"]
del df["St_dist"]
del df["St_disterr1"]
del df["St_disterr2"]
del df["St_distslim"]
del df["Gaia_dist"]
del df["Gaia_disterr1"]
del df["Gaia_disterr2"]
del df["Gaia_distlim"]
del df["St_optmag"]
del df["St_optmagerr"]
del df["St_optmaglim"]
del df["St_optband"]
del df["Gaia_gmag"]
del df["Gaia_gmagerr"]
del df["Gaia_gmaglim"]
del df["St_tefferr1"]
del df["St_tefferr2"]
del df["St_tefflim"]
del df["St_masserr1"]
del df["St_masserr2"]
del df["St_tefflim"]
del df["St_masserr1"]
del df["St_masserr2"]
del df["St_masslim"]
del df["St_raderr1"]
del df["St_raderr2"]
del df["St_radlim"]
del df["Rowupdata"]
del df["Pl_facility"]

print(list(df))

df = df.rename({
    'pl_hostname':"Solar_system_name",
    'pl_discmethod':"plant_discovery_method",
    'pl_orbincl':"planet_orbital_inclination",
    'pl_dens':"planet_density",
    'pl_dens':"planet_density",
    'ra_str':"right_ascension",
    'dec_str':"declination",
    'st_mass':"host_mass",
    'st_rad':"host_radius"
}, axis='columns')

df.to_csv('main.csv')