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
- added ability to output asset and debt totals under account breakdowns
- net worth resembles assets - breakdown
- finally gave investments their own section separate from assets under breakdowns
- still need to code delete function to delete a given account when clicked on
  - need to utilise the id of the account, similarly to accessing the amounts
- would like to add some more content to the home page

11/05/20:
- database deletes all assets regardless of item selected
- need to find solution to this

15/05/20:
- fix finally complete, correct item is deleted when clicked on
- route urls needed changing as they kept calling every function instead of just individual function
- next steps are to add content to home page, perhaps include graphs, and also be able to edit each item, it's name, amount and interest

21/05/20:
- edit button works, changes amount and interest and routes back to account page
- added buttons to home page to route to different pages, increased functionality. 
- add in history for each item, click on and be able to see changes to amount and interest
- blog section: posts on personal journey
- external links to websites: MSE current accounts, reddit UKPF
- referral links: coinbase, moneybox
- include footer
- increase aesthetic look using HTML and CSS