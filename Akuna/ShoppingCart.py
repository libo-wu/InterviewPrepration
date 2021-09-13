# An e-commerce company is currently celebrating ten years in business. They are having a sale to honor their privileged members, 
# those who have been using their services for the past five years. They receive the best discounts indicated by any discount tags 
# attached to the product. Determine the minimum cost to purchase all products listed. As each potential price is calculated, round 
# it to the nearest integer before adding it to the total. Return the cost to purchase all items as an integer.
# There are three types of discount tags:
# • Type O: discounted price, the item is sold for a given price.
# • Type 1: percentage discount, the customer is given a fixed percentage discount from the retail price.
# • Type 2: fixed discount, the customer is given a fixed amount off from the retail price.

# Example:
# products = [['10', 'd0', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1', 'EMPTY"]]
# discounts = [['d0','1','27'], ['d1', '2', '5']]
# The products array elements are in the form ['price', 'tag 1', 'tag 2', ..., 'tag m-1'). There may be zero or more discount codes 
# associated with a product. Discount tags in the products array may be 'EMPTY' which is the same as a null value.
# The discounts array elements are in the form ['tag, 'type', 'amount').

# If a privileged member buys product 1 listed at a price of 10 with two discounts available:
# Under discount do of type 1, the discounted price is 10 - 10 * 0.27 = 7.30, round to 7.
# Under discount d1 of type 2, the discounted price is 10-5 = 5. The price to purchase the product 1 is the lowest of the two, or 5 in this case
# The second product is priced at 15 because there are no discounts available
# The third product is priced at 20. Using discount tag d1 of type 2, the discounted price is 20-5= 15 The total price to purchase the three items is 5+ 15 +15 = 35.
# int FindLowestPrice(List<List<string>>products, List<List<string>> discounts){}

def FindLowestPrice(products, discounts):
    dict_discounts = {}
    for i in range(len(discounts)): # create dict
        this_discount = discounts[i]
        dict_discounts[this_discount[0]] = [int(this_discount[1]), int(this_discount[2])]   # dict = {'d0': type, number}
    
    total_price = 0
    for i in range(len(products)): # iterate over products
        product = products[i]   # get current product
        retail = int(product[0])    # get retail price
        price_list_this_product = []    # the list of all possible discounted prices
        for j in range(len(product)-1): # start from index 1
            if product[j+1] == 'EMPTY':
                price_list_this_product.append(retail)  # if empty, add the retail price
            else:
                discount_type = dict_discounts[product[j+1]][0] # get type
                discount_number = dict_discounts[product[j+1]][1]   # get number in the discount
                if discount_type == 0:
                    price_list_this_product.append(type0(discount_number))
                elif discount_type == 1:
                    price_list_this_product.append(type1(retail, discount_number))
                else:
                    price_list_this_product.append(type2(retail, discount_number))
        total_price = total_price + min(price_list_this_product)    # get the minimum price
    return total_price

def type0(discount):
    return int(discount)

def type1(price, percentage):
    return int(price - price*percentage/100)

def type2(price, discount):
    return int(price - discount)

if __name__ == "__main__":
    products = []
    discounts = []
    products.append(['10', 'd0', 'd1'])
    products.append(['15', 'EMPTY', 'EMPTY'])
    products.append(['20', 'd1', 'EMPTY'])
    discounts.append(['d0','1','27'])
    discounts.append(['d1', '2', '5'])
    price = FindLowestPrice(products, discounts)
    print(price)