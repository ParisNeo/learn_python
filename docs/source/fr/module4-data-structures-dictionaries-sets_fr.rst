.. _module4-data-structures-dictionaries-sets-fr:

======================================================================
Module 4 : Structures de Données - Dictionnaires et Ensembles (Sets)
======================================================================

Bienvenue dans le Module 4 ! Nous avons exploré les collections ordonnées avec les listes et les tuples. Maintenant, nous allons plonger dans deux autres structures de données Python puissantes : les **dictionnaires** et les **ensembles (sets)**. Les dictionnaires nous permettent de stocker des données sous forme de paires clé-valeur, offrant un moyen de rechercher rapidement des informations en utilisant un identifiant personnalisé (la clé). Les ensembles, d'autre part, sont des collections non ordonnées d'éléments uniques, parfaits pour des tâches comme la suppression de doublons ou l'exécution d'opérations mathématiques sur les ensembles.

.. image:: /_static/images/dict_set_mindmap.png
   :alt: Représentation abstraite de dictionnaires (clé-valeur) et d'ensembles (éléments uniques)
   :width: 350px
   :align: center

Objectifs d'apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Comprendre et créer des dictionnaires Python pour stocker des paires clé-valeur.
*   Accéder, ajouter, modifier et supprimer des éléments des dictionnaires.
*   Itérer sur les clés, les valeurs et les paires clé-valeur d'un dictionnaire.
*   Utiliser efficacement les méthodes courantes des dictionnaires.
*   Comprendre et créer des ensembles (sets) Python pour stocker des éléments uniques et non ordonnés.
*   Ajouter et supprimer des éléments des ensembles.
*   Effectuer les opérations courantes sur les ensembles : union, intersection, différence et différence symétrique.
*   Comprendre quand utiliser les dictionnaires par rapport aux ensembles.
*   Découvrir les `frozensets` comme équivalents immuables des ensembles.

----------------------------------------------------

Dictionnaires (`dict`)
=====================

Un **dictionnaire** en Python est une collection non ordonnée d'éléments. Alors que d'autres types de données composites n'ont que des valeurs comme éléments, un dictionnaire contient des **paires clé-valeur**. Chaque clé est unique au sein d'un dictionnaire, et elle est utilisée pour accéder à sa valeur correspondante. Pensez-y comme un dictionnaire du monde réel où vous recherchez un mot (la clé) pour trouver sa définition (la valeur).

Les clés doivent être d'un type immuable (comme les chaînes de caractères, les nombres ou les tuples ne contenant que des éléments immuables). Les valeurs peuvent être de n'importe quel type de données.

Création de Dictionnaires
---------------------
Vous pouvez créer des dictionnaires de plusieurs manières :

1.  **En utilisant des accolades `{}` avec des paires clé-valeur :**
    .. code-block:: python

        # Un dictionnaire vide
        dict_vide = {}
        print(dict_vide)       # Sortie : {}
        print(type(dict_vide)) # Sortie : <class 'dict'>

        # Un dictionnaire de scores d'étudiants
        scores_etudiants = {"Alice": 95, "Bob": 88, "Charlie": 92}
        print(scores_etudiants)   # Sortie : {'Alice': 95, 'Bob': 88, 'Charlie': 92}

        # Les clés peuvent être de différents types immuables (bien que généralement cohérentes)
        dict_cles_mixtes = {1: "un", "deux": 2, (3,0): "trois"}
        print(dict_cles_mixtes)  # Sortie : {1: 'un', 'deux': 2, (3, 0): 'trois'}

2.  **En utilisant le constructeur `dict()` :**
    .. code-block:: python

        # À partir d'arguments nommés (les clés doivent être des identifiants valides)
        personne = dict(nom="Diana", age=30, ville="Londres")
        print(personne) # Sortie : {'nom': 'Diana', 'age': 30, 'ville': 'Londres'}

        # À partir d'une liste de tuples clé-valeur
        paires = [("fruit", "pomme"), ("couleur", "rouge")]
        info_fruit = dict(paires)
        print(info_fruit) # Sortie : {'fruit': 'pomme', 'couleur': 'rouge'}

