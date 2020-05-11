import fits.fit_formula as fit_formula

def a_coeff_skyloc_merger_below3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [7.2225437521936328E-06,
            -8.6325534161662346E-03,
            1.0825666275427051E-04,
            -5.3381002870477316E-05,
            7.5265011587951132E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_skyloc_merger_above3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [4.1226575851527475E-07,
            -1.9554694840180614E-03,
            6.4562824309063027E-06,
            -3.0517421884417350E-06,
            4.1956080811530538E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_skyloc_below3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [3.8523903006309198E-06,
            -6.1674884984842041E-03,
            6.0919605664119766E-05,
            -2.9434404805582135E-05,
            4.1138078077957048E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [5.0101189091321109E-07,
            -2.2314447134803277E-03,
            8.1206115762477879E-06,
            -3.8924236245307105E-06,
            5.4352505373965236E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [1.3067923642536095E-03,
            9.8153075020522618E-02,
            1.7463452861205330E-02,
            -8.1425662968511343E-03,
            1.1070620045096611E-03
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [3.8765537439369987E-06,
            -5.5871510589275012E-03,
            6.2686207669528278E-05,
            -3.1146332533667638E-05,
            4.3487181753038569E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_skyloc_below3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [2.9981087440158299E-06,
            -5.6304546829688490E-03,
            4.6123773253020091E-05,
            -2.2361107228573783E-05,
            3.1382437250201738E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [2.1765354166901616E-06,
            -4.7614136838678069E-03,
            3.3467236598752251E-05,
            -1.5420142333691797E-05,
            2.0973989628512650E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_below3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [3.7429590831910303E-05,
            1.7258659548857434E-02,
            5.2977397108711186E-04,
            -2.5382168553919658E-04,
            3.5731610215945991E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_skyloc_above3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [2.9362077139050405E-07,
            -1.5454117036684941E-03,
            4.3704800453552052E-06,
            -2.0900622539284911E-06,
            2.8565805536544698E-07
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
            1.0676461722988417E-01,
            8.8597637487456993E-01
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
