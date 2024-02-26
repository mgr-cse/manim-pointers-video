all: pointers.py
	manim -p -ql pointers.py MyScene

clean:
	rm -rf __pycache__ media

.PHONY: clean