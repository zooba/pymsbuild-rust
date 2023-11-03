# pymsbuild-rust

This is a [pymsbuild](https://pypi.org/project/pymsbuild) extension for
compiling native modules written in Rust.

# Quick Start

In your `_msbuild.py`, import `RustPydFile` from `pymsbuild_rust`
(using `import *` is okay).

**TODO: HOW TO SPECIFY FILES?**

```
from pymsbuild import *
from pymsbuild_winui import *

METADATA = {...}

PACKAGE = Package(
    'package',
    PyFile("__init__.py"),
    RustPydFile(
        "native",
        # TODO: WHAT TYPES GO HERE?
    ),
)
```
