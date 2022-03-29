import math
import matplotlib.pyplot as plt

ITERATIONS = 100
tm = 30  # Time constant
Vreset = -65  # Reset voltage after spike generation
EL = -65
Vthreshold = -50  # Threshold of membrane for spike generation
Rm = 90  # Resistance of membrane
T_REFRACT = 2  # Refractory period of the membrane after a spike

def integrateAndFire():

    num_of_spikes = 0
    Ie = 1
    Ie_isi = 0.5
    time = 0
    V0 = -67
    voltage = 0
    r_isi = 0

    print("======================INTEGRATE AND FIRE==========================")
    i = 0
    while(i<ITERATIONS):
        voltage= EL+(Rm*Ie)+((V0-EL-(Rm*Ie))*(math.exp(-time/tm)))
        print("------------------------------------",i,"s-----------------------------------------")
        print("Voltage:", voltage)
        if (voltage > Vthreshold):
            num_of_spikes+=1
            V0=Vreset #reset membrane potential after spike generation
            print("At ", i, "ms","Voltage ", voltage, "time:", time)
            print("Number", num_of_spikes, " spike was at ", i, "ms")
            i=i+T_REFRACT #Refactory period where the neuron cannot produce spike
            time=0
        else:
            #print("At "+ str(i) +" ms "+"Voltage " + str(voltage) +" time: " + str(time))
            i+=1
            time +=1

    print("\nTotal Number of Spikes:",num_of_spikes)

    print("\n############### Inter Spike Interval - Risi #################\n")

    for j in range(0, 4):
        r_isi = (1 / (T_REFRACT + (tm * math.log(((Rm * Ie_isi) + (EL - Vreset)) / ((Rm * Ie_isi) + (EL - Vthreshold))))))
        print("For ", Ie_isi, " nA ", "Risi= ", r_isi)
        Ie_isi += 0.5



# Defining main function
def main():
    integrateAndFire()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()



