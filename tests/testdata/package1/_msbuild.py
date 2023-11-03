from pymsbuild import *
from pymsbuild_rust import *

METADATA = {
    "Name": "package1",
    "Version": "1.0",
}

PACKAGE = Package(
    "package1",
    RustPydFile(
        "module1",
        Cargo("module1/Cargo.toml"),
        SourceFile("module1/src/lib.rs"),
    )
)
