class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = list()
    self.balance = 0
    self.withdraws_total = 0

  def __str__(self):
    
    display = f"{self.category:*^30}\n"
    funds = 0
    
    for record in self.ledger:
      
      display += f"{record['description'][:23]:<23}{record['amount']:>7.2f}\n"
      funds += record["amount"]
      
    display += "Total" + ": " + str(funds) 
    
    return display

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.withdraws_total += amount
      self.balance -= amount
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.category)
      category.deposit(amount, "Transfer from " + self.category)
      return True
    return False

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    return True
    
  def get_total_withdraws(self):
    return self.withdraws_total
    


def create_spend_chart(categories):

  bar_chart = "Percentage spent by category\n"
  categ_list = []
  categ_withdraws = 0

  for each in categories:
    categ_withdraws += each.withdraws_total

  for i in range(100,-10,-10):
    bar_chart += f"{str(i):>3}| "
    for each in categories:
      percentage = int((each.withdraws_total/categ_withdraws*100)/10) * 10

      if percentage >= i:
        bar_chart += "o  "
      else:
        bar_chart += "   "
    
    bar_chart += "\n"

  bar_chart += "    -" + f"{'---' * len(categories)}\n" + " " * 5
    
  for category in categories:
    categ_list.append(category.category)
    max_len = len(max(categ_list, key=len))

  for i in range(max_len):
    for category in categories:
      try:
        bar_chart += f"{category.category[i]:<3}"
      except:
        bar_chart += "   "
        
    if i != max_len -1:
      bar_chart += "\n" + " " * 5
      
  return bar_chart
