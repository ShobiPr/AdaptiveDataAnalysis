%% Load data
T = readtable('Data_S01_Sess01.csv', 'HeaderLines',1);
data = T(:,56);
signal = table2array(data);

%% Plot signal 
signal = signal';
plot(signal)
title('Raw EEG data')

%% Short Time Fourier
N = size(signal);
n = 0:N-1;
window = 512;
noverlap = 450;

spectrogram(signal, window, noverlap, 'yaxis');
hold on 
ylim([0 1])


all_instances = [3937 5431 6924 8421 9917 12324 13818 15311 16804 18298 21264 23318 25375 27428 29481 32475 34938 36998 39055 41108 44105 46162 48255 50309 52362 54792 56285 57782 59279 60772 63766 65826 67879 69936 71989 74422 75916 77409 78906 80399 82833 84329 85823 87316 88810 91236 92733 94226 95723 97216 100210 102270 104740 106793 108850 111810 113864 115920 117977 120030];
for j=1:length(all_instances) 
    
    value = all_instances(j);
    plot([value value],[0 1], 'r')
    hold on 
end
hold off

%% Fourier Transofrm 

fs = 1/200;              
y = fft(signal);    
f = (0:length(y)-1)*200/length(y);
plot(f,abs(y))
ylim([0 250000])
xlim([0 120])
title('Magnitude')

%%
figure()
x = linspace(0,6,100);
y = exp(x);
plot(x,y)
hold on 
plot([5 5], [0 50], '-')

