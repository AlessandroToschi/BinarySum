def binary_sum_shift_fast(a,b):
	a_bit_length = a.bit_length()
	b_bit_length = b.bit_length()
	sum_reversed = 0
	sum = 0
	carry_over = 0
	
	max_length = max(a_bit_length, b_bit_length)
	min_length = min(a_bit_length, b_bit_length)
	
	for i in range(min_length):
		LSB_a = a & 1
		LSB_b = b & 1
		bit_sum = LSB_a + LSB_b
		
		if bit_sum == 2:
			sum_reversed = (sum_reversed << 1) | carry_over
			carry_over = 1
		else:
			if (bit_sum + carry_over) == 2:
				sum_reversed = sum_reversed << 1
				carry_over = 1
			else:
				sum_reversed = (sum_reversed << 1) | (carry_over + bit_sum)
				carry_over = 0
		a = a >> 1
		b = b >> 1
	
	for i in range(min_length, max_length):
		if a_bit_length == max_length:
			if ((a & 1) + carry_over) == 2:
				sum_reversed = sum_reversed << 1
				carry_over = 1
			else:
				sum_reversed = (sum_reversed << 1) | (carry_over + (a & 1))
				carry_over = 0
			a = a >> 1
		else:
			if ((b & 1) + carry_over) == 2:
				sum_reversed = sum_reversed << 1
				carry_over = 1
			else:
				sum_reversed = (sum_reversed << 1) | (carry_over + (b & 1))
				carry_over = 0
			b = b >> 1
	
	if carry_over:
		sum_reversed = (sum_reversed << 1) | carry_over
	
	for i in range(max_length):
		sum = (sum << 1) | (sum_reversed & 1)
		sum_reversed = sum_reversed >> 1
		
	return sum

def binary_sum_shift(a,b):
	bit_length = 32
	sum_reversed = 0
	sum = 0
	carry_over = 0
	i = 0
	while i < bit_length:
		LSB_a = a & 1
		LSB_b = b & 1
		bit_sum = LSB_a + LSB_b
		
		if bit_sum == 2:
			sum_reversed = (sum_reversed << 1) | carry_over
			carry_over = 1
		else:
			if (bit_sum + carry_over) == 2:
				sum_reversed = sum_reversed << 1
				carry_over = 1
			else:
				sum_reversed = (sum_reversed << 1) | (carry_over + bit_sum)
				carry_over = 0
		i += 1
		a = a >> 1
		b = b >> 1
	i = 0
	for i in range(bit_length):
		sum = (sum << 1) | (sum_reversed & 1)
		sum_reversed = sum_reversed >> 1
	return sum

def binary_sum_factorization(a,b):
	a_bits = factorize(a)
	a_bits_length = len(a_bits)
	a_bits.reverse()
	
	b_bits = factorize(b)
	b_bits_length = len(b_bits)
	b_bits.reverse()
	
	max_length = max(a_bits_length, b_bits_length)
	min_length = min(a_bits_length, b_bits_length)
	
	sum_bits = []
	carry_over = 0
	
	for i in range(min_length):
		bit_sum = a_bits[i] + b_bits[i]
		
		if bit_sum == 2:
			sum_bits.append(carry_over)
			carry_over = 1
		else:
			if (bit_sum + carry_over) == 2:
				sum_bits.append(0)
				carry_over = 1
			else:
				sum_bits.append(bit_sum + carry_over)
				carry_over = 0
	
	for i in range(min_length, max_length):
		if a_bits_length == max_length:
			if (a_bits[i] + carry_over) == 2:
				sum_bits.append(0)
				carry_over = 1
			else:
				sum_bits.append(a_bits[i] + carry_over)
				carry_over = 0
		else:
			if (b_bits[i] + carry_over) == 2:
				sum_bits.append(0)
				carry_over = 1
			else:
				sum_bits.append(b_bits[i] + carry_over)
				carry_over = 0
				
	if carry_over:
		sum_bits.append(carry_over)
		
	sum_bits.reverse()
	
	return defactorize(sum_bits)
	
def factorize(a):
	bits = []
	while a > 0:
		bits.append((a % 2))
		a /= 2
	return bits
	
def defactorize(bits):
	number = 0
	e = len(bits) - 1
	while e > 0:
		number += bits[0] * (2**e)
		bits.pop(0)
		e -= 1
	return number
