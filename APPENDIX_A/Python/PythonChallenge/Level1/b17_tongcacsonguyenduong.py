#Bài 17. Viết chương trình tính tổng của các chữ số của môt số nguyên dương n trong Python. Số nguyên dương n được nhập từ bàn phím.
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));

