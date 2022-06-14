# Pour_Choices


I will make an app that allows the user to input the items in their liquor cabinets (through a dynamic search of pre-listed items) and returns drinks that the user is able to make with the listed ingredients.

Views will include:
  1. Home (where the user can input their ingredients and get back the menu of makable drinks - this will be a list of drink names that can be clicked on to view their details)
  2. Index of drinks, a show page for individual drinks (accessible by clicking from their menu or the index page)
  3. Add page for drinks 
  4. Random Drink page (actually same as show page, but pulls a random cocktail rather than a selected cocktail)
  5. Update page for drinks
  6. My Account Page
  7. Edit List Page
  8. About page

It will be a full CRUD app, and will have a confirmation for users before they delete items. I am using Django, for both fron and back end.

The above is the MVP of the project, stretch goals include:
  1. User Auth (would also add views/changes to views)
  2. User created lists need to have the ability to add Drinks
  3. Parameters for drink menu (all drinks must include X ingredient, no drink should include X ingredient)
  4. A feature that determines what one ingredient added to your home bar would allow you to make the most new drinks
  5. User voting on suggested drink additions

WireFrames:
Home View - ![Screen Shot 2022-06-14 at 4 27 57 PM](https://user-images.githubusercontent.com/6979738/173682790-ebe031a9-c749-4a7e-8ef3-0f6d6f14ece1.png)
Index - ![Screen Shot 2022-06-14 at 4 28 05 PM](https://user-images.githubusercontent.com/6979738/173682872-da26d2c7-40bb-46c3-805d-7424b647fd68.png)
About Page - ![Screen Shot 2022-06-14 at 4 28 32 PM](https://user-images.githubusercontent.com/6979738/173683136-fc31dc93-1afd-46f8-a5dd-9e9e3a23d8ff.png)
My Account Page - ![Screen Shot 2022-06-14 at 4 28 17 PM](https://user-images.githubusercontent.com/6979738/173682957-74fb0d9f-7fdd-4a1b-a00a-5fc77152c1e7.png)
Create List Page - ![Screen Shot 2022-06-14 at 4 28 25 PM](https://user-images.githubusercontent.com/6979738/173683007-6174224c-01ab-4958-a370-4894e32e1e57.png)
Cocktail Show Page - ![Screen Shot 2022-06-14 at 4 28 11 PM](https://user-images.githubusercontent.com/6979738/173682898-2702b7ef-d0cb-4080-9732-865db3841db0.png)
Edit Cocktail Page - ![Screen Shot 2022-06-14 at 4 28 46 PM](https://user-images.githubusercontent.com/6979738/173683079-65aebefb-6d20-40a9-b884-9a7175733391.png)

