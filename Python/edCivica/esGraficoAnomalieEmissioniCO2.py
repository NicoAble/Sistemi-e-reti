import matplotlib.pyplot as plt
import csv

def main():
    Year = []
    Total = []
    GasFuel = []
    LiquidFuel = []
    SolidFuel = []
    Cement = []
    GasFlaring = []
    PerCapita = []
    
    data_file = open("./CO2_emissions.csv")
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader)
    
    for row in data_reader:
        Year.append(int(row[0]))
        Total.append(float(row[1]))
        GasFuel.append(int(row[2]))
        LiquidFuel.append(float(row[3]))
        SolidFuel.append(int(row[4]))
        Cement.append(float(row[5]))
        GasFlaring.append(int(row[6]))
        if(row[7] is ""): PerCapita.append(float(0))
        else: PerCapita.append(float(row[7]))
    
    data_file.close()
    
    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1)
    fig.suptitle('emissioni medie')

    ax1.plot(Year, Total, 'o-r')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total')

    ax2.plot(Year, GasFuel, 'o-b')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('GasFuel')

    ax3.plot(Year, LiquidFuel, 'o-b')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('LiquidFuel')

    ax4.plot(Year, SolidFuel, 'o-b')
    ax4.set_xlabel('Year')
    ax4.set_ylabel('SolidFuel')

    ax5.plot(Year, Cement, 'o-b')
    ax5.set_xlabel('Year')
    ax5.set_ylabel('Cement')

    ax6.plot(Year, GasFlaring, 'o-b')
    ax6.set_xlabel('Year')
    ax6.set_ylabel('GasFlaring')

    ax7.plot(Year, PerCapita, 'o-b')
    ax7.set_xlabel('Year')
    ax7.set_ylabel('PerCapita')
    plt.show()
       

if __name__ == "__main__":
    main()