import unittest
import pyvm.vm
class HltTest(unittest.TestCase):
    def test_htl_instruction(self):
        # NOP, NOP NOP, HLT
        program = [0,0,0,99]
        toy_vm = pyvm.vm.ToyVM()
        toy_vm.load(program)
        ret_val = toy_vm.run()
        # CS should be at 4
        self.assertEqual(3,toy_vm.register['CP'])
        self.assertTrue(ret_val)

    def test_htl_instruction_no_hlt(self):
        # NOP, NOP, NOP
        program = [0,0,0]
        toy_vm = pyvm.vm.ToyVM()
        toy_vm.load(program)
        ret_val = toy_vm.run()
        self.assertEqual(3,toy_vm.register['CP'])
        self.assertFalse(ret_val)
