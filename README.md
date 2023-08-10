This repository provides code and data to reproduce results of the article
### *Achieving net zero greenhouse gas emissions critical to limit climate tipping risks*

Tessa Möller, Annika (Ernest) Högner, Carl-Friedrich Schleussner, Samuel Bien, Niklas H. Kitzmann, Robin D. Lamboll, Joeri Rogelj, Jonathan F. Donges, Johan Rockström, Nico Wunderling

## Files
_______________

### CODE
*  01_temp_extension.py:			    Python code to produce linearly extended long-term temperature trajectories.
*  02_temp_conversion.py:			    Python code to convert temperature trajectories to .txt input for MAIN_script.py
*  03_monte_carlo_ensemble.py:		Python code to produce the ensemble members to propagate tipping related uncertainties.
*  04_MAIN_script.py:				      Python code to calculate tipping risks.
*  05_overshoots_evaluation.R:		R code to produce tipping risk .csv from MAIN_script output.
*  core                           pycascades model scripts
*  earth_sys                      pycascades model scripts
pycascades is developed at the Potsdam Institute for Climate Impact Research, Potsdam, Germany.
Description paper: N. Wunderling, J. Krönke, V. Wohlfarth, J. Kohler, J. Heitzig, A. Staal, S. Willner, R. Winkelmann, J.F. Donges, [Modelling nonlinear dynamics of interacting tipping elements on complex networks: the PyCascades package](https://link.springer.com/article/10.1140/epjs/s11734-021-00155-4), The European Physical Journal Special Topics (2021).

## DATA
### INPUT data:
*  kyoto_emissions.csv:				    PROVIDEv1.2 emissions
*  tier1_temperature_summary.csv:	PROVIDEv1.2 temperature trajectories
from [Scenario emissions and temperature data for PROVIDE project](https://zenodo.org/record/7194542) (Robin Lamboll, Joeri Rogelj, Carl-Friedrich Schleussner, 2022)

## Required modules
_______________

python:
* numpy
* pandas
* matplotlib
* cycler
* glob
* re
* sys
* os
* scipy
* seaborn
* pyDOE
* time
* itertools
* PyPDF2
* netCDF4
* networkx

R:
* dplyr
* tidyverse


## Description
_______________

The executable scripts need to be run in the indicated order. For execution, `core` and `earth_sys` need to be saved in the same folder as `04_MAIN_script.py`.
This code was implemented in Python 3.9. and R 4.2.1. For each script, it is advised to first check dependencies. 

_________________________
E.A. Högner & T. Möller, 09.08.2023
