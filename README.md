# Analytic parameter estimation for MBHBs in LISA

This repository is intended to contain the data presented in the work arXiv: (insert link) with an additional tutorial to show how these data can be used. <br />
The repository contains several folders:

1. The folder `data` contain the median, $68\%$ and $95\%$ uncertainties for:
    - Sky position $$\Delta Omega$$ ('skyloc.txt')
    - Luminosity distance $d_L$ ('dl.txt')
    - Chirp mass $\mathcal{M}$ ('mchirp.txt')
    - Mass-ratio $q$ ('mass_ratio.txt')
    - S/N ('SNR.txt')
    
assuming the standard LISA sensitivity curve, as described in Sec.II of (link to arxiv). Refer to the file with ' *_degraded.txt ' for the same quantites computed with the degraded LISA sensitivity. <br />
We report these values at 7 times from coalescence: 1 month, 1 week, 3 days, 1 day, 10 hours, 5 hours and 1 hour.
For the $\Delta Omega$ and $d_L$ we report also the uncertainties at the merger obtained from eq. (12-13). WE provide also the S/N for the full signal.
The files 'skyloc.txt', 'dl.txt' and 'SNR.txt' are organized in (METTERE IL NUMERO) columns as follow:
log10(mtot/msun) - redshift - 


