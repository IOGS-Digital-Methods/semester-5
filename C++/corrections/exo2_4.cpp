/* 
 * TD Langage C++ - Institut d'Optique - 1A / S5
 *         TD2 - Exercice 4
 *         Auteur : Julien VILLEMEJANE / 2024
 */

#include <iostream>
#include <cmath>

using namespace std;


/* Fonction principale */
int main()
{
	char chaine[10] = "IOGS 2024";
	
	printf("chaine[2] = %c\n", chaine[2]);
	printf("chaine[2] = %d\n", chaine[2]);
	printf("chaine[2] = %x\n", chaine[2]);
	
	char c = chaine[3] - 'A' + 'a';
	
	printf("c = %c\n", c);
	
	char chaine2[20];
	sprintf(chaine2, "char c = %c\n", c);
	printf("%s", chaine2);
	
	return 0;
}
