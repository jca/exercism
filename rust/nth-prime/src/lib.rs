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
    let i: u32 = primes[primes.len() - 1];

    primes.push(
        (i + 1..)
            .find(|j| {
                !primes
                    .iter()
                    .take_while(|&&prime| prime * prime <= *j)
                    .any(|&prime| j % prime == 0)
            })
            .unwrap(),
    );
}
