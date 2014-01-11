# -----------------------------------------------------
# Program Name:		list_processing_recursion.rb
# Lesson: 			Functional Programming Exercises
# Author: 			Chad Hobbs
# Collaborators: 	I developed this code on my own. Alex asked me basic recursion questions.
# Sources: 			http://www.ruby-doc.org/core-2.0.0
# 					
# Due: 				November 12, 2013, 11:59pm	
# -----------------------------------------------------

# Function Name: 	sum()
# Purpose: 			Return the sum of values in a numeric list that may contain other lists.
# Parameters: 		A list of integers, possibly of lists of integers
# Returns: 			A sum of all the numbers in the list

def sum (list)
	if list.empty?
		return 0
	else
		first, *rest = list
		if first.is_a?(Numeric)
			return first + sum(rest)
		else
			return sum(first) + sum(rest)
		end
	end

end

# Function Name: 	remove_odd()
# Purpose: 			Return a list of only the even values from a given list
# Parameters: 		A list of numbers or lists of numbers
# Returns: 			A list with the odd numbers removed

def remove_odd (list)
	if list.empty?
		return list
	else
		first, *rest = list
		if first.kind_of?(Array)
			return remove_odd(rest).unshift(remove_odd(first))
		elsif first.modulo(2) == 1
			return remove_odd(rest)
		else
			return remove_odd(rest).unshift(first)
		end
	end
end


# Function Name: 	digits()
# Purpose: 			Returns the number of digits in a number.
# Parameters: 		A number
# Returns: 			How many digits a number has.

def digits (nums)
	if nums.div(10) == 0
		return 1
	else
		return 1 + digits(nums.div(10))
	end
end

# Function Name: 	ith_digit()
# Purpose: 			Returns the number that is at a given position.
# Parameters: 		A number
# Returns: 			The digit at the specified location.

def ith_digit(num, position)
	if position == 0
		return num.modulo(10)
	else
		return ith_digit((num.div(10)), position - 1)
	end
end

# Function Name: 	occurences()
# Purpose: 			Returns the number of occurences of a specified digit.
# Parameters: 		A number
# Returns: 			How many of a digit a number has.

def occurrences(num, dig)
	if num.div(10) == 0
		if num == dig
			return 1
		else
			return 0
		end
	else
		return occurrences(num.modulo(10),dig) + occurrences(num.div(10),dig)
	end
end

# Function Name: 	digital_sum()
# Purpose: 			Returns the sum of all the individual digits of a number.
# Parameters: 		A number
# Returns: 			The total of the individual digits.

def digital_sum(num)
	if num.div(10) == 0
		return num
	else
		return digital_sum(num.modulo(10)) + digital_sum(num.div(10))
	end
end

# Function Name: 	digital_root()
# Purpose: 			Returns the root sum of the digital sum of the given number.
# Parameters: 		A number
# Returns: 			The root sum of the total sum of the given number.

def digital_root(num)
	if num.div(10) == 0
		return num
	else
		return digital_root(digital_sum(num))
	end
end

# ---------------------------------------
# ----- HOW TO OUTPUT CODE -----
puts "Homework 8, List processing and structural recursion in Ruby"
puts

# -- sum --

puts "-- Testing the sum() function (Exercise 1)--"
puts
puts "The sum of the array [2, 5, [3, 5], 1] is " + (sum([2, 5, [3, 5], 1])).to_s
puts "The sum of the array [[[1],2,3],[4,5],[6]] is " + (sum([[[1],2,3],[4,5],[6]])).to_s
puts

# -- remove_odd --

puts "-- Testing the remove_odd() function (Exercise 2)--"
puts
puts "Original array: [2, 5, [3, 4], 1]       Odds Removed: " + (remove_odd([2, 5, [3, 4], 1]).inspect).to_s
puts "Original array: [2, 5, [3, 5], 1]       Odds Removed: " + (remove_odd([2, 5, [3, 5], 1])).inspect.to_s
puts "Original array: [[1], 2, 5, [3, 4], 1]  Odds Removed: " + (remove_odd([[1], 2, 5, [3, 4], 1])).inspect.to_s
puts

# -- digits() --
puts "-- Now testing the digits() function (Exercise 3)--"
puts
puts "The number 123 has " + (digits(123)).to_s() + " digits"
puts "The number 1234 has " + (digits(1234)).to_s() + " digits"
puts "The number 12345 has " + (digits(12345)).to_s() + " digits"
puts "The number 123456 has " + (digits(123456)).to_s() + " digits"
puts "The number 1234567 has " + (digits(1234567)).to_s() + " digits"
puts

