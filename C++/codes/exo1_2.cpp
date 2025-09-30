/* 
 * TD Langage C++ - Institut d'Optique - 1A / S5
 *         TD1 - Exercice 5
 *         Auteur : Sylvie LEBRUN / 2020
 *			Modifié par Julien VILLEMEJANE / 2024
 */

#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;


int main()
{
    double capa=1e-6;
    double resistance=1e3;
    double w0=1/(resistance*capa);
    double module_filtre, gain_dB;
    double w;

	cout << "R = " << resistance;
	printf(" et C = %lf uF \n", capa*1e6);
	
	cout << "Et w0 = " << w0 << " rd/s" << endl;	
		
	printf("entrez la valeur de la pulsation : \n");
	cin >> w;
	
	module_filtre=1/sqrt(1+w*w/(w0*w0));
    gain_dB=20*log10(module_filtre);
    printf("Gain = %lf dB\n",gain_dB);
    return 0;
}