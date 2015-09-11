import os
import csv
csv_rootpath = r'E:\algorithm\fr\qa'
csvlist = os.listdir(csv_rootpath)
sharpness = 'p7'
app = os.path.basename(csv_rootpath)

outpath = os.path.join(r'E:\algorithm\fr\qa','testcase'+'.csv')
print outpath
outfile = open(outpath,'wb')
writer = csv.writer(outfile)
for _ in csvlist:
    with open(os.path.join(csv_rootpath,_),'r+') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print row
                writer.writerow([_]+row)
outfile.close()

