from brian2 import *

N=1
tau_m= 30 * ms # membrane time constant
v_r= -65 * mV # reset potential
v_th= -50 * mV # threshold potential
I_c= 20 * mV # constant input current
Ie= 1 * namp # Values: 0.5,1.0,1.5,2.0
El= -65 * mV
Rm= 90 * Mohm
V0= -67 * mV

eqs=''' 
dv/dt=(El-v+(Rm*I))/tau_m:volt (unless refractory)
I : amp
'''

def IAF_Brian():

    #Neuron Build
    lif = NeuronGroup(N, model=eqs, threshold='v>v_th', reset='v=v_r', refractory=2 * ms)
    lif.v = V0
    lif.I = Ie
    spikes = SpikeMonitor(lif)
    v_trace = StateMonitor(lif, 'v', record=True)

    #Run experiment
    run(100 * ms)
    #run(0.1 * second)

    #Plot Vol-Time
    plot(v_trace.t/ms, v_trace[0].v/mV)
    xlabel("Time(ms)", fontsize=24)
    ylabel("v(mV)", fontsize=24)
    show()

    #Spikes
    print("Spike times: %s" % spikes.t[:])
    #print("Spike times: %s", spikes.t[:]*ms)
    print(("Total number of spikes:",len(spikes.t)))

    #Spike Frequency
    print("Rate:",spikes.count/(1000 * ms))


    # Plot Input Current & Firing Rate
    Iinp = [0.5, 1, 1.5, 2]  #For each case we change Ie value
    FRate = [70, 135, 182, 217]  # Rates for 1000 ms

    plot(Iinp, FRate)
    xlabel('I (nA)', fontsize=15)
    ylabel('Firing Rate (spikes/s)',fontsize=15)
    show()




# Defining main function
def main():
    IAF_Brian()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()