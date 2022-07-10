// X = 8, Y = 9, Z = 2
// α = ((8 + 9) mod 5) + 3 = 17 mod 5 + 3 = 5
// β = ((9 + 2) mod 5) + 3 = 11 mod 5 + 3 = 4

fn main() {
    for i in 0..=125 {
        println!("f_54_rec({})     : {}", i, f_54_rec(i));
    }

    for i in 0..=125 {
        println!("f_54_tailrec({}) : {}", i, f_54_tailrec(i));
    }

    for i in 0..=125 {
        println!("f_54_it({})      : {}", i, f_54_it(i));
    }
}

fn f_54_rec(n: i32) -> i32 {
    // Casos base
    if 0 <= n && n < 20 {
        return n;
    }

    // Caso recursivo
    f_54_rec(n -  4) + f_54_rec(n -  8) + f_54_rec(n - 12) +
    f_54_rec(n - 16) + f_54_rec(n - 20)
}

fn f_54_tailrec(n: i32) -> i32 {
    // Función auxiliar que hace recursión de cola
    fn f_54_tailrec_helper(n: i32, acc: &mut[i32]) -> i32 {
        // Casos base
        if 0 <= n && n < 20 {
            return n;
        }

        // Caso recursivo
        let sum = acc.iter().sum();

        if 4 <= n && n < 24 {
            sum
        } else {
            // Rota el arreglo hacia la izquierda
            for i in 0..4 {
                acc[i] = acc[i + 1];
            }
            acc[4] = sum;
            
            f_54_tailrec_helper(n - 4, acc)
        }
    }

    // Inicialización del acumulador
    let mut acc = [0; 5];
    let m = n % 4;
    for i in 0..5 as i32 {
        acc[i as usize] = m + i*4;
    }

    f_54_tailrec_helper(n, &mut acc)
}

fn f_54_it(n: i32) -> i32 {
    // Casos base
    if 0 <= n && n < 20 {
        return n;
    }

    // Caso recursivo
    // Inicialización del acumulador
    let mut acc = [0; 5];
    let m = n % 4;
    for i in 0..5 as i32 {
        acc[i as usize] = m + i*4;
    }

    loop {
        let sum = acc.iter().sum();

        if 4 <= n && n < 24 {
            return sum;
        } else {
            for i in 0..4 {
                acc[i] = acc[i + 1];
            }
            acc[4] = sum;
        }
    }
}