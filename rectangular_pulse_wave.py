# plotting rectangular pulse waves for PWM visualization
#
import numpy as np
import matplotlib.pyplot as plt

# plotting routine
fig,ax = plt.subplots(figsize=(16,10))
ax.grid(True,color='#FCFCFC',linewidth=1.5)
ax.set_facecolor('#e6e6e6')
ax.set_ylim([-0.8,5.99])
ax.set_xlabel('Time [s]',fontsize=26,labelpad=15)
ax.set_ylabel('Amplitude [V]',fontsize=26,labelpad=15)
ax.tick_params('both',labelsize=16)

D = 0.5 # duty cycle [%]
T = 0.02 # period in seconds
tau = D*T # pulse duration
n_size = 10000 # size of the Fourier sum
n = np.linspace(1.0,n_size,n_size) # vector for Fourier sum

periods_to_plot = 3 # how many periods to plot in figure
t = np.linspace(0.0,T*periods_to_plot,1000) # time vector
t_shift = t - (tau/2.0) # shift about zero point to capture full first cycle

f_t = [] # rectangular pulse variable
for t_i in t_shift:
    f_t.append(5.0*((tau/T) + np.sum((2.0/(n*np.pi))*(np.sin((np.pi*n*tau)/(T)))*(np.cos((2.0*np.pi*n*t_i)/(T))))))

# annotations to show duty cycle, period, off band
annot1 = ax.annotate("", xy=(T, 5.25), xytext=(T+tau, 5.25),
             arrowprops=dict(arrowstyle="|-|",facecolor='k',
                             linewidth=3))
txt1 = ax.text(T+(tau/2.0),5.6,'{0:2.0f}% Duty Cycle ({1:2.0f}ms)'.format(D*100.0,tau*1000.0),
        {'color': 'black', 'fontsize': 12, 'ha': 'center', 'va': 'center',
         'bbox': dict(boxstyle="round", fc="#FCFCFC", ec="#FCFCFC", pad=0.6)})
annot2 = ax.annotate("", xy=(T, -0.25), xytext=(2.0*T, -0.25),
             arrowprops=dict(arrowstyle="|-|",facecolor='k',
                             linewidth=3))
txt2 = ax.text(T+(T/2.0),-0.5,'{0:2.0f}ms Period ({1:2.0f}Hz)'.format(T*1000.0,1.0/T),
        {'color': 'black', 'fontsize': 12, 'ha': 'center', 'va': 'center',
         'bbox': dict(boxstyle="round", fc="#FCFCFC", ec="#FCFCFC", pad=0.6)})
ax.plot(t,f_t,linewidth=4,color=plt.cm.Set1(1))
plt.show()
