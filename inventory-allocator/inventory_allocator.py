import json

# object inventoryAllocator:
class inventoryAllocator(object):

    # object initialization:
    # sets its internal object "self.order" to input 1
    # sets its internal object "self.warehouses" to input 2
    # sets an empty object inventoryDict = {}
    def __init__(self,input1,input2):
        # self.JSONdata = JSONdata;

        #TODO uncomment these
        print(input1)
        print(input2)

        self.order = json.loads(input1)
        self.warehouses = json.loads(input2)
        self.inventoryDict = {}

        print("INPUT 1 - Order:")
        print(self.order)
        print("INPUT 2 - Net Inventory:")
        print(self.warehouses)

    # function processInventory processes input #2 into a different format, such
    # that all items amounts, and warehouse sources are accounted for. It sets the
    # class variable "self.inventoryDict" (type: dict) into the following format:
    # EXAMPLE INVENTORYDICT
    # {
    #   "ITEM1": [totalAmountOfItem1, [[warehouse1, amountInWarehouse1],[warehouse2, amountInWarehouse2]] ],
    #   "ITEM2": [totalAmountOfItem2, [[warehouse2, amountInWarehouse2]] ]
    # }
    def processInventory(self):
        for warehouse in self.warehouses: #for each warehouse
            for item in warehouse['inventory']: #for each fruit type in a warehouse
                if item in self.inventoryDict:
                    self.inventoryDict[item][0] += warehouse['inventory'][item]
                else:
                    self.inventoryDict[item] = []
                    self.inventoryDict[item].append(warehouse['inventory'][item])
                    self.inventoryDict[item].append([])

                self.inventoryDict[item][1].append([warehouse['name'],warehouse['inventory'][item]])

    # function produceCheapestShipment creates the cheapest shipment available.
    # if a shipment cannot be produced (not enough stock to satisfy order/cannot
    # satisfy order) it returns an empty list.
    # input: none, changes class variables in function
    # output: prints to console appropriate shipment.
    def produceCheapestShipment(self):

        # function isValidOrder: makes sure that order can be fully fulfilled
        # if not all ordered items can be shipped, then return false. Else
        # return true.
        # input: takes an "order", in JSON format
        # output: true or false, depending on able to ship or not
        def isValidOrder(order):
            for item in order:
                if item not in self.inventoryDict or order[item] > self.inventoryDict[item][0] or order[item] < 0:
                    return False
            return True

        shipmentWithListBracket = []
        shipment = {}
        if isValidOrder(self.order): #if the order is valid
            for item in self.order: #for each item in the order
                # decrease from order, decrease from inventory, while increasing "shipment"
                while self.order[item] > 0:
                    self.inventoryDict[item][1][0][1] = self.inventoryDict[item][1][0][1] - 1 #decrement from warehouse stock
                    self.inventoryDict[item][0] = self.inventoryDict[item][0] - 1 #decrease from total stock

                    if self.inventoryDict[item][1][0][0] not in shipment: # if warehouse name not in shipment
                        shipment[self.inventoryDict[item][1][0][0]] = {} # add warehouse name to shipment

                    # if item name is not under warehouse name in shipment
                    if item not in shipment[self.inventoryDict[item][1][0][0]]:
                        shipment[self.inventoryDict[item][1][0][0]][item] = 0 #set item name & amount in shipment to 0

                    #increment item amount in correct warehouse by 1
                    shipment[self.inventoryDict[item][1][0][0]][item] = shipment[self.inventoryDict[item][1][0][0]][item] + 1

                    #if specific warehouse is out of the queried item
                    if self.inventoryDict[item][1][0][1] == 0:
                        del self.inventoryDict[item][1][0] #delete the warehouse from stock

                    self.order[item] = self.order[item] - 1 #decrement order amount

            if bool(shipment): #if there are orders with zero amounts
                shipmentWithListBracket.append(shipment)
            print(shipmentWithListBracket)
        else: #if the order cannot be met
            print(shipmentWithListBracket) #just return empty brackets
