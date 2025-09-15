import gdsfactory as gf
from cspdk.si220.cband import cells

@gf.cell
def bend_euler() -> gf.Component:
    return cells.bend_euler()

@gf.cell
def bend_metal() -> gf.Component:
    return cells.bend_euler()