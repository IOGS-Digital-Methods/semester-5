/* 
 * TD Langage C++ - Institut d'Optique - 1A / S5
 *         TD1 - Exercice 5
 *         Auteur : Julien VILLEMEJANE / 2024
 */

#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

/* Prototype de la fonction somme */
int somme(int a, int b);

/* Fonction principale */
int main()
{
   int n1=2;
   int n2=5;
   int res = somme(n1, n2);
   
   cout << "Somme de " << n1 << "+" << n2 << " = " << res << endl;
   
   return 0;
}


/* Définition de la fonction somme */
int somme(int a, int b){
	int s = a + b;
	return s;
}