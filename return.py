#function是用來「收納」程式碼的，是個功能增加程式使用性，要執行需再把功能寫出來使用

def sum_of_list(numbers):
    sum_number = 0
    for i in  numbers:
        sum_number = i + 1
    return sum_number #return是把function結果存下來

print(sum_of_list([1, 2, 3]))


def average(numbers):
	#avg = sum(numbers) / len(numbers) 這兩行註解掉等於下面那行
	#return avg 
	return sum(numbers) / len(numbers) #return是把function結果存下來，此處的sum是內建功能和len一樣

#a = average([1, 2, 3])  這兩行註解掉等於下面那行
#print(a)
print(average([1, 2, 3]))
print(average([100, 2456, 3256899]))


#公元年分非4的倍數，為平年。公元年分為4的倍數但非100的倍數，為閏年。公元年分為100的倍數但非400的倍數，為平年。公元年分為400的倍數為閏年。
def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    elif year % 3200 != 0:
        return True
    else:
        return False
#a = is_leap(400)
#print(a)

print(is_leap(400))
print(is_leap(2022))



