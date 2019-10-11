#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	char *cadena1; 
	int size;
	size = ae_load_file_to_memory("prueba1.fa", &cadena1);
	printf("%d",size);
	if (size < 0) 
	{ 
		puts("Error loading file");
		return 1;
	} 
	do { 
		putchar(cadena1[size-1]);
		//printf("%s",cadena1[size-1]);
		size--;
	} 
	while(size > 0);
	return 0;
}


int ae_load_file_to_memory(const char *filename, char **result) 
{ 
	int size = 0;
	FILE *f = fopen(filename, "rb");
	if (f == NULL) 
	{ 
		*result = NULL;
		return -1; // -1 means file opening fail 
	} 
	fseek(f, 0, SEEK_END);
	size = ftell(f);
	printf("%d",size);
	fseek(f, 0, SEEK_SET);
	*result = (char *)malloc(size+1);
	if (size != fread(*result, sizeof(char), size, f)) 
	{ 
		free(*result);
		return -2; // -2 means file reading fail 
	} 
	fclose(f);
	(*result)[size] = 0;
	return size;
}
