from xml.dom import minidom

doc = minidom.parse('Z:/3.Administration/Finances/Reporting/GECO/export_janv21.xml')

print(doc.firstChild.tagName)

transactions = doc.getElementsByTagName("Transaction")

for transaction in transactions:
    # PurchaseOrderHeaderFields
    print('Numéro de transaction: ' + transaction.getAttribute("id"))

    purchase_order_number = transaction.getElementsByTagName("PurchaseOrderNumber")
    print('Numéro de commande: ' + purchase_order_number[0].firstChild.data)

    date = transaction.getElementsByTagName("PurchaseOrderDate")
    print('Date : ' + date[0].firstChild.data)

    status = transaction.getElementsByTagName("ReleaseStatus")
    print('Status : ' + status[0].firstChild.data)
    if status[0].firstChild.data == '3':
        print('Status : Refusé')
    elif status[0].firstChild.data == '2':
        print('Status : Visé')
    elif status[0].firstChild.data == '1':
        print('Status : Attente de visas')
    elif status[0].firstChild.data == '0':
        print('Status : ---')
        # Si purchase_order_backlog_number > 0 = reliquat -> visé
        processflowfields = transaction.getElementsByTagName("ProcessFlowFields")

        for processflowfield in processflowfields:
            purchase_order_backlog_number = processflowfield.getElementsByTagName('PurchaseOrderBacklogNumber')
            if int(purchase_order_backlog_number[0].firstChild.data) > 0:
                print('Status : Reliquat visé')
            elif int(purchase_order_backlog_number[0].firstChild.data) == 0:
                # Si LineNumber > 1 = commande groupée -> visé
                line_number = processflowfield.getElementsByTagName('LineNumber')
                if int(line_number[0].firstChild.data) > 1:
                    print('Status : Commande groupée visée')
                else:
                    print('Status : Visa non attribué')
            else:
                print('Status : Error')

    else:
        print('Status : Error')

    company = transaction.getElementsByTagName("ProcessFlowNumber")
    print('Company : ' + company[0].firstChild.data)
    if company[0].firstChild.data == '1':
        print('Commande : RM')
    elif company[0].firstChild.data == '5':
        print('Commande : Tiers')
    else:
        print('Commande : Error')

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

# <PurchaseOrderBacklogNumber>4</PurchaseOrderBacklogNumber> différent de 0 = reliquat = visé

# Ne marche pas pour les reliquat <ActionDesignation>Facture fournisseur (N° doc.: 1002872)</ActionDesignation>

# print(t.firstChild.nodeValue)
# [0].firstChild.data)
