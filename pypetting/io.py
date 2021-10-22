"""Write work lists."""


def write_gwl(path, gwl):
    """Write a gwl file."""
    with open(path, "w", encoding="ascii") as file_descriptor:
        file_descriptor.write("C;INIT - gwl created by pypetting")
        file_descriptor.writelines(gwl)
