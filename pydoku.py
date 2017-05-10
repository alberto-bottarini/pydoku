class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y	
		self.available_values = range(1,10)
		self.value = False
	
	def set_value(self, value):
		self.value = int(value)

	def remove_available_value(self, available_value):
		if available_value in self.available_values:
			self.available_values.remove(available_value)

	def remove_available_values(self, available_values):
		for value in available_values:
			self.remove_available_value(value)

	def has_value(self):
		return bool(self.value) != False


class Grid:
	def __init__(self, schema):
		self.cells = []
		for i, c in enumerate(schema):
			x = i % 9
			y = int(i / 9)
			cell = Cell(x, y)
			if c != "-": cell.set_value(c)
			self.cells.append(cell)
	
	def pretty_print(self):
		out = ""
		for i, c in enumerate(self.cells):
			if i != 0 and i % 9 == 0: out += "\n"
			if bool(c.value): out += str(c.value)
			else: out += "-"
			out += " "
		print out

	def get_rows(self):
		rows = []
		for r in range(9):
			row = []
			for c in range(9): 
				row.append(self.get_cell(r, c))
			rows.append(row)
		return rows

	def get_columns(self):
		columns = []
		for c in range(9):
			column = []
			for r in range(9):
				column.append(self.get_cell(r, c))
			columns.append(column)
		return columns

	def get_blocks(self):
		blocks = []
		for rr in range(3):
			for cc in range(3):
				block = []
				for c in range(cc*3, cc*3+3):
					for r in range(rr*3, rr*3+3):
						block.append(self.get_cell(r, c))
				blocks.append(block)
		return blocks

	def do_optimization_rows(self):
		for row in self.get_rows():
			values = []
			for cell in row:
				if cell.has_value():
					values.append(cell.value)
			for cell in row:
				if cell.has_value() == False:
					print "Removing not valid values %s from cell [%s,%s] because already present in cell row" % (values, cell.x, cell.y)
					cell.remove_available_values(values)
			
	def do_optimization_columns(self):
		for column in self.get_columns():
			values = []
			for cell in column:
				if cell.has_value():
					values.append(cell.value)
			for cell in column:
				if cell.has_value() == False:
					print "Removing not valid values %s from cell [%s,%s] because already present in cell column" % (values, cell.x, cell.y)
					cell.remove_available_values(values)

	def do_optimization_blocks(self):
		for block in self.get_blocks():
			values = []
			for cell in block:
				if cell.has_value():
					values.append(cell.value)
			for cell in block:
				if cell.has_value() == False:
					print "Removing not valid values %s from cell [%s,%s] because already present in cell block" % (values, cell.x, cell.y)
					cell.remove_available_values(values)

	def refresh_available_values(self):
		for cell in grid.cells:
			if cell.has_value() == False:
				if len(cell.available_values) == 1:
					print "Cell [%s,%s] has a single acccepted value: %s" % (cell.x, cell.y, cell.available_values[0])
					cell.set_value(cell.available_values[0])

	def is_not_solved(self):
		for cell in grid.cells:
			if cell.has_value() == False:
				return True
		return False

	def get_valued_cells(self):
		count = 0
		for cell in grid.cells:
			if cell.has_value():
				count = count+1
		return count

	def get_cell(self, x, y):
		return self.cells[9*x+y]


schema = "\
-8---1--2\
--65-8--4\
-5---436-\
-91-5-4--\
---41--9-\
2---9---1\
5--1---8-\
--87--1--\
9----3-2-"

grid = Grid(schema)
while grid.is_not_solved():
	valued_cells = grid.get_valued_cells()
	grid.pretty_print()
	grid.do_optimization_rows()
	grid.do_optimization_columns()
	grid.do_optimization_blocks()
	grid.get_blocks()
	grid.refresh_available_values()
	if(valued_cells == grid.get_valued_cells()):
		print 'Can\' continue. Break!'
		break

grid.pretty_print()

