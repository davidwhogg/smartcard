from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([3.5, 5], origin=[1.5, 0.4])

pgm.add_node(daft.Node(u"sprop", r"$\Theta_\star$", 3, 5))
pgm.add_node(daft.Node(u"pprop", r"$\Theta_\mathrm{p}$", 4, 5))

pgm.add_node(daft.Node(u"star", r"$\star_n$", 3, 4))

pgm.add_node(daft.Node(u"select", r"S", 2, 2))
pgm.add_node(daft.Node(u"planet", r"$\mathrm{p}_n ^m$", 4, 3))

pgm.add_node(daft.Node(u"on", r"$\mathbf{X}_n ^m$", 3.5, 2))

pgm.add_node(daft.Node(u"observations", r"$\mathbf{X}_n$", 3.5, 1,
                       observed=True))

pgm.add_edge(u"sprop", u"star")
pgm.add_edge(u"pprop", u"planet")

pgm.add_edge(u"star", u"on")
pgm.add_edge(u"star", u"planet")

pgm.add_edge(u"planet", u"on")
pgm.add_edge(u"select", u"observations")

pgm.add_edge(u"on", u"observations")

pgm.add_plate(daft.Plate([3, 1.5, 1.6, 2],
              label=r"planets $m$", position=u"bottom right"))

pgm.add_plate(daft.Plate([2.5, 0.45, 2.25, 4.05],
              label=r"targets $n$"))

pgm.render()
pgm.figure.savefig("../document/figures/full-pgm.pdf")
