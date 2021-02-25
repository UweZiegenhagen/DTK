def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([])

with open ("extern.tex", "r") as templatefile:
	template=templatefile.read()

    with open ("generated.tex", "w") as texfile:
        for x in seq(0.1, 0.9, 0.05):
            texfile.write(template.replace("@@",str(x)))
            texfile.write("\n\n")
