import fits.fit_formula as fit_formula

def a_coeff_skyloc_merger_below3e6_median(x_in):
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

def a_coeff_skyloc_merger_above3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [4.0105742774808558E-07,
            -1.9557098210921499E-03,
            6.1166748628918375E-06,
            -2.8451805689862866E-06,
            3.8947118109047233E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_skyloc_below3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [4.0172709991207479E-06,
            -6.1718804978305002E-03,
            6.1867537466533040E-05,
            -2.8982626511057170E-05,
            3.9679798678014946E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [5.5145415474870329E-07,
            -2.2322347424944041E-03,
            8.8740314427311093E-06,
            -4.1826175287778639E-06,
            5.7079900829947835E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [1.1856011095513932E-03,
            9.5322334641475923E-02,
            1.8323876909975487E-02,
            -8.8285240529953728E-03,
            1.2288883482886796E-03
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [4.0121444455956813E-06,
            -5.5971254759373309E-03,
            5.7797748963770305E-05,
            -2.6279879929645963E-05,
            3.5185557311922444E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [3.0982736268392037E-06,
            -5.6313703980323442E-03,
            4.5345692166958698E-05,
            -2.1397963352602028E-05,
            2.9400070010276473E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [2.6576017477481015E-06,
            -4.7654650484827490E-03,
            3.9309052864039642E-05,
            -1.8192811332316016E-05,
            2.4698553815929045E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_below3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [3.3754341339943807E-05,
            1.7219651583441641E-02,
            5.0456507014192331E-04,
            -2.4432449046889377E-04,
            3.4590628167981531E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_95upper(x_in, y_in):
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
    coeff = [a_coeff_skyloc_merger_below3e6_median(x_in),
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
    coeff = [a_coeff_skyloc_merger_above3e6_median(x_in),
            5.4139696739059062E+01,
            2.0274037338727157E+02,
            -2.3033187159984609E+00,
            -2.7111505537129723E+01,
            1.8332395579982519E-01,
            1.2093497363063648E+00,
            -1.3878144502273381E+01,
            1.1879020940083329E-01,
            9.5970289308017875E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68lower(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_68lower(z, y_in),
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
    coeff = [a_coeff_for_skyloc_above3e6_68lower(z, y_in),
            5.2383012525101698E+01,
            1.7579544776391526E+02,
            -2.2473011708272770E+00,
            -2.3352234493700426E+01,
            1.8414206666493138E-01,
            1.0344053207043657E+00,
            -1.3425036490330795E+01,
            1.1019103066994429E-01,
            9.3086080566433260E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_68upper(z, y_in),
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
    coeff = [a_coeff_for_skyloc_above3e6_68upper(z, y_in),
            6.5174733154659251E+01,
            5.1539917705789783E+01,
            -2.5867891984929710E+00,
            -4.2706381788516214E+00,
            1.8536643756894744E-01,
            6.7344573782591510E-02,
            -1.6787863916162323E+01,
            1.5675470207106557E-01,
            1.1507438839858413E+00
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_95lower(z, y_in),
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
    coeff = [a_coeff_for_skyloc_above3e6_95lower(z, y_in),
            5.0407080926548197E+01,
            7.1943914502385738E+01,
            -2.1947181202668098E+00,
            -8.3388904974812128E+00,
            1.7850816214943199E-01,
            3.1292199337816129E-01,
            -1.2830561169578120E+01,
            1.0676461722988417E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_below3e6_95upper(z, y_in),
            8.0239722891400707E+00,
            -2.6738217344490810E+01,
            -7.5152960057193297E-01,
            3.6641603802115332E+00,
            1.6679990589049276E-01,
            -1.5934206247846738E-01,
            -2.3401763812130083E+00,
            -9.8639867404203496E-02,
            2.7180729923504976E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_skyloc_above3e6_95upper(z, y_in),
            7.3023564544480834E+01,
            2.5446457658921628E+02,
            -2.7498333902590368E+00,
            -3.3468223522676325E+01,
            1.9054526097859048E-01,
            1.4641492705075763E+00,
            -1.8995682349328678E+01,
            1.7532205901259790E-01,
            1.3064574469514021E+00
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value
