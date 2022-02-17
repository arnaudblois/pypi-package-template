"""Final function to run after templating."""


import os
from pathlib import Path
import shutil


def finalize(context: dict, output_dir: Path):
    """Copy the templated selected license and delete the others."""
    try:
        license_to_copy = (output_dir / "licenses" / context["license"]).resolve(strict=True)
    except FileNotFoundError:
        raise BadInputError

    shutil.copy(license_to_copy, output_dir)
    os.rename(output_dir / context["license"], output_dir / "LICENSE")
    shutil.rmtree(output_dir / "licenses")
