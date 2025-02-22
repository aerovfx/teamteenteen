từ dãy số tự nhiên 1, 2, 3, 4, 5, 6, 7, 8,9, 10, ..., N người ta sắp xếp lại dãy số này theo số dư trong các phép chia các số hạng của dãy số cho một số tự nhiên K là ước nào đó của N như sau:
Đoạn thứ nhất gồm tất cả các số chia hết cho K.
Đoạn thứ hai gồm tất cả các số chia K dư 1
Đoạn thứ ba gồm tất cả các số chia K dư 2
Đoạn thứ tư gồm tất cả các số chia K dư 3
Đoạn thứ năm gồm tất cả các số chia K dư 4
...
Đoạn cuối cùng gồm tất cả các số chia K dư K -1
Các số hạng trong mỗi đoạn cũng được sắp xếp theo chiều tăng dần.
Ví dụ: Với N = 12 và K = 4 sau khi sắp xếp ta có dãy số sau: 
4, 8, 12, 
1, 5, 9, 
2, 6, 10, 
3, 7, 11

sau khi sắp xếp xong ta có dãy
4, 8, 12, 1, 5, 9, 2, 6, 10, 3, 7, 11

Cho 3 số nguyên dương N, K, M ( Với K là ước của N và M < = N)
Yêu cầu: Viết ra dãy đã sắp xếp 4, 8, 12, 1, 5, 9, 2, 6, 10, 3, 7, 11
Dữ liệu vào đọc từ file MODK.INP gồm 3 số nguyên dương N, K, M trên cùng 1 dòng, mỗi số cách nhau bởi một dấu cách. K là ước của N. M < = N
Dữ liệu ghi ra văn bản MODK.OUT là dãy số cần tìm
MODK.INP
N  K M
12 4 6
MODK.OUT
4, 8, 12, 1, 5, 9, 2, 6, 10, 3, 7, 11

Thuật toán
Đọc dữ liệu từ file MODK.INP để lấy giá trị của N, K và M.
Xác định dãy số hạng mà số M nằm trong. Để làm điều này, tính số lượng phần tử trong mỗi đoạn:
Số lượng phần tử trong mỗi đoạn là N / K.
Số lượng đoạn là K.
Tìm số hạng thứ M trong đoạn tương ứng:
Tính số thứ tự của đoạn mà số M nằm trong: segment_number = (M - 1) / (N / K).
Tính số thứ tự của số M trong đoạn: m_in_segment = (M - 1) % (N / K).
Tìm số hạng thứ M bằng cách tính: result = K * m_in_segment + segment_number.
Ghi kết quả vào file MODK.OUT.