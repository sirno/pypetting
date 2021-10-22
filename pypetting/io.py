"""Write work lists."""


def write_gwl(path, gwl):
    """Write a gwl file."""
    with open(path, "w", encoding="latin9") as file_descriptor:
        file_descriptor.write("C;INIT - gwl created by pypetting\n")
        file_descriptor.write("\n".join(gwl))
