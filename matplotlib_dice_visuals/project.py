import matplotlib.pyplot as plt
x_values=range(1,5001)
y_values=[x**3 for x in x_values]
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, s=10)

# Zdefiniowanie tytułu wykresów
ax.set_title("Kwadraty liczb",fontsize=24)
ax.set_xlabel("Wartość",fontsize=12)
ax.set_ylabel("Kwadraty wartości",fontsize=12)
#Zdefiniowanie wielkości etykiet
ax.tick_params(axis = 'both', labelsize=14)
#Zdefiniowanie zakresu dla każdej osi
ax.axis([0,5100,0,1.4e11])
plt.show()
#plt.savefig('squares0test.png',bbox_inches='tight')
