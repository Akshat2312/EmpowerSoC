#!/usr/bin/bash

scriptLoc=/usr/lib/EmpowerSoc

cd ./EmpowerSOC/power
# calling script for running the simulation in Ngspice
perl $scriptLoc"/run_simulation.pl" $@ &> ./$1"_spice_output"

# Storing the final power values in a file
awk '/^total_q/ {print}' $1"_spice_output" >./$1"_result"
awk '/^energy_avg/ {print}' $1"_spice_output" >>./$1"_result"
awk '/^power_avg_absolute/ {print}' $1"_spice_output" >>./$1"_result"
awk '/^power_avg_uw/ {print}' $1"_spice_output" >>./$1"_result"
cd ../../
