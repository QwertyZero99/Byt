class Line:
    def __init__(self, command, parameters):
        self.command = command
        self.parameters = parameters


# class Command:
#     def __init__(self, name, start, end):
#         self.name = name
#         self.code = self._parse_section(start, end)
# 
#     def _parse_section(self, start, end):
#         return parse_file(file_path)


def run_file(file):
    variables = {}
    print('-Running file-\n--------------\n')
    for line in file:
        if line.command == 'OUT':
            if len(line.parameters) == 1:
                print(line.parameters[0])
            else:
                print(f"Incorrect Parameters. {line.command} takes 1 parameters. ERR 113")
                break
        elif line.command == 'IN':
            if len(line.parameters) == 1:
                input(line.parameters[0])
            else:
                print(f"Incorrect Parameters. {line.command} takes 1 parameters. ERR 113")
                break
        elif line.command == 'NULL':
            print("NULL command. ERR 111")
            break
        else:
            print(f'Unknown command: {line.command}. ERR 112')
            break


def parse_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line_content in file:
            line_content = line_content.strip()
            if not line_content:
                continue
                
            space_index = line_content.find(' ')
            if space_index == -1:
                command = line_content
                parameters = []
            else:
                command = line_content[:space_index]
                parameters_part = line_content[space_index + 1:]
                parameters = [param.strip() for param in parameters_part.split(',')]
            lines.append(Line(command, parameters))
    return lines


parsed_file = parse_file('test1.byt')
for idx, obj in enumerate(parsed_file, start=1):
    print(f"Line #{idx} COMMAND: {obj.command}, PARAMETERS: {obj.parameters}")
        
    
run_file(parsed_file)
