# Menu with prices
menu = {
    1: {'item': 'Pizza', 'price': 120},
    2: {'item': 'Lolli pops', 'price': 150},
    3: {'item': 'Pasta', 'price': 70},
    4: {'item': 'Burger', 'price': 60},
    5: {'item': 'Cake', 'price': 45},
    6: {'item': 'French fries', 'price': 60}
}

order = []
total_bill = 0.0

print('Dominos Pizza Hut')
print('1.Pizza - 120\n2.Lolli pops - 150\n3.Pasta - 70\n4.Burger - 60\n5.Cake - 45\n6.French fries - 60')

ch = 'y'
while ch == 'y':
    choice = int(input('Enter your choice (1-6): '))
    if 1 <= choice <= 6:
        item = menu[choice]['item']
        price = menu[choice]['price']
        order.append(item)
        total_bill += price
        print(f'Added {item} to your order. Price: {price:.2f}')
    else:
        print("Invalid choice, please select a valid option.")

    ch = input('Do you want to add any other item (y/n)? ')

print('Your current order:', order)
print(f'Your total bill is: {total_bill:.2f}')

choice = input('Do you want to modify your order (y/n)? ')
while choice == 'y':
    print('1. Add item\n2. Delete item\n3. Modify item')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        print(
            '1.Pizza - 120\n2.Lolli pops - 150\n3.Pasta - 70\n4.Burger - 60\n5.Cake - 45\n6.French fries - 60')
        choice = int(input('Enter your choice (1-6): '))
        if 1 <= choice <= 6:
            item = menu[choice]['item']
            price = menu[choice]['price']
            order.append(item)
            total_bill += price
            print(f'Added {item}. Price: {price:.2f}')
            print(f'Your updated order: {order}')
        else:
            print("Invalid choice.")

    elif choice == 2:
        print('Your order:', order)
        item_to_delete = input('Enter the item name to delete: ')
        if item_to_delete in order:
            i = order.index(item_to_delete)
            for key, value in menu.items():
                if value['item'] == item_to_delete:
                    total_bill -= value['price']
            order.pop(i)
            print(f'Removed {item_to_delete} from your order.')
        else:
            print('Item not found in your order.')
        print(f'Your updated order: {order}')

    elif choice == 3:
        print('Your order:', order)
        old_item = input('Enter the name of the item you want to modify: ')
        if old_item in order:
            new_choice = int(input('Enter the new item number to replace with (1-6): '))
            if 1 <= new_choice <= 6:
                new_item = menu[new_choice]['item']
                new_price = menu[new_choice]['price']
                index = order.index(old_item)
                for key, value in menu.items():
                    if value['item'] == old_item:
                        total_bill -= value['price']
                order[index] = new_item
                total_bill += new_price
                print(f'Replaced {old_item} with {new_item}.')
            else:
                print("Invalid choice.")
        else:
            print('Item not found in your order.')

        print(f'Your updated order: {order}')

    choice = input('Do you want to modify your order further (y/n)? ')

print(f"Your final order is: {order}")
print(f"Your total bill is: {total_bill:.2f}")
