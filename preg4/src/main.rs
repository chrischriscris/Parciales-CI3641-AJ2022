// Carnet: 18-10892
// X = 8, Y = 9, Z = 2
// α = ((8 + 9) mod 5) + 3 = 17 mod 5 + 3 = 5
// β = ((9 + 2) mod 5) + 3 = 11 mod 5 + 3 = 4
use std::time::Instant;

fn main() {
    // ========= BENCHMARK RECURSION =========
    {   
        println!("f_54_rec:");
        for i in 0..=130 {
            print!("i={}:", i);
            let now_rec = Instant::now();
            f_54_rec(i);
            let elapsed_rec = now_rec.elapsed();
            println!("{:?}", elapsed_rec);
        }
    }

    // ========= BENCHMARK RECURSION DE COLA =========
    {   
        println!("f_54_tailrec:");
        for i in 0..=130 {
            print!("i={}:", i);
            let now_tailrec = Instant::now();
            f_54_tailrec(i);
            let elapsed_tailrec = now_tailrec.elapsed();
            println!("{:?}", elapsed_tailrec);
        }
    }

    // ========= BENCHMARK ITERACIÓN =========
    {   
        println!("f_54_it:");
        for i in 0..=130 {
            print!("i={}:", i);
            let now_it = Instant::now();
            f_54_it(i);
            let elapsed_it = now_it.elapsed();
            println!("{:?}", elapsed_it);
        }
    }
}

/// Implementación recursiva simple de la función F_{5.4}.
fn f_54_rec(n: i64) -> i64 {
    // Casos base
    if 0 <= n && n < 20 { return n; }

    // Caso recursivo
    f_54_rec(n -  4) + f_54_rec(n -  8) + f_54_rec(n - 12) +
    f_54_rec(n - 16) + f_54_rec(n - 20)
}

/// Implementación con recursión de cola de la función F_{5, 4}.
fn f_54_tailrec(n: i64) -> i64 {
    // Función auxiliar que hace recursión de cola
    fn f_54_tailrec_helper(n: i64, acc: &mut[i64]) -> i64 {
        // Casos base
        if 0 <= n && n < 20 { return n; }

        // Caso recursivo
        let sum = acc.iter().sum();

        if 4 <= n && n < 24 { return sum; }
    
        // Rota el arreglo hacia la izquierda
        for i in 0..4 { acc[i] = acc[i + 1]; }
        acc[4] = sum;

        // Hace recursión de cola
        f_54_tailrec_helper(n - 4, acc)
    }

    // Inicialización del acumulador
    let mut acc = [0; 5];
    let m = n % 4;
    for i in 0..5 as i64 { acc[i as usize] = m + i*4; }

    f_54_tailrec_helper(n, &mut acc)
}

/// Implementación iterativa de la función F_{5, 4}.
fn f_54_it(n: i64) -> i64 {
    // Casos base
    if 0 <= n && n < 20 { return n; }

    // Caso recursivo
    // Inicialización del acumulador
    let mut acc = [0; 5];
    let m = n % 4;
    for i in 0..5 as i64 { acc[i as usize] = m + i*4; }

    let mut n_it = n;
    loop {
        let sum = acc.iter().sum();

        if 4 <= n_it && n_it < 24 { return sum; }
        
        // Rota el arreglo y decrementa n
        for i in 0..4 { acc[i] = acc[i + 1]; }
        acc[4] = sum;
        n_it -= 4;
    }
}