# dahil edilecek kutuphaneler
import numpy as np
import pandas as pd

# gunluk olarak guncellendigi icin kaggledaki bu datasetin github reposundan csv formatinda verileri cekiyorum
# https://github.com/CSSEGISandData/COVID-19

vakalar_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
#print(vakalar_df.columns)
olumler_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
#print(olumler_df.columns)
iyilesenler_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
#print(iyilesenler_df.head())

# burada verileri birlestirme islemi yapiyorum
# ilk 4 sutun butun verilerde ayni oldugundan dahil etmiyorum
tarihler = vakalar_df.columns[4:]
vakalar_df_long = vakalar_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=tarihler, 
    var_name='Tarih', 
    value_name='Vakalar'
)
olumler_df_long = olumler_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=tarihler, 
    var_name='Tarih', 
    value_name='Olumler'
)
iyilesenler_df_long = iyilesenler_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=tarihler, 
    var_name='Tarih', 
    value_name='Iyilesenler'
)

#print(iyilesenler_df_long.head())
#print(iyilesenler_df_long.tail())

# Kanadayı uyusmazlik sorunu yuzunden veri setinden cikarmamiz gerekiyor
iyilesenler_df_long = iyilesenler_df_long[iyilesenler_df_long['Country/Region']!='Canada']

# 3 veri setini birlestiriyoruz merge() fonksiyonu ile
tam_tablo = vakalar_df_long.merge(
  right=olumler_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Tarih', 'Lat', 'Long']
)

tam_tablo = tam_tablo.merge(
  right=iyilesenler_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Tarih', 'Lat', 'Long']
)

#print(tam_tablo)

# tarih formatini duzenliyorum
tam_tablo['Tarih'] = pd.to_datetime(tam_tablo['Tarih'])
#print(tam_tablo)

#tam_tablo.isna().sum() veri setindeki NaN verilerin sayisinin toplamini aldim
tam_tablo['Iyilesenler'] = tam_tablo['Iyilesenler'].fillna(0) #NaN degerleri duzeltiyorum

# bu veri setinde yolcu gemilerindeki vakalarada yer verilmis, yolcu gemilerinin verilerini veri setinden cikarmak gerek
gemi_satirlari = tam_tablo['Province/State'].str.contains('Grand Princess') | tam_tablo['Province/State'].str.contains('Diamond Princess') | tam_tablo['Country/Region'].str.contains('Diamond Princess') | tam_tablo['Country/Region'].str.contains('MS Zaandam')
gemi_verileri = tam_tablo[gemi_satirlari]
tam_tablo = tam_tablo[~(gemi_satirlari)]

# aktif vaka kolonu olusturalim
tam_tablo['Aktif'] = tam_tablo['Vakalar'] - tam_tablo['Olumler'] - tam_tablo['Iyilesenler']
#print(tam_tablo.columns)

# verileri ulke - bolge ve tarihe gore gruplayalim
tam_gruplanmis = tam_tablo.groupby(['Tarih', 'Country/Region'])['Vakalar', 'Olumler', 'Iyilesenler', 'Aktif'].sum().reset_index()
#print(tam_gruplanmis)

# yeni vakalar 
temp = tam_gruplanmis.groupby(['Country/Region', 'Tarih', ])['Vakalar', 'Olumler', 'Iyilesenler']
temp = temp.sum().diff().reset_index()
mask = temp['Country/Region'] != temp['Country/Region'].shift(1)
temp.loc[mask, 'Vakalar'] = np.nan
temp.loc[mask, 'Olumler'] = np.nan
temp.loc[mask, 'Iyilesenler'] = np.nan

# kolonlari duzenleyelim
temp.columns = ['Country/Region', 'Tarih', 'Yeni Vakalar', 'Yeni Olumler', 'Yeni Iyilesenler']

# yeni degerleri ekleyelim
tam_gruplanmis = pd.merge(tam_gruplanmis, temp, on=['Country/Region', 'Tarih'])

# NaN degerleri 0 ile dolduralim
tam_gruplanmis = tam_gruplanmis.fillna(0)

# veri tiplerini duzeltelim
cols = ['Yeni Vakalar', 'Yeni Olumler', 'Yeni Iyilesenler']
tam_gruplanmis[cols] = tam_gruplanmis[cols].astype('int')

# tarih ve bolgeye gore siralanmis vaka veri setinin son hali
tam_gruplanmis['Yeni Vakalar'] = tam_gruplanmis['Yeni Vakalar'].apply(lambda x: 0 if x<0 else x)
#print(tam_gruplanmis)

# olusturdugumuz bu yeni veri setini csv formatiyla localde saklayalim
tam_gruplanmis.to_csv('emir_mertoglu_covid19_calismasi.csv')
print('Guncellenmis veriler ile veri seti csv formatinda kaydedildi!')

