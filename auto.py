import boo
from boo.dataframe.util import industry


# some companies, _underscore for companies for erroneous report
class COMPANY:
    _neftekom = 7801464198
    ferronordic = 5001048893
    e4 = 7720554943
    nami = 7711000924

UNREAL = [COMPANY._neftekom]
    
# groups of companies not in their     
class ALLOC:
    tires=[7816162305,
           7704787370,
           5073007462,
           2457061775,
           1651024807,
           7706560230,
           7703247653,
           7707296796,
           7725693620,
           7703204071]
    metal=[7449006184]
    auto_specmach=[7710761161]
    auto_component=[5001048893]
    vagon=[1901004997]
    other=[1435196431,
           3711018160,
           7717591053,
           5024097520]
    construction=[7719272800,
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
                  7729564128]    

def as_str(xs):
    return [str(x) for x in xs]

    
def combine(*args, base=UNREAL):    
    return as_str(base) + as_str(args)

# Автомобильная промышленность

# производители
# импортеры
# дилеры
# шины
# компоненты
# спецтезхника

# https://www.vedomosti.ru/economics/articles/2018/04/23/767509-krupneishie-avtodileri-natorgovali-na-18-trln-rublei

              
def automotive(df, sort='of'):
    exclude = combine(COMPANY.e4,
                      *ALLOC.construction,
                      *ALLOC.tires,
                      *ALLOC.auto_specmach,
                      *ALLOC.vagon,
                      *ALLOC.metal,
                      *ALLOC.other)
    return industry(df, 29) \
           .append(industry(df, 45)) \
           .sort_values(sort, ascending=False) \
           .drop(exclude)

if __name__ == "__main__":
    try:
        df           
    except NameError:
        a_ = boo.read_dataframe(2017)
        df = boo.large_companies(a_)
        print("Imported full dataframe")
    cols = ['sales', 'ta', 'of', 'title']     

    # list a a table + save to csv         
    print(automotive(df,'sales')[cols].head(10))
    
    import pandas as pd    
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)    
    
    af = automotive(df,'sales').set_index("title")
    
    # plotting    
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    
    on_axis = ["of", "sales"]
    af[0:10].plot.scatter(*on_axis, ax=ax)
    for k, v in af[on_axis].iterrows():
        ax.annotate(k, v)
        
    fig, ax = plt.subplots()        
    af2 = af.head(15)
    (af2.sales/af2.of).sort_values(ascending=True).head(12).plot.barh()
    (af2.sales/af2.of).sort_values(ascending=True).tail(3).plot.barh()
    
