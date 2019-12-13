def menu():
   """
        prints GK Gas Station Menu Items
   """
   print("\n\n \t Gas Station Menu \n ---------------------------- \n");
   print(" %-5s %-15s %-8s " %("Item Number", "Item Name", "Price Each(in $)"));
   print("\n %-5d %-15s %-10.2f " %(1, "Fill Up Gas Per gallon (Regular)", 2.60));
   print("\n %-5d %-15s %-10.2f " %(2, "Fill Up Gas Per Gallon (Premium)", 3.00));
   print("\n %-5d %-15s %-10.2f " %(3, "Lotto Ticket", 1.00));
   print("\n %-5d %-15s %-10.2f " %(4, "Pack of Beer", 6.00));
   print("\n %-5d %-15s %-10.2f " %(5, "Cigarette Pack", 5.99));
   print("\n %-5d %-15s %-10.2f " %(6, "Pack of Gum", 1.00));
   print("\n\n %-5d %-15s " %(7, "Finalize Purchase"));
  
   # reviews the choices
   ch = int(input("\n\n Item Number: "));
  
   return ch;
  
def printRecipt(name, cash, items, prices, cart):
   """
       creates the bill
   """
   # Opening file for writing bill
   f = open("TransactionReceipt.py", 'w');
  
   # Printing to console
   print("\n\n ---------- Transaction Receipt ---------- \n");
   print("\n Name: " + name);
   print("\n cash or credit: " + cash);
   
  
   print("\n\n Items Purchased: \n\n");
   print(" %-5s %-15s %-8s %-8s" %("Item Number", "Item Name", "Qty", "Price"));
  
   # Printing to file
   f.write("\n\n ---------- Transaction Receipt---------- \n");
   f.write("\n Name: " + name);
   f.write("\n cash: " + cash);
 
  
   f.write("\n\n Items Purchased: \n\n");
   f.write(" %-5s %-15s %-8s %-8s" %("Item Number", "Item Name", "Number of Items", "Price"));
  
   total = 0;
  
   # Iterating over items purchased
   for number in cart.keys():
       if cart[number] != 0:
           # Writing to display and file
           print("\n %-5d %-15s %-8d %-10.2f " %(number, items[number-1], cart[number], prices[number-1] * cart[number]));
           f.write("\n %-5d %-15s %-8d %-10.2f " %(number, items[number-1], cart[number], prices[number-1] * cart[number]));
           total += ( cart[number] * prices[number-1] );
  
   # Printing total
   print("\n\n Total before tax: $%.2f \n" %(total));
   f.write("\n\n Total before tax: $%.2f \n" %(total));
  
   # Calculating tax
   tax = (total * 4.75) / 100.0;
  
   # Calculating total bill
   print("\n\n Tax: $%.2f \n" %(tax));
   f.write("\n\n Tax: $%.2f \n" %(tax));
  
   print("\n\n Total (tax included): $%.2f \n\n \t Thank you for shopping at GK Gas Station! \n  \n" %(total+tax));
   f.write("\n\n Total (tax included): $%.2f \n\n \t Thank you for shopping at GK Gas Station! \n  \n" %(total+tax));
  
   f.close();
  
  
def main():
   """
       Main function
   """
  
   # Reading user details
   name = input("\n Name: ");
   cash = input("\n Cash or Credit: ");
 

   # Holding item names and prices
   items = ["Fill up gas (Regular)", "Fill up gas (premium) ", "Lotto", "Pack of beer", "cigarette pack", "Pack of gum"];
   prices = [2.60, 3.00, 1.00, 6.00, 5.99, 1.00];
   cart = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0};
  
   # Prints the menu
   ch = menu();
  
   # go through until user wants to end program
   while(ch != 7):  
       if ch not in cart.keys():
           print("\n Item Unavailable! \n");
       else:
           # Reading quantity
           qty = int(input("\n Number of Selected Items: "));
           # Updating cart
           cart[ch] += qty;
           print("\n Items Secured! \n");
  
       ch = menu();
  
   # Prints the receipt
   printRecipt(name, cash, items, prices, cart);
  
  
#   activates main function  
main();
