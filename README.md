# pymsbuild-rust

This is a [pymsbuild](https://pypi.org/project/pymsbuild) extension for
compiling native modules written in Rust.

# Quick Start

In your `_msbuild.py`, import `RustPydFile` and `Cargo` from `pymsbuild_rust`
(using `import *` is okay).

While Cargo is used to run the build, all files need to be specified from your
`_msbuild.py` file to be collected when building an sdist, and to handle
incremental builds correctly.

```python
from pymsbuild import *
from pymsbuild_rust import *

METADATA = {...}

PACKAGE = Package(
    'package',
    PyFile("__init__.py"),
    RustPydFile(
        "native",
        Cargo("Cargo.toml"),
        SourceFile("src/lib.rs"),
        source="native"
    ),
)
```

The `Cargo` element refers to your `Cargo.toml`, which should specify that a
`cdylib` is to be built. The name of the lib should match the name provided to
`RustPydFile`, which will also be the resulting extension module's name.

```toml
[lib]
name = "native"
crate-type = ["cdylib"]
```

Other than this, the module may build in any way it likes. Most likely, you
will use [PyO3](https://pyo3.rs/), and so should follow their documentation for
instructions on setting up the rest of your project (ignoring the parts that
refer to other build backends such as Maturin).

Other files listed in the `RustPydFile` will be included in your sdist, and will
be used to determine whether the module needs to be recompiled.

Theoretically, multiple `Cargo` elements will trigger multiple builds. However,
as they will all be directed into the same directory, this may not do what you
hope. Advanced users may find some value regardless.
