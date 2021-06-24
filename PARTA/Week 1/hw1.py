import math

def multKara(number1, number2):
	digits = int(math.log10(number1)) + 1
	if digits == 1:
		product = number1*number2
	else:
		//TODO

	return product

def main():
	print("Karatsuba's Algorithm")
	
	number1 = int(input("Enter the first number: "))
	number2 = int(input("Enter the second number: "))

	# pseudocode 
	# def recursiveKarai(number1, number2):
	#     countDigits= numbers of digits of number1 and number2
	#     if countDigits == 1: 
	#		product = number1 * number2
	#     else:
	#	   firstHalf1 = primeira metade do numero 1
	#	   sndHalf1 = segunda metade do numero 1
	#	   firstHalf2 = primeira metade do numero 2
	#	   sndHalf2 = segunda metade do numero 2
        #   	   term1 = recursiveKara(firstHalf1, firstHalf2)
	#	   term3 = recursiveKara(sndHalf1, sndHalf2)
	#	   term2 = recursiveKara((firstHalf1 + sndHalf1),(firstHalf2 + sndHalf2)) - term1 - term3
	#          product = 10**n * (term1)  + 10 ** (n/2) *(termo2) +  (term3)      
	#    return  product

	multKara(number1, number2)
	

if __name__ == "__main__":
	main()
