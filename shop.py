class Shop(object):
    def __init__(self, shop_name='', store_type=''):
        self.shop_name = shop_name
        self.store_type = store_type
        self.numbers_of_units = 0

        print (shop_name + '\n' +  store_type)

    def describe_shop(self):
        long_name = str(self.shop_name) + ' ' + self.store_type
        return long_name
        
    def open_shop(self):
        print ('Shop is open now')

    def set_number_of_units(self, units_to_set):
        self.units_to_set=units_to_set
        self.numbers_of_units = self.units_to_set
        return units_to_set
    def increment_number_of_units(self):
        self.numbers_of_units = self.numbers_of_units + 5
        return self.numbers_of_units

class Discount(Shop):
    def __init__(self, discount_products):
        #super().__init__(shop_name, store_type)
        self.discount_products = list(discount_products)

    def get_discounts_ptoducts(self):
        return self.discount_products

"""Створіть клас з ім’ям Shop(). Метод __init__() класу Shop() повинен містити два атрибути:
shop_name і store_type. Створіть метод describe_shop(), який виводить два атрибути, і метод open_shop(),
який виводить повідомлення про те, що онлайн-магазин відкритий. Створіть на основі класу екземпляр з ім’ям store. 
Виведіть два атрибути окремо, потім викличте обидва методи."""

store = Shop()
print(store.describe_shop())
store.open_shop()



"""Створіть три різних екземпляри класу, викличте для кожного екземпляру метод describe_shop()"""

shop_model = Shop('Model shop', 'For hobism')
print(shop_model.describe_shop())
shop_tools = Shop('Shop Tools and Fools', 'this tools u can use everyday and anywhere')
print(shop_tools.describe_shop())
shop_pc = Shop('Hardware store for PC', 'Anything for minning is here')
print(shop_pc.describe_shop())



"""Додайте атрибут number_of_units зі значенням за замовчуванням 0;
він представляє кількість видів товару у магазині.
Створіть екземпляр з ім’ям store. Виведіть значення number_of_units,
а потім змініть number_of_units і виведіть знову."""

print('Default numbers of units are ', store.numbers_of_units)
store.numbers_of_units = 100500
print('Changed numbers of units', store.numbers_of_units)



"""Додайте метод з ім’ям set_number_of_units(), що дозволяє задати кількість видів товару.
Викличте метод з новим числом, знову виведіть значення. Додайте метод з ім’ям increment_number_of_units(),
який збільшує кількість видів товару на задану величину. Викличте цей метод."""

units = 10
store.set_number_of_units(units)
print('Numbers of Units is set to', store.numbers_of_units)

print('increment_number_of_units to 5, now numbers of units are: ', store.increment_number_of_units())
print('increment_number_of_units to 5, now numbers of units are: ', store.increment_number_of_units())



"""Напишіть клас Discount(), що успадковує від класу Shop(). Додайте атрибут з ім’ям 
discount_products для зберігання списку товарів, на які встановлена знижка. 
Напишіть метод get_discounts_ptoducts, який виводить цей список. 
Створіть екземпляр store_discount і викличте цей метод."""

store_discount = Discount(['Roco', 'Piko'])
print('List of discount producrs: ' , store_discount.get_discounts_ptoducts())
