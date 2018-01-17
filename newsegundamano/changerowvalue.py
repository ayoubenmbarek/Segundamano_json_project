import csv

with open('/home/databiz41/newsegundamano/newsegundamano/segundamano_new_16.csv', "rb") as infile, open('/home/databiz41/newsegundamano/newsegundamano/segundamano_new_16_sorted.csv', "wb") as outfile:
    r = csv.DictReader(infile,delimiter=',')
    w = csv.DictWriter(outfile, r.fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
    w.writeheader()
    for row in r:
    #]
            #if row['ADRESSE']:
             #      row['ADRESSE'] = row['ADRESSE'].replace(',',' ')

            
            if row['ANNONCE_TEXT']:
                row['ANNONCE_TEXT'] = row['ANNONCE_TEXT'].split('  ')#replace(',',' ') 
               # del row['ANNONCE_TEXT']
            if row['FROM_SITE']:
                row['FROM_SITE'] = 'segundamano'

            if row['M2_TOTALE']:
                row['M2_TOTALE'] = float(row['PAYS_AD'])

            if row['PAYS_AD']:
                del row['PAYS_AD']
            ##prends en charge tous les mois si besoin en avenir    
            if row['ANNONCE_DATE']:
                if 'enero' in row['ANNONCE_DATE']:
                    cc = row['ANNONCE_DATE'].split(' ')
                    row['ANNONCE_DATE'] = '2018-01-'+cc[0]+' '+cc[-1]+':00'
                elif 'dic' in row['ANNONCE_DATE']:
                    cc = row['ANNONCE_DATE'].split(' ')                                                                                                               
                    row['ANNONCE_DATE'] = '2017-12-'+cc[0]+' '+cc[-1]+':00'
                elif 'oct' in row['ANNONCE_DATE']:
                    cc = row['ANNONCE_DATE'].split(' ')
                    row['ANNONCE_DATE'] = '2017-10-'+cc[0]+' '+cc[-1]+':00'
                elif 'nov' in row['ANNONCE_DATE']:
                    cc = row['ANNONCE_DATE'].split(' ')
                    row['ANNONCE_DATE'] = '2017-11-'+cc[0]+' '+cc[-1]+':00'
	    w.writerow(row)
