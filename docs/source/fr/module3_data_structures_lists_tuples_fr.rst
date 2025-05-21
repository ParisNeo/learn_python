.. _module3-data-structures-lists-tuples-fr:

================================================================
Module 3 : Structures de Données - Listes et Tuples
================================================================

Bienvenue dans le Module 3 ! Jusqu'à présent, nous avons appris à connaître les données individuelles (comme les nombres et les chaînes de caractères) et comment contrôler le flux de nos programmes. Mais que faire si vous avez besoin de travailler avec une collection d'éléments, comme une liste de noms d'étudiants, une série de relevés de température, ou les coordonnées d'un point ? C'est là qu'interviennent les structures de données. Dans ce module, nous nous concentrerons sur deux types de séquences fondamentaux en Python : les **listes** et les **tuples**.

.. image:: /_static/images/list_tuple_boxes.png
   :alt: Représentation abstraite de listes et tuples comme des boîtes organisées
   :width: 300px
   :align: center


Objectifs d'apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Comprendre ce qu'est une structure de données et pourquoi elle est utile.
*   Définir, créer et initialiser des listes Python.
*   Accéder et modifier les éléments d'une liste en utilisant l'indexation et le découpage en tranches.
*   Utiliser les méthodes courantes des listes pour manipuler des listes (par ex., `append`, `insert`, `remove`, `pop`, `sort`, `reverse`).
*   Comprendre la mutabilité des listes.
*   Définir, créer et initialiser des tuples Python.
*   Accéder aux éléments d'un tuple en utilisant l'indexation et le découpage en tranches.
*   Comprendre l'immuabilité des tuples.
*   Effectuer l'empaquetage et le dépaquetage de tuples.
*   Savoir quand utiliser une liste plutôt qu'un tuple.
*   Itérer sur des listes et des tuples en utilisant des boucles `for`.

----------------------------------------------------

Que sont les Structures de Données ?
=========================

Une **structure de données** est une manière d'organiser et de stocker des données dans un ordinateur afin qu'elles puissent être accédées et modifiées efficacement. Différentes structures de données sont adaptées à différents types d'applications, et certaines sont hautement spécialisées.

Python offre plusieurs structures de données intégrées, notamment :

*   **Listes :** Collections ordonnées et mutables (modifiables) d'éléments.
*   **Tuples :** Collections ordonnées et immuables (non modifiables) d'éléments.
*   **Dictionnaires :** Collections non ordonnées de paires clé-valeur. (Couverts dans un module ultérieur)
*   **Ensembles (Sets) :** Collections non ordonnées d'éléments uniques. (Couverts dans un module ultérieur)

Ce module se concentre sur les listes et les tuples, qui sont tous deux des types de séquences.

----------------------------------------------------

Listes
=====

