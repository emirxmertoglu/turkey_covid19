# COVID-19 Turkey Data Repository

Üzerinde çalıştığım projedeki amacım [Covid-19 veri setini](https://github.com/CSSEGISandData/COVID-19) web üzerinde [Kaggle.com](https://www.kaggle.com/)&#39;dan yararlanarak [Python](https://www.python.org/) ve Python&#39;un kütüphaneleri olan; [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/) ve [Altair](https://altair-viz.github.io/)&#39;i kullanarak veri setindeki verileri analiz ederek anlamlı hale getirip görselleştirmek.

NumPy (Numerical Python) bilimsel hesaplamaları hızlı bir şekilde yapmamızı sağlayan bir matematik kütüphanesidir.

Pandasda, kullanımı kolay veri yapıları sunan ve veri üzerinde analiz yapmayı sağlayan açık kaynak kodlu Python kütüphanelerinden birisidir. Sahip olduğu birçok özellik sebebiyle veri okuma ve önişleme aşamalarında makine öğrenmesi alanlarında çalışanlara büyük kolaylıklar sağlamaktadır.

Altair, Python için bildirim temelli bir istatistiksel görselleştirme kütüphanesidir.

Yazılımımın kısaca çalışma yapısını açıklamam gerekirse;

- Johns Hopkins Üniversitesi Sistem Bilimi ve Mühendisliği Merkezi&#39;nin (CSSE) sağladığı günlük olarak güncellenen Covid-19 verilerini [Github](https://github.com/)&#39;dan [CSV](https://www.sonsuzteknoloji.com/csv-dosyasi-nedir-ve-ne-ise-yarar/#:~:text=Comma%20Separated%20Values%20(CSV)%20%E2%80%93,uygulamalar%20aras%C4%B1nda%20veri%20al%C4%B1%C5%9Fveri%C5%9Finde%20kullan%C4%B1l%C4%B1r.&amp;text=Bu%20dosyalar%20bazen%20Karakter%20Ayr%C4%B1lm%C4%B1%C5%9F%20De%C4%9Ferler%20veya%20Virg%C3%BClle%20Ayr%C4%B1lm%C4%B1%C5%9F%20dosyalar%20olarak%20adland%C4%B1r%C4%B1labilir.) formatında çekiyor,
- Çektiği verileri tek bir matriste birleştiriyor,
- Tarih formatlarını anlamlı hale getiriyor,
- NaN değere sahip verileri düzeltiyor,
- Verileri ülke-bölge ve tarihe göre grupluyor,
- Günlük güncellenen verilere göre, yeni oluşan vaka sayılarını, ölümleri ve iyileşmeleri farklı bir kolonda gösteriyor,
- En son da global olarak bütün ülkeleri-bölgeleri içerecek şekilde tekrardan CSV formatında kaydediyor.

Daha fazla bilgi için; projenin ilk kısmının linki: [https://www.kaggle.com/emirmertoglu/emir-mertoglu-covid-19-calisma-ortami](https://www.kaggle.com/emirmertoglu/emir-mertoglu-covid-19-calisma-ortami)

Yazılımımın ikinci ayağında ise;

- Oluşturduğum veri setinden sadece Türkiye&#39;yi içeren verileri alıp yeni bir matrise atıyor,
- Bu matristen yararlanarak iki farklı grafik oluşturuyor; ilki toplam vaka sayılarını ve toplam ölümleri gösteriyor tarihe göre, ikincisi günlük değerleri analiz edip yeni vaka sayılarını, yeni ölümleri ve yeni iyileşme sayılarını grafikte gösteriyor.

Daha fazla bilgi için; projenin ikinci kısmının linki: [https://www.kaggle.com/emirmertoglu/emir-mertoglu-covid-19-turkiye-grafigi](https://www.kaggle.com/emirmertoglu/emir-mertoglu-covid-19-turkiye-grafigi)