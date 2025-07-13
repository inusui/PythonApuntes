import sys

DATABASE_PATH = "clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/test_clientes.csv"
