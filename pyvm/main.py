
from .vm import ToyVM

if __name__ == "__main__":
    prog = [4, 0, 69, 3, 0, 99]
    toy_vm = ToyVM()
    toy_vm.load(prog)
    toy_vm.run()