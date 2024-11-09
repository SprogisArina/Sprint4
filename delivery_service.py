def count_platforms(weights: list, limit: int) -> int:
    weights.sort()
    left_pointer: int = 0
    right_pointer: int = len(weights) - 1
    platforms_amount: int = 0
    while left_pointer <= right_pointer:
        sum_weight: int = weights[left_pointer] + weights[right_pointer]
        if sum_weight <= limit:
            platforms_amount += 1
            left_pointer += 1
            right_pointer -= 1
        elif weights[right_pointer] > limit:
            raise ValueError('Weight is over the limit.')
        elif sum_weight > limit:
            right_pointer -= 1
            platforms_amount += 1
    return platforms_amount


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        line: str = file_in.readline().rstrip()
        limit: int = int(file_in.readline().rstrip())
        weights: list[int] = [int(_) for _ in line.split(' ')]
    result: int = count_platforms(weights, limit)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
