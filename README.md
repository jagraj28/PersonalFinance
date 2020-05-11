# PersonalFinance
Flask website showing current assets, net worth and different bank accounts a user has.

02/05/2020:
- created base webpage with navigation bar and routing to main page
- thought of Finance Capital as a name
  Next steps:
  - implement forms on subpages
  - implement routes for each subpage
  
03/05/2020:
- added forms for subpages and routing back to home page after filling out forms
- forms reset to blank after clicking submit button
- created classes for each subpage form
  Next steps:
  - implement sql database
  - create login and register
Design change:
Home
Assets
Investments
Debts
Account
  - Net Worth
  - Asset Breakdown
  - Debt Breakdown
Login
Register

06/05/20:
- added ability to output asset and debt totals under account breakdowns. 
- net worth resembles assets - breakdown
- finally gave investments their own section separate from assets under breakdowns
- still need to code delete function to delete a given account when clicked on
  - need to utilise the id of the account, similarly to accessing the amounts
- would like to add some more content to the home page

11/05/20:
- database deletes all assets regardless of item selected
- need to find solution to this
