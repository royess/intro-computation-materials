import math

num_cakes, num_friends = map(int, input().split(' '))
radii = map(float, input().split(' '))
vols = [math.pi * r ** 2 for r in radii]

max_vol_ub = max(vols)
max_vol_lb = 0

while '{:.3f}'.format(max_vol_lb) != '{:.3f}'.format(max_vol_ub):
    max_vol = (max_vol_ub + max_vol_lb) / 2
    num_fed = 0

    for v in vols:
        num_fed += math.floor(v / max_vol)

    if num_fed >= num_friends + 1:
        max_vol_lb = max_vol
    else:
        max_vol_ub = max_vol

print('{:.3f}'.format(max_vol_lb))