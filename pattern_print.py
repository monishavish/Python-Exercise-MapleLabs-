# program to print below pattern:
#	* * * * *
#	 * * * *
#	  * * *
#	   * *
#	    *
#	   * *
#	  * * *
#	 * * * *
#	* * * * *

if __name__ == "__main__":
    rows = 5
    i = 0
    while i <= rows - 1: #starting from 5
        j = 0
        while j < i: #for space
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1: #printing star.
            print('*', end=' ')
            k += 1
        print()
        i += 1

    i = rows - 1
    while i >= 0:
        j = 0
        while j < i: #print space
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1: #print star
            print('*', end=' ')
            k += 1
        print('')
        i -= 1