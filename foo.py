tools = ["tournevis","marteau"]
index =  tools.index("marteau")
del tools[index]

for tool in tools:
    print(tool)