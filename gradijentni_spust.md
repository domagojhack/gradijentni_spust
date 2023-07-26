# Gradijentni spust

Algoritam gradijentni spust je algoritam kojim se se optimizira pronalazak parametara određene funkcije odnosno modela koji približno opisuje podatke.

Algoritam se temelji na deriviranju izračuna razlike kvadrata u kojoj je ugnježđena željena funkcija koja se fita.

Recimo da imamo skup podataka koji linearno koreliraju (primjer linearne regresije):

![data.png](data.png)

Pomoću algoritma gradijentnog spusta moguće je pronaći parametre pravca ($a$ i $b$, nagib i presjek osi $y$) modela.

(1) Funkcija pravca modela y i x vrijednosti su nam poznate iz seta podataka

$$ y = ax+b $$


Za bilo koji pravac može se izračunati greška odstupanja od podataka pomoću sume kvadrata reziduala:

(2) Suma kvadrada reziduala

$$\text{Sum of squares} = \sum^{n}_{i=1}(y_i - \hat{y})^2$$

$\text{where:}$
- $y_i = \text{vrijednost koju predviđa model}$
- $\hat{y} = \text{izmjerena vrijednost}$

Ovu mjeru također omžemo zapisati kao slijed zbrojeva za svaku točku seta podataka:

$$ \sum \text{kvadrata reziduala} = (y_1 - y_{x1})^2 + (y_2 - y_{x2})^2 + (y_3 - y_{x3})^2 + ... + (y_n - y_{xn})^2$$

U jednadžbu sume reziduala kvadrata možemo ugnijezditi našu jednadžbu modela tada naša jednadžba izgleda ovako:

$$ \sum \text{kvadrata reziduala} = (y_1 - (ax_1+b))^2 + (y_2 -(ax_1+b))^2 + (y_3 - (ax_1+b))^2 + ... + (y_n - (ax_1+b))^2$$

Gradijentni spust se temelji na na derivacijama ovih jednadžbi za svaki parametar modela:

Za parametar $a$:

$$ \frac{d}{da} = -2x(y_1 - (a*x+b)) + ... ... $$

Za parametar $b$:

$$ \frac{d}{db} = -2(y_1 - (a*x+b)) + ... ... $$

Derivacije parametara opisuju koliko se paramatar mora promjeniti kako bi dosegao svoj lokalni minimum.


