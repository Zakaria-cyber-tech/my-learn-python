variables = {}
functions = {}
return_value = None

# --------------------
# Evaluate expressions
# --------------------
def eval_expr(expr):
    for var in variables:
        expr = expr.replace(var, str(variables[var]))
    return eval(expr)

# --------------------
# Run block
# --------------------
def run_block(lines, start=0, indent=0):
    global return_value
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        current_indent = len(line) - len(stripped)

        # skip empty lines
        if not stripped:
            i += 1
            continue

        # khzen (variable)
        if stripped.startswith("khzen "):
            left, right = stripped.replace("khzen ", "", 1).split("=", 1)
            variables[left.strip()] = eval_expr(right.strip())

        # itba3 (print)
        elif stripped.startswith("itba3"):
            inside = stripped[len("itba3"):].strip()
            if inside.startswith("(") and inside.endswith(")"):
                inside = inside[1:-1]
            print(eval_expr(inside))

        # wzifaa (function)
        elif stripped.startswith("wzifaa "):
            header = stripped[len("wzifaa "):]
            name, params = header.split("(", 1)
            name = name.strip()
            params = params.rstrip(")").split(",") if params.rstrip(")") else []
            params = [p.strip() for p in params]

            # find function body by indentation
            body = []
            j = i + 1
            while j < len(lines):
                l = lines[j]
                if len(l) - len(l.lstrip(" ")) <= current_indent:
                    break
                body.append(l[current_indent+4:] if len(l) > current_indent+4 else "")
                j += 1
            functions[name] = (params, body)
            i = j - 1

        # if / else
        elif stripped.startswith("if "):
            cond = stripped[3:].rstrip(":")
            true_block = []
            j = i + 1
            while j < len(lines):
                l = lines[j]
                l_strip = l.strip()
                l_indent = len(l) - len(l_strip)
                if l_indent <= current_indent:
                    break
                true_block.append(l[current_indent+4:])
                j += 1
            executed = False
            if eval_expr(cond):
                run_block(true_block)
                executed = True

            # check else
            if j < len(lines) and lines[j].strip().startswith("else:") and not executed:
                else_block = []
                k = j + 1
                while k < len(lines):
                    l = lines[k]
                    l_strip = l.strip()
                    l_indent = len(l) - len(l_strip)
                    if l_indent <= current_indent:
                        break
                    else_block.append(l[current_indent+4:])
                    k += 1
                run_block(else_block)
                j = k - 1
            i = j - 1

        # while
        elif stripped.startswith("while "):
            cond = stripped[6:].rstrip(":")
            loop_block = []
            j = i + 1
            while j < len(lines):
                l = lines[j]
                l_strip = l.strip()
                l_indent = len(l) - len(l_strip)
                if l_indent <= current_indent:
                    break
                loop_block.append(l[current_indent+4:])
                j += 1
            while eval_expr(cond):
                run_block(loop_block)
            i = j - 1
        # for loop بحال Python
        elif stripped.startswith("for "):
            header = stripped[4:].rstrip(":")  # مثلا i in range(5)
            var, _, iterable = header.partition(" in ")
            loop_block = []
            j = i + 1
            while j < len(lines):
                l = lines[j]
                l_strip = l.strip()
                l_indent = len(l) - len(l_strip)
                if l_indent <= current_indent:
                    break
                loop_block.append(l[current_indent+4:])
                j += 1

            iterable_val = eval_expr(iterable.strip())
            for value in iterable_val:
                variables[var.strip()] = value
                run_block(loop_block)
            i = j - 1


        # function call
        elif "(" in stripped and stripped.endswith(")"):
            name, args = stripped.split("(", 1)
            name = name.strip()
            args = args.rstrip(")")
            args_list = [eval_expr(a.strip()) for a in args.split(",")] if args else []

            if name in functions:
                params, body = functions[name]
                backup = variables.copy()
                for p, v in zip(params, args_list):
                    variables[p] = v
                run_block(body)
                variables = backup
                if return_value is not None:
                    variables["_"] = return_value
                    return_value = None

        # rj3 handled inside functions
        elif stripped.startswith("rj3 "):
            return_value = eval_expr(stripped[4:].strip())
            return

        # assignment x = ...
        elif "=" in stripped:
            left, right = stripped.split("=", 1)
            variables[left.strip()] = eval_expr(right.strip())

        i += 1

# --------------------
# Run program from file
# --------------------
with open("test.zak", "r", encoding="utf-8") as f:
    code = f.read()

lines = code.splitlines()
run_block(lines)
