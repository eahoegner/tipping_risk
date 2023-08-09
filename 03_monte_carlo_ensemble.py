from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.25)
from pyDOE import * #function name >>> lhs

#Tipping limits, see Armstrong McKay et al. 2022:
limits_gis  = [0.8, 3.0]  #0.8-3.0 (central: 1.5)
limits_thc  = [1.4, 8.0]  #1.4-8.0 (central: 4.0)
limits_wais = [1.0, 3.0]  #1.0-3.0 (central: 1.5)
limits_amaz = [2.0, 6.0]  #2.0-6.0 (central: 3.5)
limits_nino = [3.0, 6.0]  #3.0-6.0 (central: uncleear)

###################################################
# Probability fraction (PF) increases with tipping from A-->B (see gray boxes in Kriegler et al., 2009)
#TO GIS
pf_wais_to_gis = [0.1, 0.2]  # from PF = [1., 2.]
pf_thc_to_gis = [0.1, 1.]    # from PF = [0.1, 1.]
# TO THC
pf_gis_to_thc = [0.1, 1.]    # from PF = [1., 10.]
pf_nino_to_thc = [0.1, 0.2]  # changed from [0.5, 2.0] due to Lenton & Williams, 2013. It seems that only a stabilizing effect makes sense
                             # from PF = [0.5, 1.]
# unclear link
#pf_wais_to_thc = [0.1, 0.3]  # from PF = [0.3, 3.]
pf_wais_to_thc = [-0.3, 0.3]  # from PF = [0.3, 3.]
# TO WAIS
pf_nino_to_wais = [0.1, 0.5] # from PF = [1., 5.]
pf_thc_to_wais = [0.1, 0.15] # from PF = [1., 1.5]
pf_gis_to_wais = [0.1, 1.0]  # from PF = [1., 10.]
# TO NINO
pf_thc_to_nino = [0.1, 0.2]     # from PF = [1., 2.]
# unclear link
pf_amaz_to_nino = [0.1, 0.15]   # from PF = [0.8, 1.5]
# TO AMAZ
pf_nino_to_amaz = [0.1, 1.]     # from PF = [1., 10.]
# unclear link
#pf_thc_to_amaz = [0.1, 0.4]  # from PF = [1.0, 4.0]
pf_thc_to_amaz = [-0.4, 0.4]  # from PF = [-2.0, 4.0]

###################################################
#Time scale of tipping for the tipping elements (taken from the literature review of D. Armstrong McKay 2021)
tau_gis  = [1000, 15000]         #1000-15000(central: 10.000)      old values: [1000, 15000] 
tau_thc  = [15, 300]             #15-120 (central: 50)             old values: [15, 300]     
tau_wais = [500, 13000]          #500-13000 (central: 2000)        old values: [1000, 13000] 
tau_nino = [25, 200]             #unclear (around 100)             old values: [25, 200]     
tau_amaz = [50, 200]             #50-200 (central: 100)            old values: [50, 200]     

"""
Latin hypercube sampling
Note: These points need a rescaling according to the uncertainty ranges
This can be done by: x_new = lower_lim + (upper_lim - lower_lim) * u[0;1), where u[0;1) = Latin-HC
"""

#we here exclude nino from LHS: dimension reduced by 7
N = 1000

points = np.array(lhs(22-7, samples=N)) #give dimensions and sample size, here shown for a Latin hypercube; (unfortunately not space filling and not orthogonal)

#rescaling function from latin hypercube
def latin_function(limits, rand):
    resc_rand = limits[0] + (limits[1] - limits[0]) * rand
    return resc_rand
    
    
#MAIN

#to exclude nino from LHS: all nino-related parameters are set to 1

array_limits = []
sh_file = []
for i in range(0, len(points)):

    #TIPPING RANGES
    rand_gis = latin_function(limits_gis, points[i][0])
    rand_thc = latin_function(limits_thc, points[i][1])
    rand_wais = latin_function(limits_wais, points[i][2])
    rand_amaz = latin_function(limits_amaz, points[i][3])
    rand_nino = 1 #latin_function(limits_nino, points[i][4])
        

    # PROBABILITY FRACTIONS
    rand_wais_to_gis = latin_function(pf_wais_to_gis, points[i][4])
    rand_thc_to_gis = latin_function(pf_thc_to_gis, points[i][5])
    rand_gis_to_thc = latin_function(pf_gis_to_thc, points[i][6])
    rand_nino_to_thc = 1 #latin_function(pf_nino_to_thc, points[i][8])
    rand_wais_to_thc = latin_function(pf_wais_to_thc, points[i][7])
    rand_nino_to_wais = 1 #latin_function(pf_nino_to_wais, points[i][10])
    rand_thc_to_wais = latin_function(pf_thc_to_wais, points[i][8])
    rand_gis_to_wais = latin_function(pf_gis_to_wais, points[i][9])
    rand_thc_to_nino = 1 #latin_function(pf_thc_to_nino, points[i][13])
    rand_amaz_to_nino = 1 #latin_function(pf_amaz_to_nino, points[i][14])
    rand_nino_to_amaz = 1 #latin_function(pf_nino_to_amaz, points[i][15])
    rand_thc_to_amaz = latin_function(pf_thc_to_amaz, points[i][10])


    #FEEDBACKS
    rand_tau_gis = latin_function(tau_gis, points[i][11])
    rand_tau_thc = latin_function(tau_thc, points[i][12])
    rand_tau_wais = latin_function(tau_wais, points[i][13])
    rand_tau_amaz = latin_function(tau_amaz, points[i][14])
    rand_tau_nino = 1 #latin_function(tau_nino, points[i][21])


    array_limits.append([rand_gis, rand_thc, rand_wais, rand_amaz, rand_nino,
                         rand_wais_to_gis, rand_thc_to_gis, rand_gis_to_thc, rand_nino_to_thc,
                         rand_wais_to_thc, rand_nino_to_wais, rand_thc_to_wais, rand_gis_to_wais,
                         rand_thc_to_nino, rand_amaz_to_nino, rand_nino_to_amaz, rand_thc_to_amaz,
                         rand_tau_gis, rand_tau_thc, rand_tau_wais, rand_tau_nino, rand_tau_amaz])


    sh_file.append(["python /MAIN_script.py $SLURM_NTASKS {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(
                             #insert path
                             rand_gis, rand_thc, rand_wais, rand_amaz, rand_nino,
                             rand_wais_to_gis, rand_thc_to_gis, rand_gis_to_thc, rand_nino_to_thc,
                             rand_wais_to_thc, rand_nino_to_wais, rand_thc_to_wais, rand_gis_to_wais,
                             rand_thc_to_nino, rand_amaz_to_nino, rand_nino_to_amaz, rand_thc_to_amaz,
                             rand_tau_gis, rand_tau_thc, rand_tau_wais, rand_tau_nino, rand_tau_amaz,
                             str(i).zfill(4) )]) #zfill necessary to construct enough folders for monte carlo runs

array_limits = np.array(array_limits)
np.savetxt("lhs_no-nino_1000.txt", sh_file, delimiter=" ", fmt="%s")


#Create .sh file to run on the cluster
sh_file = np.array(sh_file)
np.savetxt("latin_sh_file.txt", sh_file, delimiter=" ", fmt="%s")