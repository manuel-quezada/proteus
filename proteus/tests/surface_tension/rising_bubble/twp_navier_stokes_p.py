from proteus import *
from proteus.default_p import *
from risingBubble import *
from proteus.mprans import RANS3PF

LevelModelType = RANS3PF.LevelModel
if useOnlyVF:
    LS_model = None
else:
    LS_model = 2

#No RANS
Closure_0_model = None
Closure_1_model = None

coefficients = RANS3PF.Coefficients(epsFact=epsFact_viscosity,
                                    sigma=sigma_01,
                                    rho_0 = rho_0,
                                    nu_0 = nu_0,
                                    rho_1 = rho_1,
                                    nu_1 = nu_1,
                                    g=g,
                                    nd=nd,
                                    ME_model=V_model,
                                    PRESSURE_model=PRESSURE_model,
                                    SED_model=SED_model,
                                    VOS_model=VOS_model,
                                    VOF_model=VOF_model,
                                    LS_model=LS_model,
                                    Closure_0_model=Closure_0_model,
                                    Closure_1_model=Closure_1_model,
                                    epsFact_density=epsFact_density,
                                    stokes=False,
                                    useVF=useVF,
                                    useRBLES=useRBLES,
                                    useMetrics=useMetrics,
                                    eb_adjoint_sigma=1.0,
                                    eb_penalty_constant=weak_bc_penalty_constant,
                                    forceStrongDirichlet=ns_forceStrongDirichlet,
                                    turbulenceClosureModel=ns_closure,
                                    movingDomain=movingDomain,
                                    dragAlpha=dragAlpha,
                                    PSTAB=1.0)
                                    #cE=cE,
                                    #cMax=cMax)

#######################
# BOUNDARY CONDITIONS #
#######################
def getDBC_u(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 0.0    

def getDBC_v(x,flag):
    if flag == boundaryTags['top'] and openTop:
        return lambda x,t: 0.0    

def getAFBC_u(x,flag):
    if flag != boundaryTags['top'] or not openTop:
        return lambda x,t: 0.0

def getAFBC_v(x,flag):
    if flag != boundaryTags['top'] or not openTop:
        return lambda x,t: 0.0

def getDFBC_u(x,flag):
    return lambda x,t: 0.0

def getDFBC_v(x,flag):
    return lambda x,t: 0.0

dirichletConditions = {0:getDBC_u,
                       1:getDBC_v}
advectiveFluxBoundaryConditions =  {0:getAFBC_u,
                                    1:getAFBC_v}
diffusiveFluxBoundaryConditions = {0:{0:getDFBC_u},
                                   1:{1:getDFBC_v}}

######################
# INITIAL CONDITIONS #
######################
class AtRest:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return 0.0

initialConditions = {0:AtRest(),
                     1:AtRest()}