# Endoh's quine language in python.
# The language is specially designed to print its own source and other payload easily,
# so you can use its own interpreter as payload to make a quine in any language.
# Endoh uses this to make a 51 language quine clique, which is much more impressive!
source = '''!# Endoh's quine language in python.
# The language is specially designed to print its own source and other payload easily,
# so you can use its own interpreter as payload to make a quine in any language.
# Endoh uses this to make a 51 language quine clique, which is much more impressive!
source = HHHHHH/&(*&)!HHHHHH
def run(source):
    acc, head, pc, l, stk = 0, 0, 0, len(source), []
    while pc < l:
        match source[pc]:
            # The language has only six instructions.
            case "&":
                # read a byte from its own source
                # and store it in the accumulator (0 if no more bytes).
                if head < len(source): acc, head = (ord(source[head]), head+1)
                else: acc = 0
                pc += 1
            case "*": print(chr(acc), end=""); pc += 1 # print the accumulator as a character
            case "(": stk.append(pc); pc += 1 # loop operation
            case ")": # end loop when the accumulator is zero
                if acc > 0: pc = stk[-1]
                else: stk.pop(); pc += 1
            case "!": # print literal string until next slash.
                pc += 1
                while ord(source[pc]) != 47: 
                    if ord(source[pc]) != 72: print(source[pc], end="")
                    # Use capital h to escape next character.
                    else: pc += 1; print(chr(ord(source[pc])-33), end="")
                    pc += 1
                pc += 1
            case _: raise ValueError(f"Invalid instruction at position {pc}: {source[pc]}")
run(source)
/'''
def run(source):
    acc, head, pc, l, stk = 0, 0, 0, len(source), []
    while pc < l:
        match source[pc]:
            # The language has only six instructions.
            case "&":
                # read a byte from its own source
                # and store it in the accumulator (0 if no more bytes).
                if head < len(source): acc, head = (ord(source[head]), head+1)
                else: acc = 0
                pc += 1
            case "*": print(chr(acc), end=""); pc += 1 # print the accumulator as a character
            case "(": stk.append(pc); pc += 1 # loop operation
            case ")": # end loop when the accumulator is zero
                if acc > 0: pc = stk[-1]
                else: stk.pop(); pc += 1
            case "!": # print literal string until next slash.
                pc += 1
                while ord(source[pc]) != 47: 
                    if ord(source[pc]) != 72: print(source[pc], end="")
                    # Use capital h to escape next character.
                    else: pc += 1; print(chr(ord(source[pc])-33), end="")
                    pc += 1
                pc += 1
            case _: raise ValueError(f"Invalid instruction at position {pc}: {source[pc]}")
run(source)
