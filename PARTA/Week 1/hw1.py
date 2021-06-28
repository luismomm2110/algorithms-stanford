def splitNumber(term, digits):
	divisor = digits/2

	firstHalf = int(term // (10 ** divisor))
	secondHalf = int(term % (10 ** divisor))

	return firstHalf, secondHalf
	
def multKara(number1, number2):
	digits = len(str(number1))
	
	if digits == 1:
		product = int(number1)*int(number2)
		return product

	else:
		firstHalf1, secondHalf1 = splitNumber(number1, digits)
		firstHalf2, secondHalf2 = splitNumber(number2, digits)

		term1 = multKara(firstHalf1, firstHalf2)
		term3 = multKara(secondHalf1, secondHalf2)
		term2 = multKara(firstHalf1 + secondHalf1, firstHalf2 + secondHalf2) - term1 - term3
		
		product = ((10**digits)*term1) + ((10**(digits/2))*term2) + term3

		return product

def main():
	print("Karatsuba's Algorithm")
	
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

	print(multKara(12, 34))
	print(multKara(1234,5678))
	print()
	print(multKara(3141592653589793238462643383279502884197169399375105820974944592,
					2718281828459045235360287471352662497757247093699959574966967627
					))
	

if __name__ == "__main__":
	main()
