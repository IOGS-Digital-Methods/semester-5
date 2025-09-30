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
   int a=2;
   int b=5;
   double x;
   x=-b/a;
   printf("a = %d \t b = %d \n",a,b);
   printf("la solution de a*x + b= 0 est : %lf\n",x);
   return 0;
}