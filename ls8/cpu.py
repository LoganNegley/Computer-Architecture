"""CPU functionality."""

import sys


HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 #256 bytes memory
        self.reg = [0] * 8 #8 registers
        self.pc = 0        #program counter----currently executing instuction
        self.running = True #if program is running 


    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self, file):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # Bringing in dynamic programs
        with open(file) as f:
            for line in f:
                print(line)

        # for instrucion in program:
        #     print(instrucion)

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while self.running:
            instrucion = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            
            if instrucion == LDI: #store value in register or set register to value
                #register location at pc + 1
                #value is at pc + 2
                self.reg[operand_a] = operand_b
                self.pc += 3

            elif instrucion == PRN: #PRN prints numeric value stored in given register
                print(self.reg[operand_a])
                self.pc += 2

            elif instrucion == HLT: #stops program running 
                self.running = False
                self.pc += 1




