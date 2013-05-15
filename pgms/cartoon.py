from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([3.2, 3.1], origin=[1.7, 2.3])

pgm.add_node(daft.Node(u"sprop", r"$\Theta_\star$", 3, 5))
pgm.add_node(daft.Node(u"pprop", r"$\Theta_\mathrm{p}$", 4, 5))

pgm.add_node(daft.Node(u"star", r"$\star_n$", 3, 4))

pgm.add_node(daft.Node(u"select", r"S", 2, 3.5))
pgm.add_node(daft.Node(u"planet", r"$\mathrm{p}_n ^m$", 4, 3.5))

pgm.add_node(daft.Node(u"observations", r"$\mathbf{X}_n$", 3, 3,
                       observed=True))

pgm.add_edge(u"sprop", u"star")
pgm.add_edge(u"pprop", u"planet")

pgm.add_edge(u"star", u"observations")
pgm.add_edge(u"star", u"planet")

pgm.add_edge(u"planet", u"observations")
pgm.add_edge(u"select", u"observations")

pgm.add_plate(daft.Plate([3.5, 3, 1.2, 1],
              label=r"planets $m$", position=u"bottom right"))

pgm.add_plate(daft.Plate([2.5, 2.45, 2.3, 2.05],
              label=r"targets $n$", position=u"bottom right"))

pgm.render()
pgm.figure.savefig("../document/figures/full-pgm.pdf")
