import pyvisa


rm = pyvisa.ResourceManager() 

print(rm)
print(rm.list_resources())



inst = rm.open_resource('ASRL10::INSTR')
insta = rm.open_resource("GPIB::28::INSTR")

print("razorbill:")
print(inst.query("*IDN?"))
print("cap bridge:")
print(insta.query("*IDN?"))

