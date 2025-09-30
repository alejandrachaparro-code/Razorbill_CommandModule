import pyvisa


rm = pyvisa.ResourceManager() 

print(rm)
print(rm.list_resources())



inst = rm.open_resource('ASRL8::INSTR')
insta = rm.open_resource("GPIB0::28::INSTR")

print("razorbill:")
print(inst.query("*IDN?"))
print("cap bridge:")
print(insta.query("*IDN?"))



