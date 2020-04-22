// Find the nth prime number
pub fn nth(n: u32) -> u32 {
    let mut primes: Vec<u32> = vec![2];

    loop {
        if primes.len() as u32 > n {
            return primes[n as usize];
        }
        next(&mut primes);
    }
}

// Given a vector of N prime numbers, find the N+1 number
fn next(primes: &mut Vec<u32>) {
    let dividable = |n| {
        for prime in primes.iter() {
            // If a number can't be divided by any lower prime number, it's a prime number
            if n % prime == 0 {
                return true;
            }
        }
        false
    };

    let mut i: u32 = primes[primes.len() - 1];

    loop {
        i += 1;
        if !dividable(i) {
            primes.push(i);
            break;
        }
    }
}
