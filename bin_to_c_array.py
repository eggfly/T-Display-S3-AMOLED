def bin_to_c_array(input_file, output_file, array_name):
    with open(input_file, 'rb') as f:
        data = f.read()

    with open(output_file, 'w') as f:
        f.write("const unsigned char {}[] = {{\n".format(array_name))
        for i in range(0, len(data), 16):
            f.write("    ")
            for j in range(16):
                if i + j < len(data):
                    f.write("0x{:02X}, ".format(data[i + j]))
                else:
                    f.write("0x00, ")
            f.write("\n")
        f.write("};\n")

if __name__ == "__main__":
    input_file = "LodeRunner.bin"
    output_file = "output.c"
    array_name = "my_array"

    bin_to_c_array(input_file, output_file, array_name)
