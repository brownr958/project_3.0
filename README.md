![House1](https://user-images.githubusercontent.com/74078757/123913251-fcae7b80-d94b-11eb-960b-76b76cdbc115.jpg)

Welcome to the final project for Ryan Brown, Austin Williams, Micah West, and Greg Parker in the UNC Data Science Boot Camp. The requirements for this project were to find a problem worth solving or analyzing, use machine learning to solve the problem or at least attempt to solve, and to use two of the tools we learned in the last portion of the boot camp.

### How We Did It

In this project, we used machine learning on data from house prices in Ames, Iowa. The data can be found here: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data?select=data_description.txt. The goal was to make a house price calculator using Random Forest machine learning to come up with a formula. The data came with many fields, but only eleven were used in our calculator. Although the fields we used were not the most accurate in predicting the sales price, they are more practical when entering information on a house. The fields that were the most accurate were qualities most people might not even know in the first place. In order to make a more user-friendly application, common knowledge fields such as bedrooms, baths, and square footage were used. A flask app was used to take the eleven inputs from our HTML and insert them into the price formula. The calculated value was then sent back and displayed on our HTML, which was built using CSS, JS, D3, and Bootstrap.

### How We Ran It

In order to run our house price calculator, you need to first clone the repository to your computer. Then, using your terminal of choice, direct it to the Front End folder. Once in that folder, make sure to also activate PythonData. Proceed to run the app.py in that folder by entering "python app.py". As that is running, switch to your browser (Chrome was used for this project) and enter "127.0.0.1:5000" in the URL. The first thing you should see is the header that is also included at the beginning of this readME. After scrolling down slightly, you should see the skeleton of a house with empty boxes that looks like this: 

![House2](https://user-images.githubusercontent.com/74078757/123917483-d808d280-d950-11eb-9e10-57e50b35e48a.jpg)

You can enter values in the boxes provided to calculate the price of your dream house or the one you are staying in currently. Whatever you desire. Once all the boxes contain values, click the Calculate button to get your house price. Keep in mind the price will be what the house is estimated to be worth in Ames, Iowa. Make sure you also pay attention to the note and enter only whole numbers and zeros where certain parts of the house do not apply. Some values also have limits, so no outrageous house prices can be calculated. We hope you enjoy our project and thanks for visiting the repository!
