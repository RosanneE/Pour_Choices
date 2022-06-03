I will make an app that allows the user to input the items in their liquor cabinets (through a dynamic search of pre-listed items) and returns drinks that the user is able to make with the listed ingredients.

Views will include Home (where the user can input their ingriedients and get back the menue of makable drinks - this will be a list of drink names that can be clicked on to view their details), an index of drinks, a show page for individual drinks (accessable by clicking from their menue or the index page), an add page for drinks, an update page for drinks, and an about page.

It will be a full CRUD app, and will have a confirmation for users before they delete items. I currently plan to use Django, but I may switch to React/Mongodb over the weekend if I have trouble using postgres (the M1 has sqlite3 preloaded (so it is what i have used on Finch), but sqlite3 does not work with a heroku deployment).

MVP: 1.Full CRUD Views: 1. Home 2. Index 3. Show 4. Add 5. Edit 6. About 2. Use Django (or React/Mongodb) for a deployment through heroku 3. Delete route, with verification of delete 4. Dynamic search bar for Drink Ingredients 5. Menu feature shows drinks makable with only the ingredients in the list 6. Use either pre-created API (several are availible) or create my own (this is what I want to do, already have advice/examples from Keisha)

The above is the MVP of the project, stretch goals include: User Auth (would also add views/changes to views) User created lists (favorites, things to try, things I've tried) Parameters for drink menue (all drinks must include X ingredient, no drink should include X ingredient) A Random drink page that pulls up a random drink from the drinks list A feature that determines what one ingredient added to your home bar would allow you to make the most new drinks User voting on suggested drink additions

Wire Frames: