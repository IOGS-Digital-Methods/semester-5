/*
 * TD Langage C++ - Institut d'Optique - 1A / S5
 * 	TD2 - Exercice 1 - Tableaux 1D
 * 	Auteur : Julien VILLEMEJANE / 2018
 *  	Modifié : Julien VILLEMEJANE / 2024
 */

#include "tab1D.h"

/* FICHIER CONTENANT LES DEFINITIONS DES FONCTIONS ASSOCIEES AUX TABLEAUX 1D */

/*
 * afficheTabInt : Affiche dans la console un tableau d'entiers
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type entier)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Affichage sur la console
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
void afficheTabInt(int t[], int dim){
    int i;
    for(i = 0; i < dim; i++)
        printf("%d ", t[i]);
    printf("\n");
}

/*
 * sommeTabInt : Calcule la somme des éléments d'un tableau d'entiers
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type entier)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Somme des éléments (entier)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
int sommeTabInt(int t[], int dim){
    int res;
    int i;
    res = 0;
    for(i = 0; i < dim; i++)
        res = res + t[i];
    return res;
}

/*
 * moyenneTabInt : Calcule la moyenne des éléments d'un tableau d'entiers
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Moyenne des éléments (double)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
double moyenneTabInt(int t[], int dim){
    double res;
    res = sommeTabInt(t, dim);
    return res/(double)dim;
}


/*
 * afficheTabDbl : Affiche dans la console un tableau de double
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Affichage sur la console
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
void afficheTabDbl(double t[], int dim){
    int i;
    for(i = 0; i < dim; i++)
        printf("%.2lf ", t[i]);
    printf("\n");
}

/*
 * sommeTabDbl : Calcule la somme des éléments d'un tableau de double
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Somme des éléments (double)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
double sommeTabDbl(double t[], int dim){
    double res;
    int i;
    res = 0;
    for(i = 0; i < dim; i++)
        res = res + t[i];
    return res;
}

/*
 * moyenneTabDbl : Calcule la moyenne des éléments d'un tableau de double
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Moyenne des éléments (double)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
double moyenneTabDbl(double t[], int dim){
    double res;
    res = sommeTabDbl(t, dim);
    return res/(double)dim;
}
