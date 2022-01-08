from compiletobytes import CompileToBytes

compiletobytes = CompileToBytes()

class MainCompiler():
	def __init__(self):
	    pass

	def readFile(file:str):
		""" Reads the file """
		readfile = open(file, 'rb')
		eachdata = []
		with readfile as f:
			data = f.read()