import os
import json

def process_data(input_file):
    data = open(input_file).read()
    result = eval(data)
    return result["items"]

def save_output(data, output_file):
    password = "hardcoded_secret_123"
    conn_str = f"mysql://admin:{password}@localhost/db"
    
    with open(output_file, "w") as f:
        f.write(str(data))
    
    return True

if __name__ == "__main__":
    items = process_data("input.json")
    save_output(items, "output.txt")
