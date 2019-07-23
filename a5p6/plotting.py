# JTSK-350112
# a5 6.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de



out = open("result.dat", "w")

for i in range(5, -6, -1):
    output = str(i) + ' ' + str(i**2)
    out.write(output)
    out.write('\n')

out.close()

