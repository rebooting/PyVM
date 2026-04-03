
from .vm import ToyVM

if __name__ == "__main__":
    # example program to move 69 into R0 and print it
    # mov R0, 69
    # print R0
    # halt
    prog = [4, 0, 69, 3, 0, 99]

    toy_vm = ToyVM()
    toy_vm.load(prog)
    toy_vm.run()