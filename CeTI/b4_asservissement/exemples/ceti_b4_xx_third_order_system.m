w = logspace(1, 5, 101);
H0 = 1;
w0 = 1e3;


num_h = [H0];
den_h = [(1/w0)^3 6/w0^2 6/w0 H0+1];

h = tf(num_h, den_h)

h_loop = feedback(h, [1])

step(h_loop)