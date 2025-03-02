import os
import socket
import collections
import re

# Define paths
input_files = ["/home/data/IF-1.txt", "/home/data/AlwaysRememberUsThisWay-1.txt"]
output_file = "/home/data/output/result.txt"

# Function to count words
def count_words(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return collections.Counter(words)

# Read and process files
word_counts = {}
grand_total = 0
top_words = {}

for file in input_files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    # Handle contractions in 'AlwaysRememberUsThisWay-1.txt'
    if "AlwaysRememberUsThisWay" in file:
        text = text.replace("'", " ")  # Split contractions

    counter = count_words(text)
    word_counts[file] = sum(counter.values())
    grand_total += word_counts[file]
    top_words[file] = counter.most_common(3)

# Get container IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results
with open(output_file, "w") as f:
    f.write(f"Word Count per File:\n")
    for file, count in word_counts.items():
        f.write(f"{file}: {count} words\n")
    
    f.write(f"\nGrand Total: {grand_total} words\n")

    f.write("\nTop 3 Words in IF-1.txt:\n")
    for word, count in top_words[input_files[0]]:
        f.write(f"{word}: {count}\n")

    f.write("\nTop 3 Words in AlwaysRememberUsThisWay-1.txt (after handling contractions):\n")
    for word, count in top_words[input_files[1]]:
        f.write(f"{word}: {count}\n")

    f.write(f"\nContainer IP Address: {ip_address}\n")

# Print results to console
with open(output_file, "r") as f:
    print(f.read())
