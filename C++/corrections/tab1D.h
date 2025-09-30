/*
 * TD Langage C++ - Institut d'Optique - 1A / S5
 * 	TD2 - Exercice 1 - Tableaux 1D
 * 	Auteur : Julien VILLEMEJANE / 2018
 *  	Modifié : Julien VILLEMEJANE / 2024
 */

/* FICHIER CONTENANT LES DECLARATIONS DES FONCTIONS ASSOCIEES AUX TABLEAUX 1D */
#ifndef TAB1D_H_INCLUDED
#define TAB1D_H_INCLUDED

#include <stdio.h>
#include <stdlib.h>

/*
 * afficheTabInt : Affiche dans la console un tableau d'entiers
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type entier)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Affichage sur la console
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
void afficheTabInt(int t[], int dim);

/*
 * sommeTabDbl : Calcule la somme des éléments d'un tableau d'entiers
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type entier)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Somme des éléments (entier)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
int sommeTabInt(int t[], int dim);

/*
 * moyenneTabDbl : Calcule la moyenne des éléments d'un tableau d'entiers
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type entier)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Moyenne des éléments (double)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
double moyenneTabInt(int t[], int dim);

/*
 * afficheTabDbl : Affiche dans la console un tableau de double
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Affichage sur la console
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
void afficheTabDbl(double t[], int dim);

/*
 * sommeTabDbl : Calcule la somme des éléments d'un tableau de double
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Somme des éléments (double)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
double sommeTabDbl(double t[], int dim);

/*
 * moyenneTabDbl : Calcule la moyenne des éléments d'un tableau de double
 * 	ENTREES :
 *		t[] : adresse du tableau à afficher (type double)
 *      dim : dimension du tableau à afficher (entier)
 * 	SORTIE :
 * 		Moyenne des éléments (double)
 * 	Auteur : Julien Villemejane – Création : 05/07/2018
 */
double sommeTabDbl(double t[], int dim);

#endif // TAB1D_H_INCLUDED
