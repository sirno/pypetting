def write_gwl(path, gwl):
    """Write a gwl file."""
    with open(path, "w") as fd:
        fd.write("C;INIT - gwl created by pypetting")
        fd.writelines(gwl)
