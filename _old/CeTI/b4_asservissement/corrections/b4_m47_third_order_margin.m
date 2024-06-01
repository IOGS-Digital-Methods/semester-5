%% CeTI / Bloc 4 / Systèmes et asservissements
% Mission 4.7 - Système 3e ordre + marge

% Définition constante
w0 = 1000;
H0 = 5;

% Définition système
% (a+b)3 = a3 + 3a2b + 3ab3 + b3

H_num = [H0];
H_den = [1/w0^3 3/w0^2 3/w0 1+H0];

H_sys = tf(H_num, H_den)
figure(1);
bode(H_sys)

%% Réponse en fréquence
w = logspace(0, 5, 101);
[mag_H, phase_H, w_H] = bode(H_sys, w);
mag_H = squeeze(mag_H);
phase_H = squeeze(phase_H);
w_H = squeeze(w_H);
figure(2)
subplot(2,1,1)
semilogx(w_H, 20*log(abs(mag_H)), 'b');
grid on;
subplot(2,1,2)
semilogx(w_H, phase_H, 'b');
grid on;

%% Détermination des marges
[Gm,Pm] = margin(H_sys)