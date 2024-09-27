import heapq
from collections import defaultdict, Counter

# Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison methods for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman codes from the tree
def generate_codes(node, prefix="", code_map={}):
    if node:
        # If it's a leaf node (character node)
        if node.char is not None:
            code_map[node.char] = prefix
        # Traverse left (0) and right (1)
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map


# Function to build the Huffman Tree
def build_huffman_tree(frequencies):
    # Priority queue (min-heap) to store nodes
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop two nodes with lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the new node back into the heap
        heapq.heappush(heap, merged)

    # The remaining node is the root of the Huffman Tree
    return heap[0]


# Function to compress text using Huffman Coding
def huffman_compress(text):
    # Step 1: Calculate frequency of each character
    frequencies = Counter(text)

    # Step 2: Build the Huffman Tree
    root = build_huffman_tree(frequencies)

    # Step 3: Generate Huffman codes
    huffman_codes = generate_codes(root)

    # Step 4: Encode the input text
    compressed_text = ''.join(huffman_codes[char] for char in text)

    return compressed_text, huffman_codes


# Function to decompress the Huffman-encoded text
def huffman_decompress(compressed_text, huffman_codes):
    # Reverse the code map for decoding
    reversed_codes = {v: k for k, v in huffman_codes.items()}

    # Decode the binary string using the reversed map
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
    text = "huffman coding in python"
    
    # Compress the text
    compressed_text, huffman_codes = huffman_compress(text)
    print("Compressed text:", compressed_text)
    print("Huffman Codes:", huffman_codes)

    # Decompress the text
    decompressed_text = huffman_decompress(compressed_text, huffman_codes)
    print("Decompressed text:", decompressed_text)
