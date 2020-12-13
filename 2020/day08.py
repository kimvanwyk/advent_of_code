import operator

import attr

import common
import settings


EXIT_REASON_REPEAT = 1
EXIT_REASON_JUMP_PAST_END = 2


@attr.s
class Console:
    instructions = attr.ib()
    accumulator = attr.ib(default=0)
    executed_instructions = attr.ib(default=attr.Factory(list))
    reason = attr.ib(default=None)

    def get_numerical_op(self, instruction):
        amt = instruction.split(" ")[-1]
        op = operator.add if amt[0] == "+" else operator.sub
        return (op, int(amt[1:]))

    def modify_instruction(self, instruction_number):
        return self.instructions[instruction_number]

    def process(self):
        n = 0
        while True:
            if n in self.executed_instructions:
                self.reason = EXIT_REASON_REPEAT
                break
            if n >= len(self.instructions):
                self.reason = EXIT_REASON_JUMP_PAST_END
                break
            inst = self.instructions[n]
            self.executed_instructions.append(n)
            inst = self.modify_instruction(n)
            if "nop" in inst:
                n += 1
            elif "acc" in inst:
                (op, amt) = self.get_numerical_op(inst)
                self.accumulator = op(self.accumulator, amt)
                n += 1
            elif "jmp" in inst:
                (op, amt) = self.get_numerical_op(inst)
                n = op(n, amt)


def process():
    input_data = common.read_string_file()
    console = Console([l for l in input_data])
    console.process()
    return console


def part_1():
    console = process()
    if settings.settings.debug:
        print(console.executed_instructions)
        print(console.accumulator)
    return console.accumulator


def part_2():
    class ModifyingConsole(Console):
        def __init__(self):
            self.tried = []

        def modify_instruction(self, instruction_number):
            instruction = self.instructions[instruction_number]
            if instruction_number not in self.tried:
                for (orig, new) in (("jmp", "nop"), ("nop", "jmp")):
                    if orig in instruction:
                        return instruction.replace(orig, new)
            return instruction

    return process()
