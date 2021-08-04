import sys

def hello_world(name):
    print(f"hello {name}!")


if __name__ == "__main__":
    print(sys.argv)
    hello_world(sys.argv[1])