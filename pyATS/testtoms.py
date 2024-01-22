from genie.testbed import load

# Load the testbed file
testbed = load('testbed.yaml')

# Loop through all devices in the testbed
for device_name, device in testbed.devices.items():
    print(f"Device: {device_name}")
    print(f"Hostname: {device_name}")
    print(f"IP Address: {device.connections['a'].ip}")

    # Connect to the device
    device.connect()

    # Parse 'show version' output to get model and serial number
    output = device.parse('show version')
    model = output.get('platform', {}).get('hardware', {}).get('model', 'N/A')
    serial_number = output.get('platform', {}).get('hardware', {}).get('serial_number', 'N/A')

    print(f"Model: {model}")
    print(f"Serial Number: {serial_number}\n")

    # Disconnect from the device
    device.disconnect()
