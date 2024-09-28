import heapq
from collections import Counter

class Node:
    def __init__(self, symbol=None, frequency=None):
        """Initialize a new node for the Huffman tree."""
        self.symbol = symbol
        self.frequency = frequency
        self.left = None  # Left child node
        self.right = None  # Right child node

    def __lt__(self, other):
        """Define less-than comparison for priority queue."""
        return self.frequency < other.frequency

def build_huffman_tree(chars, freq):
    """Build the Huffman tree."""
    priority_queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(priority_queue)  # Create a min-heap.

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)  # Smallest frequency node.
        right_child = heapq.heappop(priority_queue)  # Next smallest frequency.
        # Create and merge nodes.
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)  # Push merged node back.

    return priority_queue[0]  # Root of the Huffman tree.

def generate_huffman_codes(node, code="", huffman_codes={}):
    """Generate Huffman codes by traversing the tree."""
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code  # Store code for leaf node.
        generate_huffman_codes(node.left, code + "0", huffman_codes)  # Traverse left.
        generate_huffman_codes(node.right, code + "1", huffman_codes)  # Traverse right.
    return huffman_codes

def decode_huffman(root, encoded_string):
    """Decode the encoded string using the Huffman tree."""
    decoded_string = ""
    current_node = root  # Start from the root.

    for bit in encoded_string:
        current_node = current_node.left if bit == '0' else current_node.right  # Traverse tree.
        if current_node.symbol is not None:
            decoded_string += current_node.symbol  # Append symbol to result.
            current_node = root  # Reset to root for the next symbol.

    return decoded_string

# Input string.
input_string = "abbcccdddd"

# Calculate frequencies of each character.
freq_counter = Counter(input_string)
chars = list(freq_counter.keys())
freq = list(freq_counter.values())

# Build the Huffman tree.
root = build_huffman_tree(chars, freq)

# Generate Huffman codes.
huffman_codes = generate_huffman_codes(root)

# Print Huffman codes.
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")

# Generate encoded string based on frequencies.
encoded_string = ''.join(huffman_codes[char] * freq_counter[char] for char in chars)
print("Encoded string:", encoded_string)

# Decode the string.
decoded_string = decode_huffman(root, encoded_string)
print("Decoded string:", decoded_string)