Une **liste** est l'une des structures de données les plus polyvalentes et les plus couramment utilisées en Python. C'est une collection ordonnée d'éléments, et ces éléments peuvent être de n'importe quel type de données (y compris d'autres listes !). Les listes sont **mutables**, ce qui signifie que vous pouvez modifier leur contenu après leur création (ajouter, supprimer ou modifier des éléments).

Création de Listes
--------------
Vous créez une liste en plaçant des éléments entre crochets `[]`, séparés par des virgules.

.. code-block:: python

    # Une liste vide
    liste_vide = []
    print(liste_vide)      # Sortie : []
    print(type(liste_vide)) # Sortie : <class 'list'>

    # Une liste d'entiers
    nombres = [1, 2, 3, 4, 5]
    print(nombres)         # Sortie : [1, 2, 3, 4, 5]

    # Une liste de chaînes de caractères
    fruits = ["pomme", "banane", "cerise"]
    print(fruits)          # Sortie : ['pomme', 'banane', 'cerise']

    # Une liste avec des types de données mixtes
    liste_mixte = [1, "bonjour", 3.14, True, [10, 20]]
    print(liste_mixte)      # Sortie : [1, 'bonjour', 3.14, True, [10, 20]]

Accès aux Éléments d'une Liste (Indexation)
----------------------------------
Vous pouvez accéder aux éléments individuels d'une liste en utilisant leur **indice**. Python utilise une indexation basée sur zéro, ce qui signifie que le premier élément est à l'indice 0, le deuxième à l'indice 1, et ainsi de suite.

.. code-block:: python

    fruits = ["pomme", "banane", "cerise", "datte"]
    # Indice:    0        1         2        3

    print(fruits[0])  # Sortie : pomme
    print(fruits[2])  # Sortie : cerise

    # Indexation négative : -1 fait référence au dernier élément, -2 à l'avant-dernier, etc.
    print(fruits[-1]) # Sortie : datte
    print(fruits[-3]) # Sortie : banane

    # Accéder à un élément d'une liste imbriquée
    donnees = [10, 20, ["a", "b"], 40]
    print(donnees[2])    # Sortie : ['a', 'b']
    print(donnees[2][1]) # Sortie : b

Découpage en Tranches de Listes (Slicing)
-------------
Le découpage en tranches (slicing) vous permet d'obtenir une sous-liste (une portion de la liste). La syntaxe est `liste[debut:fin:pas]`.

*   `debut` : L'indice du premier élément à inclure (par défaut 0).
*   `fin` : L'indice du premier élément à *ne pas* inclure (il va jusqu'à cet indice, mais ne l'inclut pas).
*   `pas` : La valeur d'incrémentation (par défaut 1).

.. code-block:: python

    nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Indice:  0  1  2  3  4  5  6  7  8  9

    print(nombres[2:5])   # Sortie : [2, 3, 4] (éléments de l'indice 2 jusqu'à, mais non inclus, l'indice 5)
    print(nombres[:4])    # Sortie : [0, 1, 2, 3] (du début jusqu'à l'indice 4)
    print(nombres[6:])    # Sortie : [6, 7, 8, 9] (de l'indice 6 jusqu'à la fin)
    print(nombres[-3:])   # Sortie : [7, 8, 9] (les 3 derniers éléments)
    print(nombres[::2])   # Sortie : [0, 2, 4, 6, 8] (un élément sur deux, pas de 2)
    print(nombres[::-1])  # Sortie : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inverse la liste)
    print(nombres[:])     # Sortie : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (une copie superficielle de toute la liste)

Modification des Listes (Mutabilité)
----------------------------
Parce que les listes sont mutables, vous pouvez modifier leurs éléments, en ajouter de nouveaux ou en supprimer d'existants.

.. code-block:: python

    couleurs = ["rouge", "vert", "bleu"]
    print(f"Original : {couleurs}")

    # Modifier un élément
    couleurs[1] = "jaune"
    print(f"Après modification : {couleurs}") # Sortie : Original : ['rouge', 'vert', 'bleu']
                                             # Sortie : Après modification : ['rouge', 'jaune', 'bleu']

    # Modifier une tranche
    nombres = [1, 2, 3, 4, 5]
    nombres[1:3] = [20, 30, 40] # Remplace les éléments aux indices 1 et 2 par de nouveaux éléments
    print(nombres)              # Sortie : [1, 20, 30, 40, 4, 5]

Méthodes Courantes des Listes
-------------------
Les listes Python sont dotées de nombreuses méthodes intégrées utiles :

*   `append(element)`: Ajoute `element` à la fin de la liste.
    .. code-block:: python
        ma_liste = [1, 2]
        ma_liste.append(3)
        print(ma_liste) # Sortie : [1, 2, 3]

*   `insert(indice, element)`: Insère `element` à l'`indice` spécifié.
    .. code-block:: python
        ma_liste = [1, 3]
        ma_liste.insert(1, 2) # Insère 2 à l'indice 1
        print(ma_liste)     # Sortie : [1, 2, 3]

*   `remove(element)`: Supprime la première occurrence de `element` de la liste. Lève une `ValueError` si `element` n'est pas trouvé.
    .. code-block:: python
        ma_liste = ["a", "b", "c", "b"]
        ma_liste.remove("b")
        print(ma_liste) # Sortie : ['a', 'c', 'b']

*   `pop(indice=-1)`: Supprime et retourne l'élément à l'`indice`. Si `indice` n'est pas spécifié, il supprime et retourne le dernier élément.
    .. code-block:: python
        ma_liste = [10, 20, 30, 40]
        element_retire = ma_liste.pop()    # Supprime et retourne 40
        print(element_retire)            # Sortie : 40
        print(ma_liste)                # Sortie : [10, 20, 30]
        premier_element = ma_liste.pop(0)  # Supprime et retourne 10
        print(premier_element)             # Sortie : 10
        print(ma_liste)                # Sortie : [20, 30]

*   `index(element)`: Retourne l'indice de la première occurrence de `element`. Lève une `ValueError` si `element` n'est pas trouvé.
    .. code-block:: python
        ma_liste = ["x", "y", "z"]
        print(ma_liste.index("y")) # Sortie : 1

*   `count(element)`: Retourne le nombre de fois où `element` apparaît dans la liste.
    .. code-block:: python
        ma_liste = [1, 2, 2, 3, 2]
        print(ma_liste.count(2)) # Sortie : 3

*   `sort(key=None, reverse=False)`: Trie les éléments de la liste sur place.
    .. code-block:: python
        nombres = [3, 1, 4, 1, 5, 9, 2]
        nombres.sort()
        print(nombres) # Sortie : [1, 1, 2, 3, 4, 5, 9]
        nombres.sort(reverse=True)
        print(nombres) # Sortie : [9, 5, 4, 3, 2, 1, 1]

*   `reverse()`: Inverse les éléments de la liste sur place.
    .. code-block:: python
        ma_liste = [1, 2, 3]
        ma_liste.reverse()
        print(ma_liste) # Sortie : [3, 2, 1]

*   `clear()`: Supprime tous les éléments de la liste.
    .. code-block:: python
        ma_liste = [1, 2, 3]
        ma_liste.clear()
        print(ma_liste) # Sortie : []

*   `copy()`: Retourne une copie superficielle (shallow copy) de la liste.
    .. code-block:: python
        original = [1, 2, [3, 4]]
        liste_copiee = original.copy()
        liste_copiee[0] = 100
        liste_copiee[2][0] = 300 # Modifie la liste imbriquée dans l'original et la copie
        print(original)        # Sortie : [1, 2, [300, 4]]
        print(liste_copiee)    # Sortie : [100, 2, [300, 4]]

La Fonction `len()`
--------------------
La fonction intégrée `len()` (pas une méthode) retourne le nombre d'éléments dans une liste.

.. code-block:: python
    ma_liste = ["a", "b", "c", "d"]
    print(len(ma_liste)) # Sortie : 4

Itération sur les Listes
--------------------
Vous pouvez utiliser une boucle `for` pour itérer sur les éléments d'une liste.

.. code-block:: python
    fruits = ["pomme", "banane", "cerise"]
    for fruit in fruits:
        print(fruit)
    # Sortie :
    # pomme
    # banane
    # cerise

    # Pour obtenir à la fois l'indice et l'élément, utilisez enumerate() :
    for indice, fruit in enumerate(fruits):
        print(f"Indice {indice}: {fruit}")
    # Sortie :
    # Indice 0: pomme
    # Indice 1: banane
    # Indice 2: cerise

----------------------------------------------------

Tuples
======

Un **tuple** est similaire à une liste : c'est une collection ordonnée d'éléments. Cependant, les tuples sont **immuables**, ce qui signifie qu'une fois qu'un tuple est créé, vous ne pouvez pas modifier son contenu (vous ne pouvez pas ajouter, supprimer ou modifier des éléments).

Création de Tuples
---------------
Vous créez un tuple en plaçant des éléments entre parenthèses `()`, séparés par des virgules.

.. code-block:: python

    # Un tuple vide
    tuple_vide = ()
    print(tuple_vide)      # Sortie : ()
    print(type(tuple_vide)) # Sortie : <class 'tuple'>

    # Un tuple d'entiers
    nombres_tuple = (1, 2, 3, 4, 5)
    print(nombres_tuple)    # Sortie : (1, 2, 3, 4, 5)

    # Un tuple avec des types de données mixtes
    tuple_mixte = (1, "bonjour", 3.14, True)
    print(tuple_mixte)      # Sortie : (1, 'bonjour', 3.14, True)

    # Les parenthèses sont optionnelles pour la création de tuples dans de nombreux contextes (empaquetage de tuple)
    autre_tuple = 10, 20, "monde"
    print(autre_tuple)    # Sortie : (10, 20, 'monde')

    # Cas spécial : La création d'un tuple avec un seul élément nécessite une virgule finale
    tuple_un_element = (99,) # La virgule en fait un tuple
    pas_un_tuple = (99)      # Ceci est juste l'entier 99 entre parenthèses
    print(type(tuple_un_element)) # Sortie : <class 'tuple'>
    print(type(pas_un_tuple))     # Sortie : <class 'int'>

Accès aux Éléments d'un Tuple (Indexation et Tranchage)
-----------------------------------------------
L'accès aux éléments d'un tuple fonctionne exactement comme pour les listes, en utilisant l'indexation et le tranchage.

.. code-block:: python

    mon_tuple = ("a", "b", "c", "d", "e")
    print(mon_tuple[0])    # Sortie : a
    print(mon_tuple[-1])   # Sortie : e
    print(mon_tuple[1:3])  # Sortie : ('b', 'c')

Immuabilité des Tuples
----------------------
C'est la différence clé par rapport aux listes. Vous ne pouvez pas modifier un tuple après sa création.

.. code-block:: python

    mon_tuple = (10, 20, 30)
    # mon_tuple[0] = 100  # Lèverait une TypeError : 'tuple' object does not support item assignment
    # mon_tuple.append(40) # Lèverait une AttributeError : 'tuple' object has no attribute 'append'

    # Cependant, si un tuple contient un objet mutable (comme une liste), cet objet peut être modifié :
    mutable_dans_tuple = (1, 2, [3, 4])
    mutable_dans_tuple[2][0] = 300 # La liste à l'intérieur du tuple est modifiée
    print(mutable_dans_tuple)      # Sortie : (1, 2, [300, 4])
    # Le tuple lui-même (ses références aux objets) reste inchangé.

Méthodes des Tuples
-------------
Les tuples ont moins de méthodes que les listes car ils sont immuables.

*   `count(element)`: Retourne le nombre de fois où `element` apparaît dans le tuple.
*   `index(element)`: Retourne l'indice de la première occurrence de `element`.

.. code-block:: python

    mon_tuple = (1, 2, 2, 3, 2, 4)
    print(mon_tuple.count(2))  # Sortie : 3
    print(mon_tuple.index(3))  # Sortie : 3 (l'indice de la première occurrence de 3)

La fonction `len()` fonctionne également avec les tuples.

Empaquetage et Dépaquetage de Tuples
---------------------------
*   **Empaquetage (Packing) :** Lorsque vous affectez des valeurs séparées par des virgules à une seule variable, Python les "empaquète" dans un tuple.
    .. code-block:: python
        point = 10, 20, 30 # Empaquetage de tuple
        print(point)       # Sortie : (10, 20, 30)

*   **Dépaquetage (Unpacking) :** Vous pouvez affecter les éléments d'un tuple (ou d'une liste) à plusieurs variables.
    .. code-block:: python
        coordonnees = (3, 7)
        x, y = coordonnees # Dépaquetage de tuple
        print(f"x: {x}, y: {y}") # Sortie : x: 3, y: 7

        # Le nombre de variables doit correspondre au nombre d'éléments dans le tuple/liste
        # a, b = (1, 2, 3) # ValueError: too many values to unpack

