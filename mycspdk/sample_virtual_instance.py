import gdsfactory as gf


@gf.cell(tags=["vinst"])
def sample_virtual_instance() -> gf.Component:
    """Demo non manhattan virtual instance."""
    nm = 1e-3
    c = gf.Component()
    w = gf.components.straight(length=4 * nm, width=4 * nm)
    w1 = c.create_vinst(w)
    w1.rotate(30)

    w2 = c.create_vinst(w)
    w2.connect("o1", w1["o2"])
    return c
