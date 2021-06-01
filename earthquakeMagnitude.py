# Earthquake Magnitude

import math

amp = [141000, 87598000, 5296000, 32000]
mag = []
for a in amp:
    mag.append(math.log10(a))

print(mag)

#소수점자리 깔끔하게 처리하는거 다시하기
