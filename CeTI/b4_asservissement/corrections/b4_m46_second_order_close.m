%% CeTI / Bloc 4 / Systèmes et asservissements
% Mission 4.6 - Système 2nd ordre + rebouclage

% Définition constante
w0 = 800;
m = 0.3;

% Définition système

H_num = [1];
H_den = [(1/w0)^2 2*m/w0 1];

H_sys = tf(H_num, H_den)

K = 1/20;
H_total = feedback(H_sys, K);

%% Réponse à un échelon
t = linspace(0, 0.1, 1001);
[IND_H, Time_H] = step(H_sys, t);
[IND_total, Time_total] = step(H_total, t);
figure(1)
plot(Time_H, IND_H, 'b', 'DisplayName', 'open loop');
hold on;
plot(Time_total, IND_total, 'r', 'DisplayName', 'closed loop');
grid on;
legend;

%% Réponse en fréquence
w = logspace(0, 5, 101);
[mag_H, phase_H, w_H] = bode(H_sys, w);
[mag_t, phase_t, w_t] = bode(H_total, w);
mag_H = squeeze(mag_H);
phase_H = squeeze(phase_H);
w_H = squeeze(w_H);
mag_t = squeeze(mag_t);
phase_t = squeeze(phase_t);
w_t = squeeze(w_t);
figure(2)
subplot(2,1,1)
semilogx(w_H, 20*log(abs(mag_H)), 'b', 'DisplayName', 'open loop');
hold on;
semilogx(w_t, 20*log(abs(mag_t)), 'r', 'DisplayName', 'closed loop');
grid on;
legend;
subplot(2,1,2)
semilogx(w_H, phase_H, 'b');
hold on;
semilogx(w_t, phase_t, 'r');
grid on;
