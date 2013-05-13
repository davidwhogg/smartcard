from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([3, 3], origin=[0.6, 0.3])

pgm.add_node(daft.Node(u"sprop", r"$\Theta_\star$", 2, 3))
pgm.add_node(daft.Node(u"pprop", r"$\Theta_\mathrm{p}$", 3, 3))

pgm.add_node(daft.Node(u"star", r"$\star_n$", 2, 2))
pgm.add_node(daft.Node(u"planet", r"$\mathrm{p}_n$", 3, 2))
pgm.add_node(daft.Node(u"select", r"S", 1, 2))

pgm.add_node(daft.Node(u"obs", r"$q_n$", 2, 1, observed=True))
pgm.add_node(daft.Node(u"on", r"$\mathbf{X}_n$", 3, 1, observed=True))

pgm.add_edge(u"sprop", u"star")
pgm.add_edge(u"pprop", u"planet")

pgm.add_edge(u"star", u"on")
pgm.add_edge(u"star", u"obs")

pgm.add_edge(u"planet", u"obs")
pgm.add_edge(u"planet", u"on")
pgm.add_edge(u"select", u"obs")

pgm.add_plate(daft.Plate([1.5, 0.45, 2, 2],
            label=r"planets $n$"))

pgm.render()
pgm.figure.savefig("simple.pdf")
