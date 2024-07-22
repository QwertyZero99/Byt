#
# # This function parses a file and saves them in a dictionary.
# def parse_file(file_path):
#     commands = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Strip the line of leading/trailing whitespace
#             line = line.strip()
#             if line:
#                 # Split once on the first space to separate the command from the rest
#                 space_index = line.find(' ')
#                 if space_index == -1:
#                     command = line
#                     parameters = []
#                 else:
#                     command = line[:space_index]
#                     parameters_part = line[space_index + 1:]
#                     # Split the parameters part by commas, ensuring to strip any extra whitespace
#                     parameters = [param.strip() for param in parameters_part.split(',')]
#                 commands.append({command: parameters})
#     #print(commands)
#     return commands
# 
# # Example usage
# file = parse_file('test1.byt')
# def listCommands(parsedFile):
#     commands = []
#     for command in parsedFile:
#         key = command.keys()
#         commands.append(key)
#     return commands
# 
# def listParameters(parsedFile):
#     parameters = []
#     for line in parsedFile:
#         key = line.keys()
#         parameter = line.values()
#         parameters.append(parameter)
#     return parameters
# 
# #fileParameters = listParameters(file)
# #fileCommmands = listCommands(file)
# 
# #print('commands: ', fileCommmands)
# #print('parameters: ', fileParameters)