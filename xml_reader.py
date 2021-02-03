from xml.dom import minidom

doc = minidom.parse('C:/Users/yannc/Desktop/tmp/export.xml')

print(doc.firstChild.tagName)

transactions = doc.getElementsByTagName("Transaction")

for transaction in transactions:
    # PurchaseOrderHeaderFields
    print('Numéro de transaction: ' + transaction.getAttribute("id"))
    purchase_order_number = transaction.getElementsByTagName("PurchaseOrderNumber")
    print('Numéro de commande: ' + purchase_order_number[0].firstChild.data)
    date = transaction.getElementsByTagName("PurchaseOrderDate")
    print('Date : ' + date[0].firstChild.data)

    # Item
    items = transaction.getElementsByTagName("Item")
    for item in items:
        account = item.getElementsByTagName("AccountExpense")
        print('Compte : ' + account[0].firstChild.data)
        section = item.getElementsByTagName("CostCentre1Expense")
        print('Section : ' + section[0].firstChild.data)
        total = item.getElementsByTagName("TotalOrdered")
        print('Prix : ' + total[0].firstChild.data)
    print('----------------')

# print(t.firstChild.nodeValue)
# [0].firstChild.data)
