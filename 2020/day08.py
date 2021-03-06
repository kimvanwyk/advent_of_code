import operator

import attr

import common
from common import debug
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
        self.reason = None
        self.executed_instructions = []
        self.accumulator = 0
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


def process(console_cls=Console):
    input_data = common.read_string_file()
    console = console_cls([l for l in input_data])
    return console


def part_1():
    console = process()
    console.process()
    debug(console.executed_instructions)
    debug(console.accumulator)
    return console.accumulator


def part_2():
    class ModifyingConsole(Console):
        def modify_instruction(self, instruction_number):
            instruction = self.instructions[instruction_number]
            if (instruction_number not in self.options_tried) and not (self.tried):
                self.tried = True
                self.options_tried.append(instruction_number)
                for (orig, new) in (("jmp", "nop"), ("nop", "jmp")):
                    if orig in instruction:
                        debug(
                            f"Replacing {orig} with {new} for instruction '{instruction}' (number {instruction_number})"
                        )
                        return instruction.replace(orig, new)
            return instruction

        def process_with_replacement(self):
            self.options_tried = []
            self.possible_subs = len(
                [i for i in self.instructions if "nop" in i or "jmp" in i]
            )
            debug(f"Possible substitutions: {self.possible_subs}")
            tries = 0
            while tries <= self.possible_subs:
                self.tried = False
                debug(f"Try number {tries}")
                self.process()
                debug(f"Exit reason: {self.reason}")
                debug(self.executed_instructions)

                if self.reason == EXIT_REASON_JUMP_PAST_END:
                    break
                tries += 1

    console = process(ModifyingConsole)
    console.process_with_replacement()
    debug(console.reason)
    debug(console.accumulator)
    return console.accumulator