Accès aux Valeurs d'un Dictionnaire
---------------------------
Vous accédez aux valeurs d'un dictionnaire en vous référant à leurs clés entre crochets `[]`.

.. code-block:: python

    scores_etudiants = {"Alice": 95, "Bob": 88, "Charlie": 92}
    print(scores_etudiants["Alice"]) # Sortie : 95
    # print(scores_etudiants["David"]) # Lèverait une KeyError si "David" n'est pas une clé

Utilisation de la méthode `get()` :
La méthode `get(cle, valeur_par_defaut)` est un moyen plus sûr d'accéder aux valeurs. Elle retourne la valeur pour `cle` si `cle` est dans le dictionnaire, sinon `valeur_par_defaut`. Si `valeur_par_defaut` n'est pas spécifiée, elle vaut `None` par défaut.

.. code-block:: python

    print(scores_etudiants.get("Bob"))       # Sortie : 88
    print(scores_etudiants.get("David"))     # Sortie : None
    print(scores_etudiants.get("David", "Non trouvé")) # Sortie : Non trouvé

Modification des Dictionnaires
----------------------
Les dictionnaires sont mutables.

*   **Ajout ou Mise à Jour d'Éléments :**
    Si la clé existe, sa valeur est mise à jour. Si la clé n'existe pas, une nouvelle paire clé-valeur est ajoutée.
    .. code-block:: python

        scores_etudiants = {"Alice": 95, "Bob": 88}
        scores_etudiants["Charlie"] = 92 # Ajoute un nouvel élément
        print(scores_etudiants)        # Sortie : {'Alice': 95, 'Bob': 88, 'Charlie': 92}
        scores_etudiants["Alice"] = 97   # Met à jour un élément existant
        print(scores_etudiants)        # Sortie : {'Alice': 97, 'Bob': 88, 'Charlie': 92}

