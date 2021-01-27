#Simple Password Cracker without threads
import zipfile
		
def extracFile(zFile, password):		
	try:
		zFile.extractall(pwd=password)
		return password
	except:
		return
def main():
	zFile = zipfile.ZipFile('secret.zip')
	passFile = open('dictionary.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		guess = extracFile(zFile, password)
		if guess:
			print '[+] Password = ' + password + '\n'
			exit(0)
		
if __name__ == '__main__':
	main()