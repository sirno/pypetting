"""Write work lists."""


def write_gwl(path, gwl):
    """Write a gwl file."""
    with open(path, "wb") as file_descriptor:
        file_descriptor.write(b"C;INIT - gwl created by pypetting\n")
        file_descriptor.write(b"\n".join(gwl))
