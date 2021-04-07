Python 3.8.9 (tags/v3.8.9:a743f81, Apr  2 2021, 11:10:41) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(40)
>>> t.forward(100)
>>> t.left(40)
>>> t.reset()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(100)
	t.left(90)

	
>>> t.reset()
>>> def ttt():
	for i in range(4):
		t.forward(100)
		t.left(90)

		
>>> ttt()
>>> t.reset()
>>> for i in range(10):
	ttt()
	t.left(36)

	
>>> 