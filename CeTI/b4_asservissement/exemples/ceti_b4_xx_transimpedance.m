Rt = 1e5;
C = 5e-11;
A0 = 1e6;
GBP = 3e6;
w0 = 2*pi*GBP/A0;

w = logspace(0, 7, 101);

num_A = [A0];
den_A = [1/w0 1];
tf_A = tf(num_A, den_A)
[mag_A,phase_A,wout_A] = bode(tf_A, w);

num_B = [1];
den_B = [Rt*C 1];
tf_B = tf(num_B, den_B)
[mag_B,phase_B,wout_B] = bode(tf_B, w);

num_BB = [Rt];
den_BB = [Rt*C 1];
tf_BB = tf(num_BB, den_BB);

tf_G = series(tf_BB, feedback(tf_A, tf_B))
[mag_G,phase_G,wout_G] = bode(tf_G, w);


figure()
semilogx(w, 20*log10(squeeze(mag_A)), 'DisplayName','AOP')
hold on;
semilogx(w, 20*log10(squeeze(mag_B)), 'DisplayName','RC')
semilogx(w, 20*log10(squeeze(mag_G)), 'DisplayName','Loop')
legend()
