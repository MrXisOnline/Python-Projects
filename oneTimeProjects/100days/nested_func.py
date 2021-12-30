def outer_func():
	print("I'm Outer.")

	def inner_func():
		print("I'm Inner.")
	return inner_func

inner = outer_func()
inner()