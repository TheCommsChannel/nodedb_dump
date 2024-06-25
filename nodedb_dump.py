#!/usr/bin/env python3

import meshtastic
import meshtastic.serial_interface

def dump_all_node_info():
    # Connect to the device via serial connection
    interface = meshtastic.serial_interface.SerialInterface()

    # Access the node database
    nodes = interface.nodes.values()

    # Print all available information for each node
    for node in nodes:
        print("Node Info:")
        for key, value in node.items():
            print(f"{key}: {value}")
        print("\n" + "-"*40 + "\n")

    # Close the connection
    interface.close()

# Call the function to dump all node info
dump_all_node_info()
