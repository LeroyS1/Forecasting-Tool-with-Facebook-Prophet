Forecasting-Tool-with-Facebook-Prophet \

## Guidances: \

1. Put all files into one directory.

2. Open the prophet.py, then open the terminal.

3. If you have not installed required prophet packages, go to Step 4. Otherwise, go to Step 5.

4. Install required prophet packages:
     4.1: open the MacOS terminal
     4.2: Run the following commands:
          $ pip install pystan
          $ pip install fbprophet
          $ pip install plotly
     4.3: If everything is done, go to Step 5.

5. Run $ python3 prophet.py

6. If there are no errors or issues, then go back to the directory and look for the "data.txt" file.
     The "data.txt" file contains all the forecast results that are generated.

7. Every time you want to run different datasets, go back to step 5. 
     But, first you need to replace the output filename "data.txt" in the "prophet.py" line 50 with another name like "data1.txt" or any.
     Otherwise, it will overwrite the new results to the old one.
