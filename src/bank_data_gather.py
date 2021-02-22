import pandas as pd
import numpy as np
import matplotlib as plt
import scipy.stats as stats
import matplotlib.pyplot as plt
def convert_bank_data_to_float(data_lst):
    
    lst = []
    for i in data_lst:
        i = float(i[2])
        lst.append(i)
    return lst

def autolabel(rects):
   
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
    #sept2020 TCBI data
    assets_total_sept2020 = tcbi.iloc[3] 
    net_income_sept2020 = tcbi.iloc[1116]
    netloan_losses_per_average_loans_sept2020 =tcbi.iloc[567]
     #dec2019 TCBI data
    assets_total_dec2019 = tcbi.iloc[414]
    net_income_dec2019 = tcbi.iloc[1118]
    netloan_losses_per_average_loans_dec2019 =tcbi.iloc[569]

    #sept2019 TCBI data
    assets_total_sept2019 = tcbi.iloc[413]
    net_income_sept2019 = tcbi.iloc[1117]
    netloan_losses_per_average_loans_sept2019 =tcbi.iloc[568]
    
    #dec 2018 TCBI data
    assets_total_dec2018 = tcbi.iloc[415]
    net_income_dec2018 = tcbi.iloc[1119]
    netloan_losses_per_average_loans_dec2018 =tcbi.iloc[570]

    #dec 2017 TCBI data 
    assets_total_dec2017 = tcbi.iloc[416]
    net_income_dec2017 = tcbi.iloc[1120]
    netloan_losses_per_average_loans_dec2017 =tcbi.iloc[571]


    
    
#graph total assets
    bank_dates = ['dec 2017', 'dec 2018', 'sept 2019','dec 2019', 'sept 2020' ]
    # bank_dates = ['sept 2020', 'dec 2019', 'sept 2019', 'dec 2018', 'dec 2017']

    assets_total_lst = [assets_total_dec2017,assets_total_dec2018,assets_total_sept2019,assets_total_dec2019,assets_total_sept2020]
    converted_assets_total_lst = (convert_bank_data_to_float(assets_total_lst))
    fig, ax= plt.subplots(1, figsize=(8,5), dpi = 200)
    ax.bar(bank_dates, converted_assets_total_lst)
    ax.set_title ('Total Assets')
  
    ax.ticklabel_format(axis = 'y', style = 'plain')
    fig.tight_layout()


    plt.show()
    print(converted_assets_total_lst)




