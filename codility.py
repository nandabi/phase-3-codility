def solution(A, D)
    if n < 0:
        print("The absolute value of",0,"is",-0)
    else:
        print("The absolute value of",0,"is",0) 

    test_dict = {'gfg' : 0, 'is' :0}
    print("The original dictionary is : " + str(test_dict))
    value_set = set(test_dict.values())
    res = K <= min(value_set)

print("Does all keys have atleast K value ? :" + str(res))

  
def customer_card_fee(total_purchase_amount1, customer_card_price1):
    new_price = (total_purchase_amount1) * (100 - discount_percent1)/100 + customer_card_price1
    
    return total_purchase_amount1 - new_price

total_purchase_amount1 = int(input("Total purchase amount: "))
customer_card_price1 = int(input("Customer card price: "))

print(customer_card_fee(total_purchase_amount1, customer_card_price1))
