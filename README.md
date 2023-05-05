# Inventory App

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>

The purpose of this app is to assist store managers to manage inventory in their shoe warehouse. Store managers are able to view the the inventory across all warehouses internationally and to perform inventory related tasks such as: stock taking, viewing all inventory on hand across all warehouses, searching for specific shoes for details, view the value of inventory on hand, to identify which shoes need to be restocked and capturing new stock.

## Installation <a name="installation"><a> 

There are two different ways to run the program: using Docker or a virtual environment.

### Docker

You can either use docker on your desktop or by using Docker Playground. Descriptions for using both options are included.

**Run container using Desktop**

1. If you don't already have Docker installed on your desktop, install Docker on your desktop.

2. Once installed, enter the following command in the terminal:

```
docker run -i bonolor/inventory-app
```

**Run container using Docker Playground**

1. Go to Docker Playground at the following link and enter "Start": https://labs.play-with-docker.com/.

2. Add a new instance.
  
3. Enter the following command in the terminal:

```
docker run -i bonolor/inventory-app
```

### Virtual Environment

1. Download the files in the repository.

2. Create a project folder named "inventory-app".
 
3. Move and save the downloaded files to the inventory-app folder.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the inventory-app folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal (use relevant python version):
   
  ```
  python3.11 -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the garden_ai directory (if you are not already in the directory):
  
  ```
  cd inventory-app
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. If prompted to upgrade pip, enter:

  ```
  pip install --upgrade pip
  ```
  
11. Select inventory.py and run the program.

## Usage <a name="usage"><a>

1. The menu provides various options from which you can select:

<img width="1021" alt="Screenshot 2023-05-05 at 15 15 22" src="https://user-images.githubusercontent.com/127111801/236467778-5d177775-7701-4dd4-aba1-fac1b3b33153.png">

2. View all shoe inventory by select "1" from the menu.

<img width="1021" alt="Screenshot 2023-05-05 at 15 18 02" src="https://user-images.githubusercontent.com/127111801/236468482-cdd382b9-e4dc-4a7a-959e-52afc9bdec09.png">

3. Capture new shoe inventory by selecting "2" from the menu.

- Enter the country.
- Enter the shoe's SKU code.
- Enter the name of the shoe.
- Enter the cost per shoe.
- Enter the quantity of shoe(s) you would like to capture.
- A message will be printed once the shoe has been successfully captured.

<img width="1021" alt="Screenshot 2023-05-05 at 15 23 01" src="https://user-images.githubusercontent.com/127111801/236469492-d3e1742f-40e1-434b-82d1-157569f1d59a.png">

4. To see which shoe inventory needs to be restocked, select "3". 

- This will display the shoe with the lowest stock.
- Answer the question of whether you would like to restock the shoe and add to the quantity in the system.
- Enter the additional quanity of shoes you would like to add.
- A message will confirm once the shoe quantity has been successfully updated and will display the new inventory balance for the shoe in the system.

<img width="1021" alt="Screenshot 2023-05-05 at 15 30 42" src="https://user-images.githubusercontent.com/127111801/236471425-fdb8a6b0-249b-4f4d-aafe-5e7e08c33b0c.png">

5. Search for a shoe in the system by selecting "4".

- Enter the SKU code for the shoe you would like to view. If you enter an incorrect or invalid SKU, the program will notify you of that and you'll need to try again.
- Once you enter a valid SKU, the details of the shoe selected will display on the screen.

<img width="1021" alt="Screenshot 2023-05-05 at 15 45 21" src="https://user-images.githubusercontent.com/127111801/236475122-a354ae06-2ca0-4337-9fb1-6dbd08339f7a.png">

6. View the inventory value of all the stock on hand by selecting "5".

<img width="1021" alt="Screenshot 2023-05-05 at 15 52 24" src="https://user-images.githubusercontent.com/127111801/236476959-96c00986-2d53-49d3-9994-3402852265e5.png">

7. To view the shoe to be placed on sale, select "6". This shows the shoe that has the highest quantity in the system and so has been placed on sale to reduce stock.

<img width="1021" alt="Screenshot 2023-05-05 at 15 55 27" src="https://user-images.githubusercontent.com/127111801/236477756-8956fabb-1aaf-4402-ada7-3c4eb5813e53.png">

8. Exit the system by selecting "7".

<img width="1021" alt="Screenshot 2023-05-05 at 15 57 25" src="https://user-images.githubusercontent.com/127111801/236478384-dfe02e13-b987-4237-bd3e-7bb76c73ce13.png">

## Credit and Contribution <a name="credit_and_contribution"><a> 

This project has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.
