# Lossless

## 1) Huffman Simulation

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

![alt text](https://i.ibb.co/1v1Rhg2/Screen-Shot-2024-09-28-at-12-53-01-AM.png)

### Step 3: Huffman Codes

Traverse the tree to generate binary codes for each character:

| Character | Huffman Code |
|-----------|--------------|
| a         | 110          |
| b         | 111          |
| c         | 10           |
| d         | 0            |

### Step 4: Compress the Text

Using the Huffman codes, compress **"abbcccdddd"** into the following binary string:


### Step 5: Decompress the Text

Decompress the binary string `1101111111010100000` back into the original string:

================================================================================================================================================================

## 2) Run-Length Encoding (RLE) Simulation

Run-Length Encoding (RLE) is a simple lossless compression algorithm that encodes consecutive repeated characters by storing the character followed by the number of repetitions. This method is particularly useful when the data contains many repeated characters.

### Input String: `"abbcccdddd"`

Let's simulate the process of encoding and decoding this string using RLE.

---

## Step 1: **Encoding Process**

**Input:** `"abbcccdddd"`

The algorithm goes through each character and counts the consecutive occurrences, then stores the character followed by the count.

| Character | Count | Encoded Pair |
|-----------|-------|--------------|
| a         | 1     | a1           |
| b         | 2     | b2           |
| c         | 3     | c3           |
| d         | 4     | d4           |

---

**Encoded Output:** `"a1b2c3d4"`

The input string `"abbcccdddd"` is compressed into the encoded string `"a1b2c3d4"`.

---

## Step 2: **Decoding Process**

**Encoded Input:** `"a1b2c3d4"`

The decoding process reads the encoded pairs and reconstructs the original string by repeating each character according to the count provided.

| Encoded Pair | Decoded Output |
|--------------|----------------|
| a1           | a              |
| b2           | bb             |
| c3           | ccc            |
| d4           | dddd           |

---

**Decoded Output:** `"abbcccdddd"`

The encoded string `"a1b2c3d4"` is successfully decoded back into the original string `"abbcccdddd"`.

---

## Summary

- **Original String:** `"abbcccdddd"`
- **Encoded String:** `"a1b2c3d4"`
- **Decoded String:** `"abbcccdddd"`

The RLE compression reduces the size of the string, especially when there are many consecutive repeating characters.

