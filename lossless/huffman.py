import heapq
from collections import Counter

# Function to generate Huffman codes by traversing the tree
def generate_codes(tree, prefix="", code_map={}):
    if isinstance(tree, tuple):
        # Leaf node (character, frequency)
        char = tree[1]
        code_map[char] = prefix
    else:
        # Internal node, traverse left (0) and right (1)
        generate_codes(tree[0], prefix + "0", code_map)
        generate_codes(tree[1], prefix + "1", code_map)
    return code_map

# Function to build the Huffman tree from character frequencies
def build_huffman_tree(frequencies):
    heap = [[freq, char] for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Pop two smallest nodes
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Combine them and push the new node back into the heap
        heapq.heappush(heap, [left[0] + right[0], [left, right]])

    return heap[0]  # Root of the Huffman Tree

# Function to compress text using Huffman Coding
def huffman_compress(text):
    frequencies = Counter(text)  # Count frequencies of characters
    tree = build_huffman_tree(frequencies)  # Build Huffman tree
    huffman_codes = generate_codes(tree)  # Generate Huffman codes
    compressed_text = ''.join(huffman_codes[char] for char in text)  # Compress text

    return compressed_text, huffman_codes

# Function to decompress Huffman-encoded text
def huffman_decompress(compressed_text, huffman_codes):
    reversed_codes = {v: k for k, v in huffman_codes.items()}  # Reverse the Huffman code map
    decoded_text = ""
    buffer = ""
    
    for bit in compressed_text:
        buffer += bit
        if buffer in reversed_codes:
            decoded_text += reversed_codes[buffer]
            buffer = ""

    return decoded_text

# Example usage
if __name__ == "__main__":
    text = "abbcccdddd"
    
    # Compress the text
    compressed_text, huffman_codes = huffman_compress(text)
    print("Compressed text:", compressed_text)
    print("Huffman Codes:", huffman_codes)

    # Decompress the text
    decompressed_text = huffman_decompress(compressed_text, huffman_codes)
    print("Decompressed text:", decompressed_text)