Pourquoi Utiliser les Tuples ?
---------------
*   **Immuabilité :** Garantit que les données ne seront pas modifiées accidentellement. Utile pour représenter des collections fixes d'éléments, comme les valeurs de couleur RVB `(255, 0, 0)`.
*   **Performance :** Les tuples peuvent être légèrement plus rapides que les listes pour l'itération dans certains cas, bien que cette différence soit souvent négligeable pour les petites collections.
*   **Clés de Dictionnaire :** Les tuples peuvent être utilisés comme clés dans les dictionnaires (car ils sont immuables et hachables), tandis que les listes ne le peuvent pas. (Plus d'informations à ce sujet dans le module Dictionnaires).
*   **Lisibilité :** L'utilisation d'un tuple peut indiquer à quelqu'un qui lit votre code que cette collection d'éléments n'est pas destinée à être modifiée.

----------------------------------------------------

Choisir Entre Listes et Tuples
=================================

*   Utilisez une **liste** lorsque :
    *   Vous avez besoin d'une collection d'éléments qui pourrait changer (ajouter, supprimer, modifier).
    *   L'ordre des éléments est important.
    *   Vous avez besoin de trier ou d'inverser fréquemment la collection.
*   Utilisez un **tuple** lorsque :
    *   Vous avez une collection d'éléments qui ne doit pas changer.
    *   Vous voulez utiliser la collection comme clé dans un dictionnaire.
    *   L'ordre des éléments est important, mais la collection est fixe.
    *   Vous voulez assurer l'intégrité des données.

----------------------------------------------------

Mini-Projet : Gestionnaire Simple de Liste de Tâches
=======================================

Utilisons une liste pour créer un gestionnaire de liste de tâches basique en ligne de commande.

**Objectif :**
1.  Permettre à l'utilisateur d'ajouter des tâches à une liste de tâches.
2.  Permettre à l'utilisateur de voir toutes les tâches de la liste.
3.  Permettre à l'utilisateur de marquer une tâche comme terminée (la supprimer de la liste).
4.  Permettre à l'utilisateur de quitter le programme.

**Étapes :**

1.  Initialisez une liste vide appelée `tasks`.
2.  Utilisez une boucle `while True` pour créer une interface pilotée par menu.
3.  À l'intérieur de la boucle, affichez les options à l'utilisateur : Ajouter, Voir, Supprimer, Quitter.
4.  Obtenez le choix de l'utilisateur en utilisant `input()`.
5.  Utilisez des instructions `if/elif/else` pour gérer le choix de l'utilisateur :
    *   **Ajouter :** Demandez à l'utilisateur la description de la tâche et ajoutez-la (`append()`) à la liste `tasks`.
    *   **Voir :**
        *   Si la liste est vide, affichez "Votre liste de tâches est vide."
        *   Sinon, itérez sur la liste `tasks` en utilisant `enumerate()` pour afficher chaque tâche avec son numéro (par ex., "1. Acheter des provisions").
    *   **Supprimer :**
        *   D'abord, affichez les tâches avec des numéros (comme dans Voir).
        *   Si la liste est vide, informez l'utilisateur.
        *   Demandez à l'utilisateur le numéro de la tâche à supprimer.
        *   Convertissez l'entrée en entier. Assurez-vous de soustraire 1 pour obtenir l'indice correct.
        *   Utilisez `try-except` pour gérer les `ValueError` potentielles (si l'entrée n'est pas un nombre) ou `IndexError` (si le numéro est hors limites).
        *   Si valide, utilisez `pop()` pour supprimer la tâche et afficher une confirmation.
    *   **Quitter :** Affichez un message d'au revoir et sortez (`break`) de la boucle.
    *   **Choix Invalide :** Affichez un message d'erreur.

**Exemple d'Interaction :**

.. code-block:: text

    Gestionnaire de Liste de Tâches
    --------------------
    1. Ajouter Tâche
    2. Voir Tâches
    3. Supprimer Tâche
    4. Quitter
    Entrez votre choix : 1
    Entrez la description de la tâche : Acheter du lait
    Tâche ajoutée !

    Entrez votre choix : 2
    Votre Liste de Tâches :
    1. Acheter du lait

    Entrez votre choix : 1
    Entrez la description de la tâche : Promener le chien
    Tâche ajoutée !

    Entrez votre choix : 2
    Votre Liste de Tâches :
    1. Acheter du lait
    2. Promener le chien

    Entrez votre choix : 3
    Votre Liste de Tâches :
    1. Acheter du lait
    2. Promener le chien
    Entrez le numéro de la tâche à supprimer : 1
    Tâche "Acheter du lait" supprimée.

    Entrez votre choix : 4
    Fermeture du Gestionnaire de Liste de Tâches. Au revoir !

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # gestionnaire_liste_taches.py

       tasks = [] # Nom de variable conservé en anglais pour la cohérence du code Python

       def display_tasks(): # Nom de fonction conservé
           if not tasks:
               print("Votre liste de tâches est vide.")
               return False # Indique que la liste est vide
           print("\nVotre Liste de Tâches :")
           for index, task in enumerate(tasks):
               print(f"{index + 1}. {task}")
           print("-" * 20)
           return True # Indique que la liste contient des tâches

       print("Gestionnaire de Liste de Tâches")
       print("--------------------")

       while True:
           print("\nMenu :")
           print("1. Ajouter Tâche")
           print("2. Voir Tâches")
           print("3. Supprimer Tâche (Marquer comme terminée)")
           print("4. Quitter")

           choice = input("Entrez votre choix (1-4) : ")

           if choice == '1':
               task_description = input("Entrez la description de la tâche : ")
               tasks.append(task_description)
               print(f"Tâche '{task_description}' ajoutée !")
           elif choice == '2':
               display_tasks()
           elif choice == '3':
               if display_tasks(): # Continuer seulement s'il y a des tâches
                   try:
                       task_num_str = input("Entrez le numéro de la tâche à supprimer : ")
                       task_num = int(task_num_str)
                       if 1 <= task_num <= len(tasks):
                           removed_task = tasks.pop(task_num - 1) # Ajuster pour l'indice basé sur 0
                           print(f"Tâche '{removed_task}' supprimée.")
                       else:
                           print("Numéro de tâche invalide.")
                   except ValueError:
                       print("Entrée invalide. Veuillez entrer un nombre.")
                   except IndexError: # Devrait être intercepté par la condition if, mais bonne pratique
                       print("Numéro de tâche invalide (hors limites).")
           elif choice == '4':
               print("Fermeture du Gestionnaire de Liste de Tâches. Au revoir !")
               break
           else:
               print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

----------------------------------------------------

Résumé du Module 3
================

Bravo ! Vous avez maintenant été initié à deux structures de données Python essentielles :

*   Les **listes** sont des collections ordonnées et **mutables**, parfaites lorsque vous avez besoin de stocker une séquence d'éléments qui pourrait changer. Vous avez appris à créer, indexer, découper en tranches et utiliser diverses méthodes comme `append()`, `remove()` et `sort()`.
*   Les **tuples** sont des collections ordonnées et **immuables**, idéales pour les séquences de données fixes où l'intégrité est importante. Vous avez appris leur création (en particulier la nuance du tuple à un seul élément), l'indexation, le découpage en tranches et pourquoi leur immuabilité est utile.
*   Vous comprenez maintenant les principales différences entre les listes et les tuples et avez une meilleure idée de quand utiliser chacun.
*   Itérer sur ces séquences en utilisant des boucles `for` est une compétence fondamentale que vous avez pratiquée.

Ces structures de données sont des éléments de base pour des programmes plus complexes, vous permettant de gérer efficacement des groupes de données associées.

Dans le prochain module, nous explorerons des structures de données plus puissantes : les **dictionnaires et les ensembles (sets)**, qui offrent différentes manières d'organiser et d'accéder aux données : :ref:`module4-data-structures-dictionaries-sets-fr` !