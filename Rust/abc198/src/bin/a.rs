use proconio::input;

fn main() {
    input! {
        mut n: usize,
    }
    if n == 1 {
        println!("{}", 0);
        return;
    }
    println!("{}", n - 1);
}
