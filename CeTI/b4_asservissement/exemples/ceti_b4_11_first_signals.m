%
% Module Conception Electronique / Semestre 5 / Institut d'Optique
% 
% Découverte de Matlab / Signaux et Traitements
%
% Created on 09/Jul/2023
%
% author: Julien Villemejane / LEnsE / IOGS
%

%% Variables
a = 2;
b = 5;
c = a + b

%% Vecteurs
vt = linspace(0, 0.1, 128);
A = 20;
f0 = 100;
vs = A * sin(2*pi*f0*vt);

%% Affichage
figure()
plot(vt, vs)
str = sprintf('Sine Wave - at f0 = %.2f / A = %.2f', f0, A);
title(str);

%% Transformée de Fourier
fft_vs = fft(vs);
fft_vs_shift = fftshift(fft_vs);
vt_size = length(vt);
n_padding = 8;
fft_vs_padding = fft(vs, n_padding*vt_size);
fft_vs_padding_shift = fftshift(fft_vs_padding);

% Axe des fréquences
Fe = 1 / (vt(2)-vt(1));
freq_fft = linspace(0, Fe-Fe/vt_size, vt_size);
freq_fft_shift = fftshift(freq_fft);
freq_fft_padding = linspace(0, Fe-Fe/(n_padding*vt_size), n_padding*vt_size);
freq_fft_padding_shift = fftshift(freq_fft_padding);

% Figure
figure()
plot(freq_fft_shift, abs(fft_vs_shift), 'b')
hold on
plot(freq_fft_padding_shift, abs(fft_vs_padding_shift), 'r')
title('FFT of sine wave')
legend('FFT','FFT with zero-padding')