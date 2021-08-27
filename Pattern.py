# Implement function build_tower
#
def build_tower(n):
    asterics = '*'
    num_spaces = n * 2 - 2
    res = []
    for i in range(n):
        res.append(f"{' ' * (num_spaces // 2)}{asterics}{' ' * (num_spaces // 2)}")
        asterics += '**'
        num_spaces -= 2

    return res

print(build_tower(3))

