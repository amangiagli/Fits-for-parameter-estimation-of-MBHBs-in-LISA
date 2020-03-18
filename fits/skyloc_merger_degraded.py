import fits.fit_formula as fit_formula

def a_coeff_skyloc_merger_below3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [7.1578823069230005E-06,
            -8.6467202099482117E-03,
            1.0889851107678952E-04,
            -5.2486812277782605E-05,
            7.3941751272244785E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_skyloc_merger_above3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [1.7952230425132029E-07,
            -1.3226826518119906E-03,
            2.8349906514609630E-06,
            -1.3283583560120236E-06,
            1.8093040400009963E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_skyloc_below3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [4.0172709991207479E-06,
            -6.1718804978305002E-03,
            6.1867537466533040E-05,
            -2.8982626511057170E-05,
            3.9679798678014946E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [1.9083377724091455E-07,
            -1.3842687614480835E-03,
            2.9425009465900432E-06,
            -1.3818534572957364E-06,
            1.8960515675980485E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [1.1856011095513932E-03,
            9.5322334641475923E-02,
            1.8323876909975487E-02,
            -8.8285240529953728E-03,
            1.2288883482886796E-03
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [7.8837991858108180E-07,
            -2.6902114792208250E-03,
            1.1865082270050338E-05,
            -5.5279773464244965E-06,
            7.4938732115307276E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [3.0982736268392037E-06,
            -5.6313703980323442E-03,
            4.5345692166958698E-05,
            -2.1397963352602028E-05,
            2.9400070010276473E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [2.6576017477481015E-06,
            -4.7654650484827490E-03,
            3.9309052864039642E-05,
            -1.8192811332316016E-05,
            2.4698553815929045E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_below3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [2.1134061070540773E-05,
            1.4029587325612627E-02,
            3.3209477772239414E-04,
            -1.6091371092458802E-04,
            2.2652148482853297E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [2.9474082128350613E-07,
            -1.5462718722277454E-03,
            4.7104645882360045E-06,
            -2.2569836992558167E-06,
            3.1232309094971835E-07
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
