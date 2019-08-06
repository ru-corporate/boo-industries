import boo
from boo.dataframe.util import industry, sort


# some companies
class COMPANY:
    ferronordic = 5001048893
    e4 = 7720554943
    nami = 7711000924

SUSPICIOUS = [
        7801464198, # neftekom 
        ]

# industry(df, 52, 24)[cols]
    
# groups of companies not in their     
class ALLOC:
    seaport_grain=[
           2315014748,
           2315996886,
           2352044733,
           2315006923,
           2365026121
            ]
    tires=[
           1651000027,
           1651049488,
           2223621728,
           3435900531,
           3663088326,
           4027105304,
           4345465597,
           4703073810,
           4802011710,           
           5047065059,
           5073007462,
           5506007419,
           6674134107,      
           7601001509,
           7703204071,
           7703247653,
           7704787370,
           7706560230,
           7707296796,
           7728629485,
           7816162305,
           ]
    tires_trade=[
            1651024807,
            3664023441,
            7725693620
            ]
    metal=[7449006184]
    auto_specmach=[7710761161]
    auto_component=[5001048893]
    vagon=[1901004997]
    other=[1435196431,
           3711018160,
           7717591053,
           5024097520]
    construction=[
           7719272800,
           7703702341,
           7705892313,
           5024115433,
           7715941922,
           7701716324,
           7708645993,
           7734050262,
           7720554943,
           7705008315,
           3123156420,
           7729564128,
           2457061775,
                  ]    

def named(df, name):
    ix = [str(x) for x in getattr(ALLOC, name)]
    return df.loc[ix,:] 
    

def as_str(xs):
    return [str(x) for x in xs]

    
def combine(*args):    
    return as_str(args)

              
def automotive(df):
    exclude = as_str(SUSPICIOUS) + combine(
                      COMPANY.e4,
                      *ALLOC.construction,
                      *ALLOC.tires,
                      *ALLOC.auto_specmach,
                      *ALLOC.vagon,
                      *ALLOC.metal,
                      *ALLOC.other)
    return industry(df, 29) \
           .append(industry(df, 45)) \
           .drop(exclude, errors='ignore')


def tires(df):    
    return named(df, 'tires')


def tires_prod(df):    
    return tires(df).query('of>0.3')


def tires_dist(df):    
    return tires(df).query('of<=0.3')


def tires_trade(df):    
    return named(df, 'tires_trade')


def seaport_grain(df):
    return named(df, 'seaport_grain')

def grain_trade(df):
    return industry(df, 46, 21) 
    #Торговля оптовая зерном, необработанным табаком, семенами и кормами для сельскохозяйственных животных

if __name__ == "__main__":
    try:
        df           
    except NameError:
        a_ = boo.read_dataframe(2017)
        df = boo.large_companies(a_)
    cols = ['sales', 'ta', 'of', 'profit_before_tax', 'title']     

      
    print(sort(automotive(df), 'sales')[cols].head(10))
    for f in tires_prod, tires_dist, tires_trade:
        print(f(df)[cols])