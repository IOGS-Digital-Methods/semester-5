/* 
 * TD Langage C++ - Institut d'Optique - 1A / S5
 *         TD1 - Exercice 5
 *         Auteur : Julien VILLEMEJANE / 2024
 */

#include <iostream>
#include <cmath>

using namespace std;

/* Prototype de la fonction somme */
int somme(int a, int b);
/* Prototype de la fonction serie */
int serie(int u0, int n);


/* Fonction principale */
int main()
{
   int n1=2;
   int n2=5;
   int res = somme(n1, n2);
   
   cout << "Somme de " << n1 << "+" << n2 << " = " << res << endl;
   
   int n = 2;
   res = serie(3, n);
   
   cout << "Série pour n = " << n << " = " << res << endl;
   
   return 0;
}


/* Définition de la fonction somme */
int somme(int a, int b){
	int s = a + b;
	return s;
}

/* Prototype de la fonction serie */
int serie(int u0, int n){
	int uk = u0;
	for(int k = 0; k < n; k++){
		uk = 3*uk + 4;
	}
	return uk;
}