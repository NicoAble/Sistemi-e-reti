import matplotlib.pyplot as plt
import csv

def main():
    anni = []
    tmp = []
    
    data_file = open("./Temperature_Anomaly.csv")
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader)
    
    for row in data_reader:
        anni.append(int(row[0]))
        tmp.append(float(row[1]))
    
    fig, (ax1) = plt.subplots(1, 1)
    fig.suptitle('temperature medie della superficie terrestre ed oceanica')

    ax1.plot(anni, tmp, 'o-r')
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('Temperatura')
    plt.show()
       

if __name__ == "__main__":
    main()
    