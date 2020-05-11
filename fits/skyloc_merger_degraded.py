import fits.fit_formula as fit_formula

def a_coeff_skyloc_merger_below3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [7.6056096475886960E-06,
            -8.6367146844934378E-03,
            1.1424546667596481E-04,
            -5.4315047540263851E-05,
            7.4076508118002494E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_skyloc_merger_above3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [1.9345649019145569E-07,
            -1.3227527430514391E-03,
            3.0423394417990450E-06,
            -1.3958883475969260E-06,
            1.8862040433959365E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_skyloc_below3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [3.7939266704898313E-06,
            -6.1670674471493610E-03,
            6.0194198382476909E-05,
            -2.9131182102626919E-05,
            4.0646187321372521E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [2.1499488514690514E-07,
            -1.3844277619337220E-03,
            3.3005686349098834E-06,
            -1.5338871250012100E-06,
            2.1079237530355295E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [1.3039771972514144E-03,
            9.7881126550369915E-02,
            1.8730455362635824E-02,
            -9.0839482484470942E-03,
            1.2716110601770126E-03
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [8.5865540158545512E-07,
            -2.6880939387556807E-03,
            1.2342398695102516E-05,
            -5.7304694893581139E-06,
            7.8598226879395746E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [3.3913586757000917E-06,
            -5.6339538712064721E-03,
            5.3970517975408306E-05,
            -2.6484567395778357E-05,
            3.7320479151392457E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [2.3884476558898162E-06,
            -4.7629557501448535E-03,
            3.5774444946863561E-05,
            -1.6447341066474102E-05,
            2.1912714718263290E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_below3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [2.0612836039083996E-05,
            1.4078904613131438E-02,
            3.0195143085003106E-04,
            -1.3278174360263346E-04,
            1.7254150864555516E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [1.4997584959197871E-06,
            -3.7025570606378029E-03,
            2.4659069978713066E-05,
            -1.1010680408451089E-05,
            1.4857892587798124E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def median_below3e6(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_skyloc_merger_below3e6_degr_median(x_in),
            1.3296116396911980E+01,
            6.2096760851946058E+01,
            -8.5798025867388283E-01,
            -1.1402684996826045E+01,
            1.6077059513921377E-01,
            6.8075075339525171E-01,
            -4.1001717499017021E+00,
            -7.2509794586645304E-02,
            4.1190128228801459E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def median_above3e6(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_skyloc_merger_above3e6_degr_median(x_in),
            6.1574445809100126E+01,
            3.0935442439267888E+02,
            -2.3909627635172246E+00,
            -4.2565600886886116E+01,
            1.7985780973681864E-01,
            1.9545561448840090E+00,
            -1.6106488800626103E+01,
            1.3530578101873214E-01,
            1.1257975106112195E+00
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68lower(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_degr_68lower(z, y_in),
            1.4386277830172427E+01,
            8.6261786592532800E+01,
            -8.3586849513691619E-01,
            -1.5597796491034515E+01,
            1.5759325741274299E-01,
            9.1963038020206511E-01,
            -4.5106749897604645E+00,
            -7.2579291047361494E-02,
            4.4772604482740785E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_above3e6_68lower(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_above3e6_degr_68lower(z, y_in),
            6.3970311290673905E+01,
            2.9393990453742407E+02,
            -2.3233971566489267E+00,
            -4.0280153633184661E+01,
            1.7873040109502147E-01,
            1.8411889094542673E+00,
            -1.6827182589256882E+01,
            1.2665029688878970E-01,
            1.1791258815435626E+00
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_degr_68upper(z, y_in),
            1.1922448690611969E+01,
            -3.7036536669376927E+00,
            -7.9455679270077761E-01,
            -1.6784877396772702E-02,
            1.6128787281388313E-01,
            3.1798285335073118E-02,
            -3.6714511491137243E+00,
            -8.5330786602052955E-02,
            3.8199330752361593E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_above3e6_degr_68upper(z, y_in),
            6.7450905097111956E+01,
            1.3819142326142190E+02,
            -2.6731418533053413E+00,
            -1.7207801518911346E+01,
            1.9047729287381054E-01,
            7.0920375683479620E-01,
            -1.7560439599623209E+01,
            1.6386767843716754E-01,
            1.2177020183874276E+00
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_degr_95lower(z, y_in),
            1.6513117533321150E+01,
            9.3582497152863795E+01,
            -8.4731820115731504E-01,
            -1.6759443916427372E+01,
            1.5216261343165871E-01,
            9.7877070714543279E-01,
            -5.2654786870017647E+00,
            -6.4074701191568106E-02,
            5.1155957435754829E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_above3e6_degr_95lower(z, y_in),
            5.0407080926548197E+01,
            7.1943914502385738E+01,
            -2.1947181202668098E+00,
            -8.3388904974812128E+00,
            1.7850816214943199E-01,
            3.1292199337816129E-01,
            -1.2830561169578120E+01,
            1.0676461722988417E-01,
            8.8597637487456993E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_degr_95upper(z, y_in),
            9.0332804750900539E+00,
            -3.3947168782109820E+01,
            -7.0405297996251370E-01,
            4.9541352732663952E+00,
            1.6830342860175707E-01,
            -2.3520557724655511E-01,
            -2.7586526748454618E+00,
            -1.0972654692075579E-01,
            3.1576565029343673E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_above3e6_degr_95upper(z, y_in),
            7.0247514213503038E+01,
            9.0988261559806077E+01,
            -2.7325415231281207E+00,
            -9.9634597686428652E+00,
            1.9891383119594153E-01,
            3.4346371457591829E-01,
            -1.8261081587824538E+01,
            1.6357992328786608E-01,
            1.2634603370890112E+00
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value
