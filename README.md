# Python (Opcode) to Bytecode

<b>Convert disassembled Python opcode back into a valid Python bytecode (.pyc) file.</b>


<img src="https://github.com/user-attachments/assets/663b49ed-987c-4148-93f7-f6ecf11e4459">


# What is bytecode?

<b>Bytecode is a low-level representation of the instructions in a programming language.
In the case of Python, the CPython interpreter uses a particular kind of bytecode known as CPython bytecode. It functions as a collection of guidelines that specify the activities the interpreter should do.



# dis module


The dis module, which is a component of the standard Python library, aids in the analysis of CPython bytecode. In order for you to comprehend what each instruction accomplishes, the dis module in Python is designed to disassemble or break down the bytecode into its individual instructions.
Disassembling bytecode is done in order to gain a better understanding of how the interpreter runs Python code. It can be helpful for code analysis and debugging, figuring out performance snags, or discovering how specific constructs are converted into bytecode</b>


## Example

- Python

```
a = 1
b = 2
c = a + b
print(c)
def func(e, f, g):
    h = e + f + g

func(a, b, c)
```

- Opcode

  ```
    1           0 LOAD_CONST               0 (1)
              2 STORE_NAME               0 (a)

  2           4 LOAD_CONST               1 (2)
              6 STORE_NAME               1 (b)

  3           8 LOAD_NAME                0 (a)
             10 LOAD_NAME                1 (b)
             12 BINARY_ADD
             14 STORE_NAME               2 (c)

  4          16 LOAD_NAME                3 (print)
             18 LOAD_NAME                2 (c)
             20 CALL_FUNCTION            1
             22 POP_TOP

  5          24 LOAD_CONST               2 (<code object func at 0x7fb9aebb59c0, file "btins3.py", line 5>)
             26 LOAD_CONST               3 ('func')
             28 MAKE_FUNCTION            0
             30 STORE_NAME               4 (func)

  8          32 LOAD_NAME                4 (func)
             34 LOAD_NAME                0 (a)
             36 LOAD_NAME                1 (b)
             38 LOAD_NAME                2 (c)
             40 CALL_FUNCTION            3
             42 POP_TOP
             44 LOAD_CONST               4 (None)
             46 RETURN_VALUE```

### How to Convert Python to Opcode/disassemble

- install dis

`pip install dis`

- How To Convert?

`python3 -m dis name.py`

# Decrypt Marshal

How To Decrypt? <a href="https://github.com/Mr-Spect3r/Py2Bytecode/blob/main/Decrypt.md">Click Me

<a href="https://github.com/Mr-Spect3r/Py2Bytecode/tree/main/pycdc%20Android"> Pycdc For Android

<a href="https://github.com/Mr-Spect3r/Py2Bytecode/tree/main/pycdc%20Windows"> Pycdc For Windows

