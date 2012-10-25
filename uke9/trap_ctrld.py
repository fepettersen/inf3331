sum = 0
print "Enter a series of integers. Press Ctrl-D to print the sum."
while 1:
    try:
        number = raw_input("> ")
        sum += int(number)
    except EOFError:   # Catch the Ctrl-D
        break
    except:   # Trap all other errors
        print "Bad input. '%s' is not an integer." % number
print
print "The sum is %s." % sum

