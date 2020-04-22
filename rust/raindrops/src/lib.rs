const SOUNDS: [(u32, &str); 3] = [(3, "Pling"), (5, "Plang"), (7, "Plong")];

// Plops away depending on the dividability of the input number
pub fn raindrops(drops: u32) -> String {
    let mut vec: Vec<&str> = Vec::new();
    for (n, sound) in SOUNDS.iter() {
        if drops % n == 0 {
            vec.push(sound)
        }
    }

    if vec.is_empty() {
        drops.to_string()
    } else {
        vec.join("")
    }
}
