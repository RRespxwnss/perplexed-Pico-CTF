# Perplexed Pico-CTF

# Explotation
The binary code acts as a simple password checker. It reads a line from stdin, passes it to a function called check, and prints "Correct!!" :D or Wrong :( based on the return value. The relevant behavior is entirely within check, and the correct password never appears as a readable string anywhere in the binary, meaning that the strings command alone does not solve the challenge.

The first thing check does is call strlen on the input and compare it to 0x1b, which is 27 in decimal. If the length is different from 27, the function immediately returns the error value. This is a fixed-size filter and eliminates any brute-force attempts that don't take length into account.

The next block loads 23 bytes directly onto the stack via individual assignments to a local array called local_58. These are the values ​​that Ghidra displays as negative numbers like -0x1f and -0x59, alongside printable character literals like 'u' and 'a'. The negative representation is an artifact of Ghidra when treating the values ​​as signed char. To convert, simply apply n + 256 to any negative n value: -0x1f becomes 0xe1, -0x59 becomes 0xa7, and so on. To facilitate this conversion, a byte converter was created that receives the values ​​directly from the Ghidra output and returns the correct bytes. This converter is available in the repository along with this README.

The comparison itself is done bit by bit, not byte by byte. Two nested loops traverse the key bytes and the input bytes simultaneously, extracting individual bits from each using mask operations of the type 1 << (7 - bit_index). For each position, the code checks if the corresponding bit of the key and the bit of the input have the same value. If any bit differs, the function returns the error value immediately. If all the bits in all positions match, the function returns zero and the program prints the success message.

Since the 23 bytes of the key are mostly non-printable in ASCII, the password cannot be typed directly into the terminal. For this, a Python script was created that converts the extracted bytes into a payload. This script is also available in the repository.

# GHidra Analysis

<img width="600" alt="image" src="https://github.com/user-attachments/assets/510f7b98-9957-41b5-95aa-5b4947acaf5c" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/28939fa7-e480-4360-910c-9cbd920d80a4" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/f795d3c2-9e7d-47f0-99b5-d61f9a132c5e" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/f505c2a8-15e9-4653-a21e-eee38605de3f" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/02fe591e-408a-4c82-9420-0a377d99b81e" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/539dbbdf-2093-4958-ab2b-2f8852ff54f1" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/683ae9b4-178b-4115-ad3f-efd967cdb7d6" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/5d5f1453-974b-4e93-aec0-d9c65033bacf" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/8553baa8-f231-4b23-9916-440440492c24" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/5b8927ca-83ad-49be-af27-717ecdc4f4dc" />
<img width="600" alt="image" src="https://github.com/user-attachments/assets/1d856762-c0c1-4f1a-b5b9-32e925ccb3e5" />
