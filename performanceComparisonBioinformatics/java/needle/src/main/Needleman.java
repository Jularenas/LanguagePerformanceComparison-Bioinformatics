package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class Needleman {

	private static String cadena1;

	private static String cadena2;

	public final static long GAP=2;

	public final static long MUT=1;

	private static long score;

	private static long[][]matrizDinamica;


	public static void main(String[] args) {
		System.out.println("Hi");
		String file1=args[0];
		try(BufferedReader in= new BufferedReader(new FileReader(new File("./data/fastaFiles/"+file1)))){
			String ln1=in.readLine();
			ln1=in.readLine();
			String dna1="";
			while(ln1!=null) {
				//System.out.prlongln(cs+=ln1.length());
				dna1+=ln1;
				ln1=in.readLine();
			}
			cadena1=dna1;
		}
		catch(Exception e) {
			
		}
		String file2=args[1];
		try(BufferedReader in= new BufferedReader(new FileReader(new File("./data/fastaFiles/"+file2)))){
			String ln1=in.readLine();
			ln1=in.readLine();
			String dna2="";
			while(ln1!=null) {
				//System.out.prlongln(cs+=ln1.length());
				dna2+=ln1;
				ln1=in.readLine();
			}
			cadena2=dna2;
		}
		catch(Exception e) {
			
		}
		dinamica(cadena1, cadena2);
	}

	public static int  dinamica(String cad1,String cad2) {

		///
		//Construcción matriz dinamica
		///
		matrizDinamica= new long [cad1.length()+1][cad2.length()+1];

		//Llenar scores de los extremos
		for (int i = 0; i < matrizDinamica.length; i++) {
			matrizDinamica[i][0]=i*GAP;
			//System.out.println(matrizDinamica[i][0]);
		}	
		for (int i = 1; i < matrizDinamica[0].length; i++) {
			matrizDinamica[0][i]=i*GAP;
			//System.out.println(matrizDinamica[0][i]);
		}

		for (int i = 1; i < matrizDinamica.length; i++) {
			for (int j = 1; j < matrizDinamica[i].length; j++) {
				long upVal=matrizDinamica[i-1][j];
				long leftVal=matrizDinamica[i][j-1];
				long diagVal=matrizDinamica[i-1][j-1];

				long costUp=0;
				long costDiag=diagVal;
				long costLeft=0;

				costUp=upVal+GAP;
				costLeft=leftVal+GAP;
				if(!(cad1.charAt(i-1)==cad2.charAt(j-1))) {
					costDiag+=MUT;
				}
				matrizDinamica[i][j]=Math.min(Math.min(costDiag, costLeft), costUp);
				//System.out.println(matrizDinamica[i][j]);
			}
		}
		score=matrizDinamica[cad1.length()][cad2.length()];
		System.out.println(score);
		return (int) score;
	}

}
