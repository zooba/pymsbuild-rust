from package1.module1 import sum_as_string

v = sum_as_string(1, 1)
if v != "2":
    raise RuntimeError(f"Expected 1+1=='2', got {v!r} ({type(v)})")
