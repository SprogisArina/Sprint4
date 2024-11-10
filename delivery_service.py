# Посылка №124355008
def count_platforms(weights: list[int], limit: int) -> int:
    sorted_weights = sorted(weights)
    left_pointer: int = 0
    right_pointer: int = len(weights) - 1
    platforms_amount: int = 0
    while left_pointer <= right_pointer:
        sum_weight: int = (
            sorted_weights[left_pointer] + sorted_weights[right_pointer])
        if sum_weight <= limit:
            left_pointer += 1
        right_pointer -= 1
        platforms_amount += 1
    return platforms_amount


if __name__ == '__main__':
    line: str = input()
    limit: int = int(input())
    weights: list[int] = [int(weight) for weight in line.split(' ')]
    result: int = count_platforms(weights, limit)
    print(result)
