# Code to find sqroot using binary search
def get_sqrt(num, precision):
    start = 0
    end = num

    mid = start + (end - start) // 2
    ans = -1

    if num == 1:
        ans = 1
    elif num == 0:
        ans = 0
    else:
        while start < end:
            sq = mid * mid
            if sq == num:
                return mid
            elif sq > num:
                end = mid
            else:
                ans = mid
                start = mid + 1
            mid = start + (end - start) // 2

    power = 1
    while power <= precision:
        factor = 1 / (10 ** power)
        while ans * ans <= num:
            ans = ans + factor
        power += 1

    return round(ans, precision)


print(get_sqrt(50, 4))
