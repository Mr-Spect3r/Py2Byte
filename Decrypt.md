# My Source

```
import requests

r = requests.post("https://google.com")

print (r.status_code)
```
Now it's encrypted! <a href="https://github.com/Mr-Spect3r/Py2Bytecode/blob/main/Encrypter%20Marshal/Marshal.py"> Click For Encrypt with marshal

## How To Decrypt Marshal?

# Step 1

<b>In the first step, convert the source to disassembly or bytecode
How?
Example</b>

- Encrypted source:

```
import marshal
exec(marshal.loads(b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s \x00\x00\x00d\x00d\x01l\x00Z\x00e\x00\xa0\x01d\x02\xa1\x01Z\x02e\x03e\x02j\x04\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz\x12https://google.com)\x05Z\x08requestsZ\x04post\xda\x01r\xda\x05printZ\x0bstatus_code\xa9\x00r\x03\x00\x00\x00r\x03\x00\x00\x00\xda\x00\xda\x08<module>\x01\x00\x00\x00s\x06\x00\x00\x00\x08\x00\n\x02\x0e\x02'))
```

- Convert to:

```
import marshal,dis
code = marshal.loads(b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s \x00\x00\x00d\x00d\x01l\x00Z\x00e\x00\xa0\x01d\x02\xa1\x01Z\x02e\x03e\x02j\x04\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nz\x12https://google.com)\x05Z\x08requestsZ\x04post\xda\x01r\xda\x05printZ\x0bstatus_code\xa9\x00r\x03\x00\x00\x00r\x03\x00\x00\x00\xda\x00\xda\x08<module>\x01\x00\x00\x00s\x06\x00\x00\x00\x08\x00\n\x02\x0e\x02')

with open('output.txt','w',encoding='UTF-8') as f:
    dis.dis(code,file=f)
```

- Result

```
  1           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (None)
              4 IMPORT_NAME              0 (requests)
              6 STORE_NAME               0 (requests)

  3           8 LOAD_NAME                0 (requests)
             10 LOAD_METHOD              1 (post)
             12 LOAD_CONST               2 ('https://google.com')
             14 CALL_METHOD              1
             16 STORE_NAME               2 (r)

  5          18 LOAD_NAME                3 (print)
             20 LOAD_NAME                2 (r)
             22 LOAD_ATTR                4 (status_code)
             24 CALL_FUNCTION            1
             26 POP_TOP
             28 LOAD_CONST               1 (None)
             30 RETURN_VALUE

```

# Step 2

<b>Run the Py2Byte.py file</b>

- Run

```
python Bytecode2Py.py
```

- Convert the disassembly to a pyc file

- Result

```
[+] Enter input file name: output.txt
[+] Enter output file name (default: output.pyc): out.pyc
[+] Code object written to 'out.pyc'


Codes were converted into ByteCode/ObjectCode!
[+] Do you have pycdc? [yes/no]: yes
[+] The code is successfully returned to the initial state! Decrypted.py
```
# End

<b>Now it's time to convert pyc to py. For this, you can use pycdc, uncompyle6 and https://pylingual.io</b>

## Pycdc

- how to convert pyc to py with pycdc

```
pycdc out.pyc
```

- Result

```
#Telegram: @MrEsfelurm

# Source Generated with Decompyle++
# File: out.pyc (Python 3.10)

import requests
r = requests.post('https://google.com')
print(r.status_code)
```

End!

Marshal's decoding videos: 

https://t.me/MrEsfelurm/10628
https://t.me/MrEsfelurm/10629
https://t.me/MrEsfelurm/10631


My channel in Telegram: @MrEsfelurm
