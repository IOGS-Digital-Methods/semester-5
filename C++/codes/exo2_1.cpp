/*
 * TD Langage C++ - Institut d'Optique - 1A / S5
 * 	TD2 - Exercice 1 - Tableaux 1D
 * 	Auteur : Julien VILLEMEJANE / 2018
 *  	Modifié : Julien VILLEMEJANE / 2024
 */


#include <iostream>
#include <cmath>
#include <cstdio>
#include "tab1D.h"

using namespace std;

/* FONCTION PRINCIPALE */
int main()
{
	double valeurs[10] = {1.5, 4.8, 17.2, 9.3, 5.2, 16.4, 9.1, 5.9, 13.5, 16.2};
	int notes[5] = {5, 16, 12, 9, 15};
    double k;

    afficheTabDbl(valeurs, 10);
    k = sommeTabDbl(valeurs, 10);
    printf("Somme valeurs : %.2lf \n", k);
    
    afficheTabInt(notes, 5);
    k = moyenneTabInt(notes, 5);
    printf("Moyenne notes : %.2lf \n", k);

	return 0;
}
