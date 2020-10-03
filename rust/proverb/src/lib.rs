pub fn build_proverb(list: &[&str]) -> String {
    let mut c: String = String::from("");
    let mut maybe_previous: Option<&str> = None;
    for text in list.into_iter() {
        if let Some(previous) = maybe_previous {
            c = format!("{}For want of a {} the {} was lost.\n", c, previous, text);
        }
        maybe_previous = Some(text)
    }

    if let Some(first) = list.first() {
        c = format!("{}And all for the want of a {}.", c, first);
    }

    return c;
}
