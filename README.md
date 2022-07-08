# about this codes
(1)dataanalysis_main.py
This is a code to analyze chi files obtained from measurements at the BL40B2 beamline at SPring-8.
It performs transmittance correction and subtracts the solvent data from the sample data.
The calculation results are obtained as a csv file for each sample.
Absolute scattering intensity correction is not performed.

(2)insitu_analysis.py
This is a code to obtain one scattring profile with opning 2 chi files (sample and solvent) from BL40B2 at the SPring-8.
The solvent data multiplied by the constant you entered. The default is 1.00.

(3)csvmerge.py
This is a code to merge csv files produced by dataanalysis_main.py process.
Select the csv files and save path, you can obtain the merged excel file.
Sometimes, depending on your PC, this code can not work because the deliminator of the selected csv file is different.
By editing l12(---.split()), this code will be able to be used.

(4)data_analysis_4mq.py
This is the code modified "dataanalysis_main.py". The minimum q and maximum q were adjusted. (4 m: min 0.025, max 1.8)[L65]

(5)abs_int_cons.py
This is the code that can calculate the absolute scattering intensity correction constant.

(6)apply_correction.py
This is the code that apply the absolute scattering intensity correction constant to csv files that you selected.

This code can work on Jyupyter Notebook. When you use this, copy and paste on the Jupyter Notebook, please.
