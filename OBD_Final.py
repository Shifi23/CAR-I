import obd

connection = obd.OBD()  # auto-connects to USB or RF port

cmd = obd.commands.ELM_VOLTAGE  # select an OBD command (sensor)

response = connection.query(cmd)  # send the command, and parse the response

print(response.value)  # returns unit-bearing values thanks to Pint
# print(response.value.to("mph")) # user-friendly unit conversions
# 00:1D:A5:0A:85:FB
# connection = obd.Async(fast=True, baudrate=500000)


# def get_coolant(c):
#     global coolant
#     if not c.is_null():
#         coolant = int(c.value.magnitude)


# def get_voltage(v):
#     global voltage
#     if not v.is_null():
#         voltage = float(v.value.magnitude)


# def get_load(l):
#     global load
#     if not l.is_null():
#         load = int(l.value.magnitude)


# def get_throttle(t):
#     global throttle
#     if not t.is_null():
#         throttle = int(t.value.magnitude)


# connection.watch(obd.commands.COOLANT_TEMP, callback=get_coolant, force=False)
# connection.watch(obd.commands.ELM_VOLTAGE, callback=get_voltage, force=False)
# connection.watch(obd.commands.ENGINE_LOAD, callback=get_load, force=False)
# connection.watch(obd.commands.THROTTLE_POS, callback=get_throttle, force=False)

# connection.start()

# print(coolant, voltage, load, throttle)
