# inputs = [12, 1969, 100756]
with open('input.txt', 'r') as fh:
    inputs = [int(l.strip()) for l in fh]

def calc_mass_fuel(mass):
    return int(mass/3) - 2

def calc_module_fuel(mass):
    res = [calc_mass_fuel(mass)]
    while res[-1] > 0:
        res.append(calc_mass_fuel(res[-1]))
    return sum([r for r in res if r > 0])

# for i in inputs:
#     print(calc_module_fuel(i))
if 1:
    def sum_inputs(inputs):
        return(sum([calc_module_fuel(i) for i in inputs]))

    print(sum_inputs(inputs))
