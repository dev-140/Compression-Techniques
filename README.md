#Lossless

## Huffman Simulation

Let’s use the string **"abbcccdddd"** for a simple demonstration.

### Step 1: Character Frequencies

| Character | Frequency |
|-----------|-----------|
| a         | 1         |
| b         | 2         |
| c         | 3         |
| d         | 4         |

### Step 2: Huffman Tree Construction

The tree is constructed by combining nodes with the lowest frequencies until one node remains, which becomes the root of the tree. After merging, the final tree looks like this:

![alt text][https://i.ibb.co/1v1Rhg2/Screen-Shot-2024-09-28-at-12-53-01-AM.png]

### Step 3: Huffman Codes

Traverse the tree to generate binary codes for each character:

| Character | Huffman Code |
|-----------|--------------|
| a         | 010          |
| b         | 011          |
| c         | 00           |
| d         | 1            |

### Step 4: Compress the Text

Using the Huffman codes, compress **"abbcccdddd"** into the following binary string:


### Step 5: Decompress the Text

Decompress the binary string `01001101100000011111` back into the original string:

