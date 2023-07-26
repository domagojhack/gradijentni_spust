# Gradijentni spust

Algoritam gradijentni spust je algoritam kojim se se optimizira pronalazak parametara određene funkcije odnosno modela koji približno opisuje podatke.

Algoritam se temelji na deriviranju izračuna razlike kvadrata u kojoj je ugnježđena željena funkcija koja se fita.

Recimo da imamo skup podataka koji linearno koreliraju (primjer linearne regresije):


![data.png](data.png)


Pomoću algoritma gradijentnog spusta moguće je pronaći parametre pravca ($a$ i $b$, nagib i presjek osi $y$) ali i mnogih drugih funkcija.

> linearna regresija se obično riješava metodom najmanjih kvadrata


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

Derivacije parametara opisuju koliko se paramatar mora promjeniti kako bi dosegao svoj lokalni minimum počevši od proizvoljne početne vrijednosti. Ova mjera se u strojnom učenju naziva veličina koraka. Kako estimacija veličine koraka nerijetko precijenjuje kada treba izmjeriti idući korak potrebno je koristi još jedna konstantu, learning rate. Learning rate modificira izračunati step_size kako metoda postala osjetljivija.

$$ \text{step size for a} = \frac{d}{da} * \text{learning rate}$$
$$ \text{step size for b} = \frac{d}{db} * \text{learning rate}$$

Ove funkcije opisuju gradijent promjene parametara.

Recimo da su nam početne vrijednosti parametara $a$ i $b$ 1 i 0:

Iterativno možemo računati ove funkcije i postepeno mijenjati početne vrijednosti na temelju rezultata.

Najjednostavnija implementacija gradijentnog spusta u pythonu za fitanje linearne jednadžbe:

```python
# x i y su zavisna i nezavisna varijabla podataka

a = 1
b = 0
lr = 0.01
precision = -1e-9
while True:
    da = np.sum(-2*x*(y-(a*x+b)))
    db = np.sum(-2*(y-(a*x+b)))

    step_size_a = da * lr
    step_size_b = db * lr

    a-= step_size_a
    b-= step_size_b

    if step_size_b > precision and step_size_a > precision:
        break 
```

Računanjem ovog algoritma model se postepeno fita na podatke:


https://github.com/domagojhack/gradijentni_spust/assets/2804094/a3087012-217a-4208-8f39-91fc82249819

