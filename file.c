#include <stdio.h>

int resultado = 0, a, b, c;

int suma();
int resta();
int multi();
int divi();
int selecciona;

	int
	main() {
	printf("\tCalculadora\n");
	printf("1:Suma\n2:Resta\n3:Multiplicacion\n4:Division\n\tSeleccione una opcion: ");
	scanf("%i", &selecciona);

	switch (selecciona) {
	case 1:
		printf("\nUsted ha seleccionado Suma");
		printf("\nIngrese el valor 1:");
		scanf("%i", &a);
		printf("Ingrese el valor 2:");
		scanf("%i", &b);

		resultado = suma(a, b);
		printf("\nLa suma es: %i", resultado);
		break;

	case 2:
		printf("\nUsted ha seleccionado Resta");
		printf("\nIngrese el valor 1:");
		scanf("%i", &a);
		printf("Ingrese el valor 2:");
		scanf("%i", &b);

		resultado = resta(a, b);
		printf("\nLa resta es: %i", resultado);
		break;

	case 3:
		printf("\nUsted ha seleccionado Multiplicacion");
		printf("\nIngrese el valor 1:");
		scanf("%i", &a);
		printf("Ingrese el valor 2:");
		scanf("%i", &b);

		resultado = multi(a, b);
		printf("\nLa Multiplicacion es: %i", resultado);
		break;

	case 4:
		printf("\nUsted ha seleccionado Division");
		printf("\nIngrese el valor 1:");
		scanf("%i", &a);
		printf("Ingrese el valor 2:");
		scanf("%i", &b);

		resultado = divi(a, b);
		printf("\nLa Division es: %i", resultado);
		break;

	default:
		printf("Opción invalida");
		break;
	}

	return 0;
}

int suma(int a, int b) {
	int Suma = 0;
	Suma = a + b;
	return Suma;
}

int resta(int a, int b) {
	int Resta = 0;
	Resta = a - b;
	return Resta;
}

int multi(int a, int b) {
	int Multi = 0;
	Multi = a * b;
	return Multi;
}

int divi(int a, int b) {
	int Divi = 0;
	Divi = a / b;
	return Divi;
}