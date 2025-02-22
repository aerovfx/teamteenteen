def count_ways(n, weights):
    weights.sort()  # Sắp xếp các quả cân theo thứ tự tăng dần
    count = 0

    def dequy_count(index, left_weight, right_weight):
        nonlocal count
        if index == n:
            if left_weight <= right_weight:
                count += 1
            return

        # Đặt quả cân ở đĩa trái và đệ quy
        dequy_count(index + 1, left_weight + weights[index], right_weight)
        # print(weights[index])
        # Đặt quả cân ở đĩa phải và đệ quy
        dequy_count(index + 1, left_weight, right_weight + weights[index])

    dequy_count(0, 0, 0)
    return count

# Đọc dữ liệu từ file CANDIA.INP
with open("CANDIA.INP", "r") as f:
    n = int(f.readline())
    weights = list(map(int, f.readline().split()))

# Tính và in ra kết quả
result = count_ways(n, weights)
print(result)