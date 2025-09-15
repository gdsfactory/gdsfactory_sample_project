import gdsfactory as gf



@gf.cell
def dbr2():
    from mycspdk.dbr import dbr
    return dbr()
