
from ast import literal_eval as Eval
from os import system as Runer
from opcode import opname
import re
import importlib.util
from marshal import dumps
import sys

Runer("cls || clear")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g,b = '\033[00;36m', '\033[90m','\033[38;5;130m','[2;36m'
tr = f'{rd}[{gn}+{rd}]{gn} '
fls = f'{rd}[{lrd}-{rd}]{lrd} '

class Py2Byte:
    VaRib = {
        "co_consts": ["LOAD_CONST"],
        "co_names": ["STORE_NAME", "DELETE_NAME", "STORE_ATTR", "DELETE_ATTR", "LOAD_NAME", "LOAD_ATTR", "IMPORT_NAME", "IMPORT_FROM", "LOAD_GLOBAL", "LOAD_METHOD"],
        "co_varnames": ["STORE_FAST", "DELETE_FAST", "LOAD_FAST"],
        "co_cellvars": ["STORE_DEREF", "LOAD_CLOSURE"],
        "co_freevars": ["LOAD_DEREF"],
    }

    def __init__(self, input_file):
        self.input_file = input_file
        self.sections = {None: []}
        self.current_section = None
    Prefix = "Disassembly of "
    def Parser(self, lines):
        codes = []
        for line in lines:
            if len(line) == 0:
                continue
            if line.startswith(self.Prefix):
                break
            parts = list(filter(lambda x: x not in ["", ">>"], line[6:].split(" ")))
            _offset = int(parts[0])
            op_name = parts[1]
            arg = int(parts[2]) if len(parts) > 2 else None
            repr = ' '.join(parts[3:])[1:-1] if len(parts) > 3 else None
            codes.append((op_name, arg, repr))
        return codes

    def GetCode(self, name):
        name = re.search(r"<code object (\S+) at", name).group(1)
        if name == "<lambda>":
            return (lambda: None).__code__
        elif name == "<listcomp>":
            return (lambda: [None for _ in []]).__code__.co_consts[1]
        else:
            return (lambda: None).__code__.replace(co_name=name)

    def GetConst(self, codes):
        consts = {}
        for code in codes:
            if code[0] == "LOAD_CONST":
                value = code[2]
                if value in self.sections:
                    if isinstance(self.sections[value], list):
                        base = self.GetCode(value)
                        self.sections[value] = self.reassemble(self.sections[value], code_base=base)
                    value = self.sections[value]
                else:
                    value = Eval(value)
                consts[code[1]] = value
        length = max(consts.keys(), default=-1) + 1
        return tuple(consts.get(i) for i in range(length))

    def GetCoAny(self, codes, co_attr):
        vars = {}
        for code in codes:
            if code[0] in self.VaRib[co_attr]:
                vars[code[1]] = code[2]
        length = max(vars.keys(), default=-1) + 1
        return tuple(vars.get(i) for i in range(length))

    def Getargcount(self, codes):
        stored_first = set()
        load_first = set()
        for code in codes:
            if code[0] == "STORE_FAST" and code[1] not in load_first:
                stored_first.add(code[1])
            elif code[0] == "LOAD_FAST" and code[1] not in stored_first:
                load_first.add(code[1])
        return len(load_first)

    def ToByte(self, codes):
        bytecode = b""
        for code in codes:
            op_index = opname.index(code[0])
            arg = code[1] if code[1] is not None else 0
            bytecode += bytes([op_index, arg & 0xff])
        return bytecode

    def reassemble(self, lines, code_base=(lambda: None).__code__):
        codes = self.Parser(lines)
        code = code_base.replace(
            co_consts=self.GetConst(codes),
            co_names=self.GetCoAny(codes, "co_names"),
            co_varnames=self.GetCoAny(codes, "co_varnames"),
            co_cellvars=self.GetCoAny(codes, "co_cellvars"),
            co_freevars=self.GetCoAny(codes, "co_freevars"),
            co_argcount=self.Getargcount(codes),
            co_code=self.ToByte(codes),
        )
        return code

    def full_reassemble(self):
        with open(self.input_file) as f:
            disassembly = f.read()
        for line in disassembly.splitlines():
            if line.startswith(self.Prefix):
                self.current_section = line[len(self.Prefix):-1]
                self.sections[self.current_section] = []
            else:
                self.sections[self.current_section].append(line)
        return self.reassemble(self.sections.pop(None))

    @staticmethod
    def write_code_object(code, filename):
        with open(filename, "wb") as f:
            f.write(importlib.util.MAGIC_NUMBER)
            f.write(b"\x00" * 8)
            if sys.version_info[1] >= 7:
                f.write(b"\x00" * 4)
            f.write(dumps(code))
        print(f"{tr}Code object written to {yw}{filename!r}")

def main():
    print (f"""{b}
                                                                                                                                                                                
  ▄▄▄▄▄▄                                                ▄▄             
 █▀██▀▀▀█▄                                         █▄    ██            
   ██▄▄▄█▀                                ▄        ██    ██       ▄    
   ██▀▀█▄   ▄█▀█▄ ▄▀▀█▄ ▄██▀█ ▄██▀█ ▄█▀█▄ ███▄███▄ ████▄ ██ ▄█▀█▄ ████▄
 ▄ ██  ██   ██▄█▀ ▄█▀██ ▀███▄ ▀███▄ ██▄█▀ ██ ██ ██ ██ ██ ██ ██▄█▀ ██   
 ▀██▀  ▀██▀▄▀█▄▄▄▄▀█▄███▄▄██▀█▄▄██▀▄▀█▄▄▄▄██ ██ ▀█▄████▀▄██▄▀█▄▄▄▄█▀   
                                                                       
                         
                    {gn}Tg: @MrEsfelurm

           """)
    input_file = input(f"{tr}Enter input file name:{cn} ")
    output_file = input(f"{tr}Enter output file name {rd}({yw}default: output.pyc{rd}): {cn}") or "output.pyc"
    reassembler = Py2Byte(input_file)
    main_code = reassembler.full_reassemble()
    reassembler.write_code_object(main_code, output_file)
    print (f"\n\n{lgn}Codes were converted into ByteCode/ObjectCode!")
    pycdc = input(f"{tr}Do you have pycdc? [yes/no]:{cn} ").upper()
    if pycdc == "YES":
        import subprocess
        result = subprocess.run(f"pycdc {output_file}", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            with open(f'Decrypted.py', 'w') as f:
                f.write(f"#Telegram: @MrEsfelurm\n\n{result.stdout}")
            print (f"{tr}The code is successfully returned to the initial state! {yw}Decrypted.py")
        else:
            print(f"{fls}Error: {result.stderr}")

if __name__ == "__main__":
    main()
