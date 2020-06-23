# Fits for parameter estimation of MBHBs in LISA

This repository is intended to contain the data presented in the work arXiv: (insert link) with an additional tutorial to show how these data can be used. <br />
The repository contains several folders and .tar:

## 1. The folder `data` 
contains the median, 68\% and 95\% uncertainties for:
- Sky position <img src="https://render.githubusercontent.com/render/math?math=\Delta \Omega \, [deg^2]"> ('sky_loc.txt')
- Luminosity distance <img src="https://render.githubusercontent.com/render/math?math=\Delta{d_L/d_L}" >  ('dl.txt')
- Chirp mass <img src="https://render.githubusercontent.com/render/math?math=\Delta\mathcal{M}/\mathcal{M}"> ('mchirp.txt')
- Mass-ratio <img src="https://render.githubusercontent.com/render/math?math=\Delta{q/q}"> ('mass_ratio.txt')
- S/N ('SNR.txt')
    
assuming the standard LISA sensitivity curve, as described in Sec.II of (link to arxiv). Refer to the file with ' *_degraded.txt ' for the same quantites computed with the degraded LISA sensitivity. <br />
We report the values at 7 times from coalescence: 1 month, 1 week, 3 days, 1 day, 10 hours, 5 hours and 1 hour.
For the <img src="https://render.githubusercontent.com/render/math?math=\Delta \Omega"> and <img src="https://render.githubusercontent.com/render/math?math=\Delta{d_L/d_L}" > uncertainties we report also the uncertainties at the merger obtained from eq. (12-13). We provide also the S/N for the full signal. <br />
The files 'skyloc.txt', 'dl.txt', 'SNR.txt' are organized in 42 columns as follow: <br />
log10(mtot/msun) - redshift - median (1 month) - median (1 week) -  ... median (1 hour) - median (merger) - 68% lower (1 month)  - ... - 68% lower (merger) - 68% upper (1 month) - ... - 68% upper (merger) - 95% lower (1 month)  ... - 95% lower (merger) - 95% upper (1 month) - ... - 95% upper (merger) 

The files 'mchirp.txt' and 'mass_ratio.txt' are organized in the same way withour the 'merger' columns, i.e. they have 37 columns

## 2. The folder `fits`
contains modules where we already implemented the fits. You can find an application of these formula in the notebook `Fits_tutorial.ipynb`. 
We notice that `the area uncertainties provided by the corresponding formula are in steradians`.

## 3. The `distribution.tar` and `distribution_degr.tar` archive
contain the <img src="https://render.githubusercontent.com/render/math?math=\Delta \Omega \, [deg^2]">, <img src="https://render.githubusercontent.com/render/math?math=\Delta{d_L/d_L}" >, <img src="https://render.githubusercontent.com/render/math?math=\Delta\mathcal{M}/\mathcal{M}">, <img src="https://render.githubusercontent.com/render/math?math=\Delta{q/q}"> and S/N distribution for the whole set of parameters explored at different time from coalescence.  <br />
In each file, we report the fraction of binaries that fall inside each bins for 68% and 95% of the distributions. The files 'area_M#_z#.txt', 'dl_M#_z#.txt' and 'SNR_M#_z#.txt' are organized in 17 columns:  <br />
bin value - 68% (1 month) - ... 68% (1 hour) - 68% (merger) - 95% (1 month) - ... 95% (1 hour) - 95% (merger)

The files 'mchirp_M#_z#.txt' and 'mass_ratio_M#_z#.txt' are organized in the same way withour the 'merger' columns, i.e. they have 15 columns.  <br />

## 3. The folder `table_coefficient`
contains the coefficients necessary for the fitting formula. The file for the fiducial LISA sensitivity curve (i.e. without 'degraded' in the namefile) report the same values of Tab.II-V.
The file for the degraded LISA sensitivity curve follow the same convention.
