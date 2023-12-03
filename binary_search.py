import random

def create_array(*, arr_len: int=100, min_val: int=0, max_val: int=100) -> list[int]:
    return[random.randint(min_val, max_val) for _ in range(arr_len)]

def binary_search(*, source: list[int], quary: int) -> int|None:
    start = 0
    end = len(source) - 1
    while end - start > 0:
        idx = (end - start) // 2 + start
        if source[idx] == quary:
            return idx
        if source[idx] < quary:
            start = idx + 1
        else:
            end = idx - 1
    else: 
        return None
    
    
if __name__ == '__main__':
    numbers = sorted(create_array())
    print(numbers)

    print(binary_search(source=numbers, quary=50))
    