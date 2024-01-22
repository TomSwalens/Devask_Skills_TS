Task name:
DNAC
Task preparation:
VM with linux OS.
Task implementation:

I asked GPT to help me full in the blanks of the code.


If we only want to output c3504.abc.inc or leaf1.abc.inc add the following to the code:


if device['type'] is not None:
        hostname = device['hostname']
        if hostname.startswith(('c3504.abc.inc', 'leaf1.abc.inc')):





Task troubleshooting:

c3504.abc.inc or leaf1.abc.inc Not on the virtual router. I reread the task an found out that we only need to generate a simular output. Task finished.


Task verification:
script.py found under DNAC for the code.

Documentation can be found under DNAC:
https://docs.google.com/document/d/1sJQKWfi7IL6FfIjJBT3c5zstpOfB3hE3WigJU2X5QX4/edit?usp=sharing