from datetime import datetime
input1 = input()
date = datetime.strptime(input1, '%B %d, %Y %H:%M')
d1 = datetime.strptime(str(date.year) + ' January 01, 00:00', '%B %d, %Y %H:%M')
d2 = date
d3 = datetime.strptime(str(date.year + 1) + ' January 01, 00:00', '%B %d, %Y %H:%M')
dm = (d2 - d1).total_seconds()
dy = (d3 - d1).total_seconds()
ans = (dm / dy) * 100
print(ans)