*   **Suppression d'Éléments :**
    *   `pop(cle, valeur_par_defaut)`: Supprime l'élément avec la `cle` spécifiée et retourne sa valeur. Lève `KeyError` si la clé n'est pas trouvée et qu'aucune valeur par défaut n'est donnée.
        .. code-block:: python
            score = scores_etudiants.pop("Bob")
            print(score)              # Sortie : 88
            print(scores_etudiants)     # Sortie : {'Alice': 97, 'Charlie': 92}
            # score_manquant = scores_etudiants.pop("Eve") # KeyError

    *   `popitem()`: Supprime et retourne un élément (clé, valeur) arbitraire du dictionnaire (dans les versions antérieures à Python 3.7, il supprimait un élément aléatoire ; à partir de 3.7+, il supprime les éléments dans l'ordre LIFO - dernier entré, premier sorti). Lève `KeyError` si le dictionnaire est vide.
        .. code-block:: python
            element = scores_etudiants.popitem()
            print(element)               # par ex., ('Charlie', 92) si c'était le dernier ajouté
            print(scores_etudiants)     # par ex., {'Alice': 97}

    *   `del nom_dict[cle]`: Supprime l'élément avec la clé spécifiée. Lève `KeyError` si la clé n'est pas trouvée.
        .. code-block:: python
            config = {"host": "localhost", "port": 8080}
            del config["port"]
            print(config) # Sortie : {'host': 'localhost'}

    *   `clear()`: Supprime tous les éléments du dictionnaire.
        .. code-block:: python
            config.clear()
            print(config) # Sortie : {}

Méthodes Courantes des Dictionnaires
-------------------------
*   `keys()`: Retourne un objet de vue qui affiche une liste de toutes les clés du dictionnaire.
*   `values()`: Retourne un objet de vue qui affiche une liste de toutes les valeurs du dictionnaire.
*   `items()`: Retourne un objet de vue qui affiche une liste des paires tuple (clé, valeur) d'un dictionnaire.

.. code-block:: python

    scores_etudiants = {"Alice": 95, "Bob": 88, "Charlie": 92}
    print(scores_etudiants.keys())   # Sortie : dict_keys(['Alice', 'Bob', 'Charlie'])
    print(scores_etudiants.values()) # Sortie : dict_values([95, 88, 92])
    print(scores_etudiants.items())  # Sortie : dict_items([('Alice', 95), ('Bob', 88), ('Charlie', 92)])

    # Vous pouvez convertir ces objets de vue en listes si nécessaire :
    liste_cles = list(scores_etudiants.keys())
    print(liste_cles) # Sortie : ['Alice', 'Bob', 'Charlie']

*   `update(autre_dict)`: Met à jour le dictionnaire avec les paires clé-valeur de `autre_dict`, écrasant les clés existantes.
    .. code-block:: python
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict1.update(dict2)
        print(dict1) # Sortie : {'a': 1, 'b': 3, 'c': 4}

*   `copy()`: Retourne une copie superficielle (shallow copy) du dictionnaire.

Itération sur les Dictionnaires
---------------------------
Vous pouvez itérer sur les dictionnaires de plusieurs manières :

.. code-block:: python

    scores_etudiants = {"Alice": 95, "Bob": 88, "Charlie": 92}

    # Itérer sur les clés (itération par défaut)
    print("--- Clés ---")
    for nom in scores_etudiants:
        print(nom) # Affiche Alice, Bob, Charlie

    # Itérer explicitement sur les clés
    print("--- Clés (explicite) ---")
    for nom in scores_etudiants.keys():
        print(nom)

    # Itérer sur les valeurs
    print("--- Valeurs ---")
    for score in scores_etudiants.values():
        print(score) # Affiche 95, 88, 92

    # Itérer sur les paires clé-valeur (items)
    print("--- Éléments (Items) ---")
    for nom, score in scores_etudiants.items():
        print(f"{nom}: {score}")
    # Sortie :
    # Alice: 95
    # Bob: 88
    # Charlie: 92

Compréhensions de Dictionnaire (Avancé)
------------------------------------
Similaires aux compréhensions de liste, vous pouvez créer des dictionnaires de manière concise.

.. code-block:: python

    nombres = [1, 2, 3, 4]
    dict_carres = {x: x**2 for x in nombres}
    print(dict_carres) # Sortie : {1: 1, 2: 4, 3: 9, 4: 16}

    noms = ["pomme", "banane", "cerise"]
    longueurs_noms = {nom: len(nom) for nom in noms}
    print(longueurs_noms) # Sortie : {'pomme': 5, 'banane': 6, 'cerise': 6}

Quand Utiliser les Dictionnaires
------------------------
*   Lorsque vous avez besoin d'associer des clés uniques à des valeurs (par ex., des ID utilisateur avec des profils utilisateur).
*   Pour des recherches rapides par un identifiant unique.
*   Lorsque les données sont naturellement représentées sous forme de paires clé-valeur (par ex., paramètres de configuration, données de type JSON).
*   Pour compter les fréquences d'éléments.

----------------------------------------------------

Ensembles (`set`)
============

Un **ensemble (set)** est une collection non ordonnée d'éléments **uniques**. Les ensembles sont mutables, ce qui signifie que vous pouvez y ajouter ou en supprimer des éléments. Ils sont particulièrement utiles pour tester l'appartenance, supprimer les doublons d'une séquence et effectuer des opérations mathématiques sur les ensembles comme l'union, l'intersection, la différence et la différence symétrique.

Création d'Ensembles
-------------
1.  **En utilisant des accolades `{}` avec des éléments séparés par des virgules :**
    .. code-block:: python

        # Un ensemble d'entiers
        ensemble_nombres = {1, 2, 3, 4, 3, 2} # Les doublons sont automatiquement supprimés
        print(ensemble_nombres)             # Sortie : {1, 2, 3, 4} (l'ordre peut varier)
        print(type(ensemble_nombres))       # Sortie : <class 'set'>

        # Un ensemble de types de données mixtes (les éléments doivent être hachables/immuables)
        ensemble_mixte = {1, "bonjour", 3.14, (1, 2)}
        print(ensemble_mixte)               # Sortie : {1, 3.14, (1, 2), 'bonjour'} (l'ordre peut varier)

    .. important::
        Pour créer un **ensemble vide**, vous *devez* utiliser le constructeur `set()`, et non `{}`.
        `accolades_vides = {}` crée un *dictionnaire* vide.
        `ensemble_vide = set()` crée un *ensemble* vide.

        .. code-block:: python
            ens_vide = set()
            print(ens_vide)        # Sortie : set()
            print(type(ens_vide))  # Sortie : <class 'set'>

2.  **En utilisant le constructeur `set()` avec un itérable (par ex., liste, tuple, chaîne) :**
    .. code-block:: python

        ma_liste = [1, 2, 2, 3, "a", "a"]
        ensemble_depuis_liste = set(ma_liste)
        print(ensemble_depuis_liste) # Sortie : {1, 2, 3, 'a'} (l'ordre peut varier)

        ensemble_depuis_chaine = set("bonjourr")
        print(ensemble_depuis_chaine) # Sortie : {'b', 'j', 'n', 'o', 'r', 'u'} (l'ordre peut varier)

Modification des Ensembles
--------------
*   `add(element)`: Ajoute un élément à l'ensemble. Si l'élément est déjà présent, ne fait rien.
    .. code-block:: python
        mon_ensemble = {1, 2}
        mon_ensemble.add(3)
        print(mon_ensemble) # Sortie : {1, 2, 3}
        mon_ensemble.add(2) # Ajout d'un élément existant
        print(mon_ensemble) # Sortie : {1, 2, 3}

*   `remove(element)`: Supprime `element` de l'ensemble. Lève une `KeyError` si l'élément n'est pas trouvé.
    .. code-block:: python
        mon_ensemble = {1, 2, 3}
        mon_ensemble.remove(2)
        print(mon_ensemble) # Sortie : {1, 3}
        # mon_ensemble.remove(4) # Lèverait une KeyError

*   `discard(element)`: Supprime `element` de l'ensemble s'il est présent. Ne lève *pas* d'erreur si l'élément n'est pas trouvé.
    .. code-block:: python
        mon_ensemble = {1, 2, 3}
        mon_ensemble.discard(3)
        print(mon_ensemble) # Sortie : {1, 2}
        mon_ensemble.discard(4) # Pas d'erreur
        print(mon_ensemble) # Sortie : {1, 2}

*   `pop()`: Supprime et retourne un élément arbitraire de l'ensemble. Lève `KeyError` si l'ensemble est vide.
    .. code-block:: python
        mon_ensemble = {"a", "b", "c"}
        element_retire = mon_ensemble.pop()
        print(element_retire) # par ex., 'a' (l'ordre n'est pas garanti)
        print(mon_ensemble)    # par ex., {'c', 'b'}

*   `clear()`: Supprime tous les éléments de l'ensemble.

Opérations sur les Ensembles
--------------
Les ensembles supportent des opérations mathématiques puissantes.

Soient `A = {1, 2, 3, 4}` et `B = {3, 4, 5, 6}`

*   **Union :** Éléments présents dans l'ensemble A ou l'ensemble B (ou les deux).
    *   Opérateur : `|`
    *   Méthode : `union()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        ens_union_op = A | B
        ens_union_meth = A.union(B)
        print(ens_union_op)   # Sortie : {1, 2, 3, 4, 5, 6}
        print(ens_union_meth) # Sortie : {1, 2, 3, 4, 5, 6}

*   **Intersection :** Éléments présents à la fois dans l'ensemble A et l'ensemble B.
    *   Opérateur : `&`
    *   Méthode : `intersection()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        ens_intersection_op = A & B
        ens_intersection_meth = A.intersection(B)
        print(ens_intersection_op)   # Sortie : {3, 4}
        print(ens_intersection_meth) # Sortie : {3, 4}

*   **Différence :** Éléments présents dans l'ensemble A mais pas dans l'ensemble B.
    *   Opérateur : `-`
    *   Méthode : `difference()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        ens_difference_op = A - B # Éléments dans A mais pas dans B
        ens_difference_meth = A.difference(B)
        print(ens_difference_op)   # Sortie : {1, 2}
        print(ens_difference_meth) # Sortie : {1, 2}
        print(B - A)               # Sortie : {5, 6} (Éléments dans B mais pas dans A)

*   **Différence Symétrique :** Éléments présents dans l'ensemble A ou l'ensemble B, mais pas dans les deux.
    *   Opérateur : `^`
    *   Méthode : `symmetric_difference()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        diff_sym_op = A ^ B
        diff_sym_meth = A.symmetric_difference(B)
        print(diff_sym_op)   # Sortie : {1, 2, 5, 6}
        print(diff_sym_meth) # Sortie : {1, 2, 5, 6}

Autres Méthodes des Ensembles
-----------------
*   `issubset(autre_ensemble)`: Retourne `True` si tous les éléments de l'ensemble sont présents dans `autre_ensemble`.
*   `issuperset(autre_ensemble)`: Retourne `True` si tous les éléments de `autre_ensemble` sont présents dans l'ensemble.
*   `isdisjoint(autre_ensemble)`: Retourne `True` si l'ensemble n'a aucun élément en commun avec `autre_ensemble`.

Test d'Appartenance (`in`)
-----------------------
Vérifier si un élément existe dans un ensemble est très efficace.

.. code-block:: python
    mon_ensemble = {"pomme", "banane", "cerise"}
    print("pomme" in mon_ensemble)  # Sortie : True
    print("raisin" in mon_ensemble) # Sortie : False

Quand Utiliser les Ensembles
----------------
*   Supprimer les doublons d'une liste ou d'une autre séquence.
*   Test d'appartenance rapide (vérifier si un élément est dans une collection).
*   Effectuer des opérations mathématiques sur les ensembles (union, intersection, etc.).
*   Lorsque l'ordre des éléments n'a pas d'importance et que vous avez besoin d'unicité.

----------------------------------------------------

Frozensets (`frozenset`)
========================

Un **frozenset** est une version immuable d'un ensemble Python. Une fois créé, vous ne pouvez pas modifier son contenu (ajouter ou supprimer des éléments). Parce qu'ils sont immuables et hachables, les frozensets peuvent être utilisés comme clés de dictionnaire ou comme éléments d'un autre ensemble, ce que les ensembles réguliers (mutables) ne peuvent pas faire.

.. code-block:: python

    ma_liste = [1, 2, 3, 2, 1]
    ens_gele = frozenset(ma_liste)
    print(ens_gele) # Sortie : frozenset({1, 2, 3})

    # ens_gele.add(4) # Lèverait une AttributeError

    # Peut être utilisé comme clé de dictionnaire
    mon_dict = {ens_gele: "Un frozenset comme clé"}
    print(mon_dict)  # Sortie : {frozenset({1, 2, 3}): 'Un frozenset comme clé'}

Les frozensets supportent toutes les opérations et méthodes des ensembles qui ne modifient pas l'ensemble (comme union, intersection, `issubset()`, etc.).

----------------------------------------------------

Mini-Projet : Compteur de Fréquence des Mots
====================================

Utilisons un dictionnaire pour compter la fréquence des mots dans un texte donné.

**Objectif :**
1.  Prendre une chaîne de texte en entrée.
2.  Traiter le texte :
    *   Le convertir en minuscules pour traiter "Le" et "le" comme le même mot.
    *   Supprimer la ponctuation courante (par ex., points, virgules) ou diviser les mots efficacement.
3.  Compter les occurrences de chaque mot.
4.  Afficher les fréquences des mots.

**Étapes :**

1.  Définir une chaîne de texte d'exemple.
2.  Initialiser un dictionnaire vide, disons `frequences_mots`.
3.  Prétraiter le texte :
    *   Convertir tout le texte en minuscules en utilisant `texte.lower()`.
    *   Réfléchir à la manière de gérer la ponctuation. Une méthode simple consiste à remplacer les signes de ponctuation courants par des espaces, puis à diviser par espace. Des méthodes plus robustes impliquent les expressions régulières (qui dépassent le cadre de ce module mais sont bonnes à connaître pour l'avenir). Pour simplifier, nous pouvons itérer sur les caractères et construire les mots.
    *   Diviser le texte en une liste de mots (par ex., en utilisant `texte.split()`).
4.  Itérer sur la liste de mots :
    *   Pour chaque `mot` :
        *   Si le `mot` est déjà une clé dans `frequences_mots`, incrémenter sa valeur.
        *   Si le `mot` n'est pas dans `frequences_mots`, l'ajouter comme nouvelle clé avec une valeur de 1.
        *   (Alternativement, utiliser `frequences_mots.get(mot, 0) + 1`)
5.  Après avoir traité tous les mots, itérer sur le dictionnaire `frequences_mots` et afficher chaque mot et sa fréquence.

**Texte d'Exemple :**
"Ceci est un texte d'exemple. Ce texte est pour tester le compteur de fréquence des mots."

**Sortie Attendue (l'ordre peut varier) :**

.. code-block:: text

    ceci: 2
    est: 2
    un: 1
    texte: 2
    d'exemple: 1
    ce: 1
    pour: 1
    tester: 1
    le: 1
    compteur: 1
    de: 1
    fréquence: 1
    des: 1
    mots: 1

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # compteur_frequence_mots.py
       import string # Pour aider avec la ponctuation

       def compter_frequences_mots(texte):
           frequences_mots = {}
           # Convertir en minuscules
           texte = texte.lower()

           # Supprimer la ponctuation (approche simple)
           # Créer une table de traduction pour supprimer la ponctuation
           traducteur = str.maketrans('', '', string.punctuation)
           texte_sans_ponctuation = texte.translate(traducteur)

           # Diviser en mots
           mots = texte_sans_ponctuation.split()

           for mot in mots:
               if mot: # S'assurer que le mot n'est pas vide après la division
                   frequences_mots[mot] = frequences_mots.get(mot, 0) + 1
           return frequences_mots

       # Exemple d'utilisation
       texte_exemple = "Ceci est un texte d'exemple. Ce texte est pour tester le compteur de fréquence des mots et ce compteur fonctionne !"
       # (Note: The word "d'exemple" will be treated as "dexemple" after punctuation removal with this simple method.
       # More sophisticated NLP techniques would handle apostrophes better, for example by splitting on whitespace
       # and then cleaning each token, or by using regex for splitting.)

       frequences = compter_frequences_mots(texte_exemple)

       print("Fréquences des Mots :")
       for mot, compte in frequences.items():
           print(f"{mot}: {compte}")

       # Exemple d'utilisation d'un ensemble pour trouver les mots uniques
       # texte_sans_ponctuation = texte_exemple.lower().translate(str.maketrans('', '', string.punctuation))
       # mots_uniques = set(texte_sans_ponctuation.split())
       # print(f"\nMots uniques : {mots_uniques}")
       # print(f"Nombre de mots uniques : {len(mots_uniques)}")

----------------------------------------------------

Résumé du Module 4
================

Félicitations pour avoir terminé le Module 4 ! Vous avez acquis des connaissances sur deux autres structures de données Python fondamentales :

*   Les **Dictionnaires (`dict`)** stockent les données sous forme de **paires clé-valeur**, permettant une récupération, une modification et une organisation efficaces des données lorsque vous avez des identifiants uniques pour vos données.
*   Les **Ensembles (`set`)** sont des collections non ordonnées d'**éléments uniques**. Ils sont excellents pour des tâches telles que la suppression de doublons, la vérification rapide de l'appartenance et l'exécution d'opérations mathématiques sur les ensembles (union, intersection, etc.).
*   Vous avez également découvert les **frozensets**, l'équivalent immuable des ensembles, utiles lorsqu'un ensemble immuable est requis (par ex., comme clés de dictionnaire).
*   Comprendre les caractéristiques des dictionnaires (non ordonnés, accès par clé) et des ensembles (non ordonnés, éléments uniques) vous aide à choisir le bon outil pour divers problèmes de programmation.

Ces structures élargissent votre capacité à modéliser et à manipuler des relations de données complexes en Python.

Ensuite, nous aborderons un aspect crucial de l'écriture de programmes plus volumineux et mieux organisés : les **fonctions** : :ref:`module5-functions-fr` !