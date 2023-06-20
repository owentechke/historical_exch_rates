import requests
import matplotlib.pyplot as plt

my_key="your_API_key_goes-here"

my_years = []
KES_rate = []
for my_year in range(2000, 2024):
    my_url="http://api.exchangeratesapi.io/v1/"+str(my_year)+"-06-15?access_key="+my_key
    response = requests.get(my_url)

    my_dict = response.json()
    euro_rate = my_dict['rates']['EUR']
    usd_rate = my_dict['rates']['USD']
    kes_to_euro = my_dict['rates']['KES']
    #kes_to_usd = kes_to_euro * (euro_rate/usd_rate)
    kes_to_usd = kes_to_euro/usd_rate # same as above since this site is based on the Euro, so Euro is 1.00
    my_years.append(my_year)
    KES_rate.append(kes_to_usd)
    #KES_rate.append(my_dict['rates']['KES'])
    
print("Done") # I was using Jupyter Notebook, so I wanted to know when the loop was done

# Set the figure size and create the plot
plt.figure(figsize=(8, 6))
plt.plot(my_years, KES_rate, color='red')

# Customize the plot
plt.title("USD to KES Rates (Years 2000 to 2023)", fontsize='16')
plt.xlabel("Year", fontsize='13', color='green')
plt.ylabel("USD-KES Rate", fontsize='13', color='blue')
plt.minorticks_on()
plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle=':', linewidth=0.5)

# Save and show the plot
plt.savefig('ExRatesAPI_io.png')
plt.show()
