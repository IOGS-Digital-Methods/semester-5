% """
% Module Outils Numériques / Semestre 5 / Institut d'Optique
% 
% System approach - RC filter - Matlab Script
% 
% Created on 20/Apr/2023
% 
% @author: LEnsE / IOGS / Palaiseau
% @author: Julien Villemejane
% """

R = 1e3;
C = 1e-6;

num = [1];
den = [(R*C) 1];
tf_sys = tf(num, den)

bode(tf_sys)
step(tf_sys)