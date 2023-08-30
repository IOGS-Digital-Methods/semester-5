%% CeTI / Bloc 4 / Systèmes et asservissements
% Mission 4.5 - Système 2nd ordre

% Définition constante
w0 = 800;
m = 0.3;

% Définition système

H_num = [1];
H_den = [(1/w0)^2 2*m/w0 1];

H_sys = tf(H_num, H_den)

%% Réponse à un échelon
t = linspace(0, 0.1, 1001);
[IND_H, Time_H] = step(H_sys, t);
figure(1)
plot(Time_H, IND_H);
grid on;

%% Réponse en fréquence
w = logspace(0, 5, 101);
[mag_H, phase_H, w_H] = bode(H_sys, w);
mag_H = squeeze(mag_H);
phase_H = squeeze(phase_H);
w_H = squeeze(w_H);
figure(2)
subplot(2,1,1)
semilogx(w_H, 20*log(abs(mag_H)));
grid on;
subplot(2,1,2)
semilogx(w_H, phase_H);
grid on;

%% Pour des m differents
m1 = 0.3;
m2 = 0.707;
m3 = 1.2;

H_num = [1];
H_den1 = [(1/w0)^2 2*m1/w0 1];
H_sys1 = tf(H_num, H_den1);
H_den2 = [(1/w0)^2 2*m2/w0 1];
H_sys2 = tf(H_num, H_den2);
H_den3 = [(1/w0)^2 2*m3/w0 1];
H_sys3 = tf(H_num, H_den3);

[imp_1, t_1] = impulse(H_sys1, t)
[imp_2, t_2] = impulse(H_sys2, t)
[imp_3, t_3] = impulse(H_sys3, t)

figure(3)
plot(t_1, imp_1, 'b', 'DisplayName', 'm = 0.3')
hold on;
plot(t_2, imp_2, 'g', 'DisplayName', 'm = 0.707')
plot(t_3, imp_3, 'r', 'DisplayName', 'm = 1.2')
grid on;
legend;