# -- ith_digit() --

puts "-- Now testing the ith_digit() function (Exercise 4)--"
puts
puts "The number in the 0 position of 123 is " + (ith_digit(123, 0)).to_s()
puts "The number in the 3 position of 1234 is " + (ith_digit(1234, 3)).to_s()
puts "The number in the 3 position of 12345 is " + (ith_digit(12345, 3)).to_s()
puts "The number in the 1 position of 123456 is " + (ith_digit(123456, 1)).to_s()
puts "The number in the 6 position of 1234567 is " + (ith_digit(1234567, 6)).to_s()
puts

# -- occurrences() --

puts "-- Now testing the occurrences() function (Exercise 5)--"
puts
puts "There are " + (occurrences(4314243124, 2)).to_s() + " 2's in the number 4314243124"
puts "There are " + (occurrences(1111111111, 1)).to_s() + " 1's in the number 111111111"
puts "There are " + (occurrences(123123123123, 3)).to_s() + " 3's in the number 123123123123"
puts "There are " + (occurrences(111, 2)).to_s() + " 2's in the number 111"
puts "There are " + (occurrences(123451234, 5)).to_s() + " 5's in the number 123451234"
puts

# -- digital_sum() --

puts "-- Now testing the digital_sum() function (Exercise 6)--"
puts
puts "The digital sum of 99999999999 adds up to " + (digital_sum(99999999999)).to_s()
puts "The digital sum of 12345 adds up to " + (digital_sum(12345)).to_s()
puts "The digital sum of 1111111111 adds up to " + (digital_sum(1111111111)).to_s()
puts "The digital sum of 2 adds up to " + (digital_sum(2)).to_s()
puts "The digital sum of 10 adds up to " + (digital_sum(10)).to_s()
puts

# -- digital_root() --

puts "-- Now testing the digital_root() function (Exercise 7)--"
puts
puts "The digital root of 99999999999 adds up to " + (digital_root(99999999999)).to_s()
puts "The digital root of 12345 adds up to " + (digital_root(12345)).to_s()
puts "The digital root of 5555555555 adds up to " + (digital_root(5555555555)).to_s()
puts "The digital root of 8675309 adds up to " + (digital_root(8675309)).to_s()
puts

# ---------------------------------------
# ----- RESULTS -----
=begin
	
Homework 8, List processing and structural recursion in Ruby

-- Testing the sum() function (Exercise 1)--

The sum of the array [2, 5, [3, 5], 1] is 16
The sum of the array [[[1],2,3],[4,5],[6]] is 21

-- Testing the remove_odd() function (Exercise 2)--

Original array: [2, 5, [3, 4], 1]       Odds Removed: [2, [4]]
Original array: [2, 5, [3, 5], 1]       Odds Removed: [2, []]
Original array: [[1], 2, 5, [3, 4], 1]  Odds Removed: [[], 2, [4]]

-- Now testing the digits() function (Exercise 3)--

The number 123 has 3 digits
The number 1234 has 4 digits
The number 12345 has 5 digits
The number 123456 has 6 digits
The number 1234567 has 7 digits

-- Now testing the ith_digit() function (Exercise 4)--

The number in the 0 position of 123 is 3
The number in the 3 position of 1234 is 1
The number in the 3 position of 12345 is 2
The number in the 1 position of 123456 is 5
The number in the 6 position of 1234567 is 1

-- Now testing the occurrences() function (Exercise 5)--

There are 2 2's in the number 4314243124
There are 10 1's in the number 111111111
There are 4 3's in the number 123123123123
There are 0 2's in the number 111
There are 1 5's in the number 123451234

-- Now testing the digital_sum() function (Exercise 6)--

The digital sum of 99999999999 adds up to 99
The digital sum of 12345 adds up to 15
The digital sum of 1111111111 adds up to 10
The digital sum of 2 adds up to 2
The digital sum of 10 adds up to 1

-- Now testing the digital_root() function (Exercise 7)--

The digital root of 99999999999 adds up to 9
The digital root of 12345 adds up to 6
The digital root of 5555555555 adds up to 5
The digital root of 8675309 adds up to 2

	
=end





