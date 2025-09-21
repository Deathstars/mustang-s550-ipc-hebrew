def extract_ttf_from_bin(bin_path, out_path):
    with open(bin_path, 'rb') as f:
        data = f.read()

    # Search for TTF header (00 01 00 00)
    ttf_magic = b'\x00\x01\x00\x00\x00\x12\x01'
    ttf_offset = data.find(ttf_magic)
    if ttf_offset == -1:
        print("TTF header not found")
        return

    # Read numTables (2 bytes after magic, big endian)
    num_tables = int.from_bytes(data[ttf_offset+4:ttf_offset+6], 'big')

    # Table Directory starts at offset+12, each entry is 16 bytes
    td_start = ttf_offset + 12
    max_end = 0
    for i in range(num_tables):
        entry_offset = td_start + 16*i
        # Each table: 4 byte tag, 4 byte checksum, 4 byte offset, 4 byte length
        table_offset = int.from_bytes(data[entry_offset+8:entry_offset+12], 'big')
        table_length = int.from_bytes(data[entry_offset+12:entry_offset+16], 'big')
        end = table_offset + table_length
        if end > max_end:
            max_end = end

    # Extract full TTF
    ttf_data = data[ttf_offset : ttf_offset + max_end]
    with open(out_path, 'wb') as out:
        out.write(ttf_data)
    print(f"Extracted TTF at {ttf_offset:08X}, size {len(ttf_data)} bytes to {out_path}")

# Usage:
extract_ttf_from_bin(r"C:\Users\yaari\Downloads\firm\bitmaps.bin", r"C:\Users\yaari\Downloads\firm\output.ttf")
