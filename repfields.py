age = 24
print("My age is " + str(age) + " years ")
print("My age is {0} years".format(age)) # same op as last line
print("There are {0} days in {1}, {2},{3},{4},{5},{6} and {7}  and {8} days in months {9},{10},{11},{12} and in {13}, {14} or {15} days "
.format(31, "Jan","Mar","May","Jul","Aug", "Oct", "Dec", 30, "Apr","Jun","Sep","Nov","Feb",28,29))
print("There are {0} days in Jan, Mar, May, Jul, Aug,Oct and Dec" .format(31))

print("Jan:{2}, Feb:{0}, Mar:{2}, Apr:{1},May:{2}, Jun:{1}, Jul:{2}, Aug:{2}, Sep:{1}, Oct:{2}, Nov:{1}, Dec:{2}".format(28,30,31))

print("""Jan:{2}
Feb:{0}
Mar:{2}
Apr:{1}
May:{2}
Jun:{1}
Jul:{2}
Aug:{2}
Sep:{1}
Oct:{2}
Nov:{1}
Dec:{2}""".format(28,30,31))