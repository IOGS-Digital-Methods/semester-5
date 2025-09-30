/* 
 * TD Langage C++ - Institut d'Optique - 1A / S5
 *         TD2 - Exercice 3
 *         Auteur : Julien VILLEMEJANE / 2024
 */

#include <iostream>
#include <cmath>

using namespace std;


/* Fonction principale */
int main()
{
   int a = 478;
   
   int k = a << 3;
   
   printf("k = %d\n", k);
   
   k = a >> 2;
   
   printf("k = %d\n", k);
   
   k = a & 0b11111111;
   
   printf("k = %d\n", k);
   
   int k1, k2;
   
   k1 = (a >> 8) & 0b11111111;
   k2 = (a) & 0b11111111;
   
   k = (k1 << 8) + k2; 
   printf("k = %d\n", k);
   
   return 0;
}
