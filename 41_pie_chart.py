from pylab import *

marks = [30, 25, 20, 25]
subjects = ["Python", "Java", "PHP", "C++"]

pie(marks, labels=subjects)

title("Subject Marks")

show()