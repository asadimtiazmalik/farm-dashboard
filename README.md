# Wheat Health Monitoring Dashboard

## **Introduction**

This application provides health information regarding the Wheat crop and provides ways to assess wheat health using both satellite and drone imagery. The Raster Visualization helps us understand the distribution of ndvi all across the ROI. 


![Raster Visualization](https://user-images.githubusercontent.com/65748116/230757994-63a1d4c7-10ca-45d8-8ba2-acd0aa1af85c.jpg)


## **Cloning the repository**

Clone the repo by navigating to the folder where you want to store your project and run the following command:

>`git clone https://github.com/asadimtiazmalik/farm-dashboard.git`


## **Activating a virtual environment**

Once you have successfully cloned the repository, install all the dependencies required to run this application. To do so, navigate to the `.../farm-dashboard` folder and open VSCode. Once you do this launch your conda environment by running the command:

>`conda activate env`

## **Installing Dependancies**


Upon successfully starting the environment run the command below to install the releveant dependancies to run this appliation.

>`pip intsall -r requirements.txt`

## **Running this application**

If you have reached this stage it means we are almost done. Lets now run the following command to finally run this application.

>`python -m streamlit streamlit_app.py` OR simply
>
>`streamlit streamlit_app.py`

