import os
import csv
import numpy
csv_rootpath = r'E:\quality\diivine\yy'
sharpness = 'CQ'
app = os.path.basename(csv_rootpath)
outpath = r'E:\quality\diivine'
csvlist = os.listdir(csv_rootpath)
for _ in csvlist:
    videoname = _.split('.')
    #if sharpness in videoname[0]:
    with open(os.path.join(csv_rootpath,_),'rb') as csvfile:
            reader = csv.reader(csvfile)
            csvfile.next()
            score = []
            for row in reader:
                try:
                    qa = float(row[len(row)-1])
                    score.append(qa)
                except:
                    print 'float() error'
            mean = round(numpy.mean(score),3)
            with open(os.path.join(outpath,app+'.csv'),'ab') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([videoname[0],mean])