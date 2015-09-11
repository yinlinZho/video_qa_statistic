import numpy
import pylab
import csv
import collections
import os
def draw_diivine_brisque(csvfile,plotfile):
    print csvfile
    with open(csvfile,'rb') as file:
        reader = csv.reader(file)
        file.seek(0)
        y = [float(row[len(row)-1]) for row in reader]
        file.seek(0)
        x = [int(row[0]) for row in reader]
        point = dict(zip(x,y))
        point_set = collections.OrderedDict(sorted(point.items()))
        pylab.rcParams['figure.figsize']
        pylab.rcParams['savefig.dpi']
        pylab.plot(point_set.keys(),point_set.values())
        pylab.grid(True)
        pylab.savefig(plotfile, dpi=200)
        pylab.clf()

if __name__ == '__main__':
    csv_path = r'E:\quality\9_9\brisque'
    plot_path = r'E:\quality\9_9\brisque\brisqueplot'
    csv_list = os.listdir(csv_path)
    for _ in csv_list:
        if 'csv' in _:
            csvfile = os.path.join(csv_path,_)
            plotfile = os.path.join(plot_path,_.split('.')[0]+'.png')
            draw_diivine_brisque(csvfile,plotfile)