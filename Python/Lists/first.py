row = ["ford", "chevy", "toyota", "honda"]

row.append("nissan")
print(row, "\n")
row[2] = 'crossroad'
print(row, "\n")

row.append("jeep")
print(row, "\n")

row.insert(0, "dodge")
print(row, "\n")

print(row.index("nissan"))

print(row.pop(5))
row.pop(5)
print(row, "\n")
print(row.index('honda'))

