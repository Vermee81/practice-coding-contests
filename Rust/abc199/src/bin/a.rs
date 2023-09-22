use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        c: usize,
    }
    let is_less = a * a + b * b < c * c;
    println!("{}", if is_less {"Yes"} else {"No"});
}
