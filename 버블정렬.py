def bubble_sort(arr):
    n = len(arr)
    
    # 배열의 모든 원소를 비교하고 정렬합니다.
    for i in range(n):
        for j in range(0, n - i - 1):
            # 현재 원소가 다음 원소보다 크다면 위치를 교환합니다.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 정렬할 리스트를 생성합니다.
my_list = [64, 34, 25, 12, 22, 11, 90]

# 버블 정렬 함수를 호출하여 리스트를 정렬합니다.
bubble_sort(my_list)

# 정렬된 리스트를 출력합니다.
print("정렬된 리스트:", my_list)
