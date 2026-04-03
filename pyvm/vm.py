import copy
MEMORY_SIZE = 1024
TOP_OF_STACK_LOCATION = MEMORY_SIZE - 1

class ToyVM:

    def __init__(self):

        self.stack = []
        self.memory = [0] * MEMORY_SIZE
        self.ipc = 0
        self.register = {
            "R0": 0,
            "R1": 0,
            "SP": TOP_OF_STACK_LOCATION
        }
        self.program_end = 0 # for ensuring that stack does not overwrite CS
    
    
    def load(self, program: list[int]) -> None:
        # check program is below 1024
        if len(program)< MEMORY_SIZE:
            # deep copy
            self.memory[:len(program) ] = program
            self.ipc = 0
            self.program_end = len(program)
            self.stack = []
            self.register["SP"] = TOP_OF_STACK_LOCATION
        else:
            print("insufficient memory")

    def run(self):
        dispatch_table = {
            0: self.no_op,
            1: self.push,
            2: self.pop,
            3: self.print,
            4: self.mov,

        }
        while self.ipc < self.program_end:
            instr = self.memory[self.ipc]
            print(f" inst:{instr}")
            if instr == 99:
                print('halted')
                return True
            if instr < 5:
                handler = dispatch_table.get(instr)
                if handler is None:
                    print('Bad instruction')
                    return False
                ok = handler()
                if not ok:
                    print(f"execute error for {instr}")
                    return False
                ok = self.inc_ipc()
                if not ok:
                    print ("execute error next")



    def no_op(self):
        return True
    
    def push(self):
        if self.register["SP"] <= self.program_end:
            self.memory[self.register["SP"]] = self.register["R0"]
            self.register["SP"] = self.register["SP"] - 1
            return True
        else:
            print('STACK OVERFLOW')
            return False
    

    def pop(self)->bool:
        if self.register["SP"] < TOP_OF_STACK_LOCATION:
            self.register["R0"] = self.register["SP"]
            self.register["SP"] = self.register["SP"] - 1
            return True
        else:
            print('EMPTY STACK')
            return False

    def print(self):
        ret = self.inc_ipc()
        if ret == True:
            reg = self.memory[self.ipc]

            if reg == 0:
                print(f"{self.register['R0']}")
                return True

            elif reg == 1:
                print(f"{self.register['R1']}")
                return True
            else:
                print("no such register")
                return False            
        
    def mov(self)->bool:
        ret = self.inc_ipc()
        if ret == True:
            reg = self.memory[self.ipc]
        else:
            print ("error, outside program code")
            return False
        ret = self.inc_ipc()
        if ret == True:
           val = self.memory[self.ipc]
        else:
            print ("error, outside program code")
            return False

        if reg == 0:
            self.register["R0"] = val
        elif reg == 1:
            self.register["R1"] = val
        else:
            print("no such register")
            return False
        return True

    def inc_ipc(self)-> bool:
        if self.ipc < self.program_end:
            self.ipc = self.ipc + 1
            return True
        else:
            return False
        


