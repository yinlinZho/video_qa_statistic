
import os
import csv
import numpy
#sharpness = 'CQ'
def first2(csv_rootpath):
    outpath =csv_rootpath
    alg = os.path.basename(outpath)
    csvlist = os.listdir(csv_rootpath)
    for _ in csvlist:
        if 'csv' in _:
            videoname = _.split('.')
            #if sharpness in videoname[0]:
            niqe_score = []
            sseq_score = []
            with open(os.path.join(csv_rootpath,_),'rb') as csvfile:
                    reader = csv.reader(csvfile)
                    #csvfile.next()
                    for row in reader:
                        try:
                            niqe_qa = float(row[len(row)-2])
                            #print row
                            niqe_score.append(niqe_qa)

                        except:
                            print 'float() error'
                    csvfile.seek(0)
                    for row in reader:
                        try:
                            sseq_qa = float(row[len(row)-1])
                            sseq_score.append(sseq_qa)
                        except:
                            print 'float error'
                    mean_niqe = round(numpy.mean(niqe_score),3)
                    mean_sseq = round(numpy.mean(sseq_score),3)
                    var_niqe = round(numpy.var(niqe_score),3)
                    var_sseq = round(numpy.var(sseq_score),3)
                    with open(os.path.join(outpath,alg+'.csv'),'ab') as outfile:
                        writer = csv.writer(outfile)
                        #writer.writerow([videoname[0],mean_niqe,mean_sseq])
                        writer.writerow([videoname[0],mean_niqe,mean_sseq,var_niqe,var_sseq])
def mean_each(csv_rootpath):
    outpath =csv_rootpath
    alg = os.path.basename(outpath)
    csvlist = os.listdir(csv_rootpath)
    for _ in csvlist:
        if 'csv' in _:
            videoname = _.split('.')
            #if sharpness in videoname[0]:
            with open(os.path.join(csv_rootpath,_),'rb') as csvfile:
                    reader = csv.reader(csvfile)

                    score = []
                    for row in reader:
                        try:
                            qa = float(row[len(row)-1])
                            score.append(qa)
                        except:
                            print 'float() error'
                    mean = round(numpy.mean(score),3)
                    var_score = round(numpy.var(score),3)
                    with open(os.path.join(outpath,alg+'.csv'),'ab') as outfile:
                        writer = csv.writer(outfile)
                        #writer.writerow([videoname[0],mean])
                        writer.writerow([videoname[0],mean,var_score])

if __name__ == '__main__':
    csv_rootpath = r'E:\quality\9_9\first2'
    first2(csv_rootpath)