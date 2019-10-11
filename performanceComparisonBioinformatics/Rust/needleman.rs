use std::fs::File;
use std::io::{BufRead, BufReader};
use std::cmp;
use std::env;
const GAP: i32 = 2;
const MUT: i32=1;
fn main() {
    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);



    let dna1="ATCGATCGATCGATCGATCGAAAAAAAAAAAAA";
    let dna2="CGTACGTACGTACGTAAAAAAAAAAAAAA";
    needelman(dna1,dna2);
    let cad1=readFile("fastaFiles/".to_string()+&args[1].to_owned());
    //println!("{}",cad1);
    let cad2=readFile("fastaFiles/".to_string()+&args[2].to_owned());
    //println!("{}",cad2);
    needelman(&cad1.to_owned(),&cad2.to_owned());
}

fn readFile(file1:String) ->String{
    let mut ans="".to_string();
    let filename = file1;
    // Open the file in read-only mode (ignoring errors).
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for (mut index, line) in reader.lines().enumerate() {
        let line = line.unwrap(); // Ignore errors.
        // Show the line and its number.
        if(index!=0){
        //println!("{}. {}", index + 1, line);
        ans+=&line;
        }
        else{
            index+=1;
        }
    }
    return ans;
}

fn needelman(cadena1:&str,cadena2:&str){
    let len_cad_1=cadena1.chars().count();
    let len_matrix=(len_cad_1)+1;
    //println!("{}",cadena1);
    let len_cad_2=cadena2.chars().count();
    let len_matrix_2=(len_cad_2)+1;
    //println!("{}",cadena2 );
    let mut matriz_dinamica = vec![vec![0i32; len_matrix_2]; len_matrix];
    matriz_dinamica[0][0]=0;
    let mut x = 0; // mut x: i32
    let mut done = false; // mut done: bool
    
    while !done {
        if x == matriz_dinamica.len()-1 {
            done = true;
        }
        matriz_dinamica[x][0]=(x as i32) *GAP  ;
        //println!("{}",matriz_dinamica[x][0]);
        x += 1;
    }
    
    let mut z=0;
    done=false;
    while !done {
        if z == matriz_dinamica[0].len()-1 {
            done = true;
        }
        matriz_dinamica[0][z]=(z as i32) *GAP  ;
        //println!("{}",matriz_dinamica[0][z]);
        z += 1;
    }
    let ch1=cadena1.chars();
    let ch2=cadena2.chars();
    let mut i=1;
    while i<matriz_dinamica.len(){
        let mut j=1;
        while j<matriz_dinamica[i].len(){
            let upVal=matriz_dinamica[i-1][j];
            let leftVal=matriz_dinamica[i][j-1];
            let diagVal=matriz_dinamica[i-1][j-1];

            let costUp=upVal+GAP;
            let costLeft=leftVal+GAP;
            let mut costDiag=diagVal;
            //println!("{}",cadena1.chars().nth(i-1).unwrap()==cadena2.chars().nth(j-1).unwrap());
            if(cadena1.chars().nth(i-1).unwrap()!=cadena2.chars().nth(j-1).unwrap()){
                costDiag+=MUT;
            }
            if(costUp==0){
                //println!("{}",i-1);
            }
            if(costLeft==0){
                //println!("{}",j-1);
            }
            if(costDiag==0){
                //println!("{}",i-1);
                //println!("{}","----");
                //println!("{}",j-1);
            }
            let min1=cmp::min(costUp, costLeft);
            let min=cmp::min(min1,costDiag);
            matriz_dinamica[i][j]=min;
            j+=1;
        }
        i+=1;
    }

    println!("{}",matriz_dinamica[len_cad_1][len_cad_2]);
    
}