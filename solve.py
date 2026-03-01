import subprocess

# Bytes da chave extraidos do Ghidra (local_58)
# Conversao aplicada: valores negativos -> n + 256
key = bytes([
    0xe1,  # local_58[0]  = -0x1f
    0xa7,  # local_58[1]  = -0x59
    0x1e,  # local_58[2]  = '\x1e'
    0xf8,  # local_58[3]  = -8
    0x75,  # local_58[4]  = 'u'
    0x23,  # local_58[5]  = '#'
    0x7b,  # local_58[6]  = '{'
    0x61,  # local_58[7]  = 'a'
    0xb9,  # local_58[8]  = -0x47
    0x9d,  # local_58[9]  = -99
    0xfc,  # local_58[10] = -4
    0x5a,  # local_58[11] = 'Z'
    0x5b,  # local_58[12] = '['
    0xdf,  # local_58[13] = -0x21
    0x69,  # local_58[14] = 'i'
    0xd2,  # local_58[15] = 0xd2
    0xfe,  # local_58[16] = -2
    0x1b,  # local_58[17] = '\x1b'
    0xed,  # local_58[18] = -0x13
    0xf4,  # local_58[19] = -0xc
    0xed,  # local_58[20] = -0x13
    0x67,  # local_58[21] = 'g'
    0xf4,  # local_58[22] = -0xc
])

print(f"[*] Chave: {key.hex()}")
print(f"[*] Tamanho: {len(key)} bytes")
print(f"[*] Bytes imprimiveis: {''.join(chr(b) if 32 <= b < 127 else '.' for b in key)}")

# fgets le ate newline, entao adicionamos \n ao payload
payload = key + b'\n'

# Envia para o binario via stdin
result = subprocess.run(
    ['./perplexed'],
    input=payload,
    capture_output=True
)

print(f"\n[*] Output: {result.stdout.decode().strip()}")
