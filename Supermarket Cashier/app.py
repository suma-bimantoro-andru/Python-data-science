from module import enterProducts
from module import getPrice
from module import getDiscount
from module import makeBill


buyingData= enterProducts()
membership=input('Enter Costumer Membership : ')
makeBill(buyingData,membership)