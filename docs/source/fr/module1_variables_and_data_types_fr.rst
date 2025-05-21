.. _module1-variables-and-data-types-fr:

====================================================================
Module 1 : Variables, Types de Données et Entrées Utilisateur
====================================================================

Bienvenue dans le Module 1 ! Maintenant que vous êtes configuré et que vous avez écrit votre premier programme Python, il est temps de plonger dans la manière dont Python gère les données. Nous explorerons les variables (comment stocker des informations) et les différents types de données que vous rencontrerez. Nous apprendrons également comment rendre vos programmes interactifs en obtenant des entrées de l'utilisateur.

.. image:: /_static/images/data_blocks.png
   :alt: Blocs colorés représentant différents types de données
   :width: 250px
   :align: center


Objectifs d'apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Comprendre ce que sont les variables et pourquoi elles sont utilisées.
*   Déclarer et affecter des valeurs aux variables en Python.
*   Suivre les règles et conventions de nommage de Python pour les variables.
*   Identifier et utiliser les types de données Python fondamentaux :
    *   Entiers (`int`)
    *   Nombres à virgule flottante (`float`)
    *   Chaînes de caractères (`str`)
    *   Booléens (`bool`)
*   Utiliser la fonction `type()` pour déterminer le type de données d'une variable.
*   Effectuer des opérations de base avec les nombres et les chaînes de caractères (concaténation, f-strings).
*   Convertir des données d'un type à un autre (conversion de type).
*   Obtenir une entrée d'un utilisateur à l'aide de la fonction `input()`.

----------------------------------------------------

Que sont les Variables ?
===================

En programmation, une **variable** est comme un conteneur étiqueté ou une boîte où vous pouvez stocker une information (donnée). Vous donnez un nom à la variable, et ensuite vous pouvez vous référer à la donnée par ce nom. Cela rend votre code beaucoup plus lisible et flexible.

Imaginez que vous calculez l'aire d'un rectangle. Au lieu d'écrire `5 * 10` partout, vous pourriez stocker la longueur et la largeur dans des variables :

.. code-block:: python

    longueur = 10
    largeur = 5
    aire = longueur * largeur
    print(aire) # Sortie : 50

Si vous avez besoin de changer la longueur ou la largeur, vous n'avez qu'à la modifier à un seul endroit (là où la variable est affectée), et le reste de votre code qui utilise cette variable utilisera automatiquement la nouvelle valeur.

Affectation de Valeurs aux Variables
-----------------------------

En Python, vous créez une variable et lui affectez une valeur en utilisant le signe égal (`=`):

.. code-block:: python

    # nom_variable = valeur
    mon_age = 30
    nom_utilisateur = "Alice"
    valeur_pi = 3.14159
    est_en_apprentissage = True

    print(mon_age)
    print(nom_utilisateur)
    print(valeur_pi)
    print(est_en_apprentissage)

*   `mon_age` est une variable stockant un entier.
*   `nom_utilisateur` est une variable stockant une séquence de caractères (une chaîne de caractères).
*   `valeur_pi` est une variable stockant un nombre avec un point décimal.
*   `est_en_apprentissage` est une variable stockant une valeur de vérité (Booléen).

Vous pouvez changer la valeur d'une variable en la réaffectant :

.. code-block:: python

    x = 10
    print(x) # Sortie : 10
    x = 20
    print(x) # Sortie : 20

Règles et Conventions de Nommage des Variables
-------------------------------------

Python a des règles pour nommer les variables :

*   **Doit commencer par une lettre (a-z, A-Z) ou un tiret bas (`_`).**
*   Ne peut pas commencer par un chiffre.
*   Peut uniquement contenir des caractères alphanumériques (a-z, A-Z, 0-9) et des tirets bas.
*   Les noms de variables sont **sensibles à la casse** (`age`, `Age`, et `AGE` sont trois variables différentes).

**Conventions (Meilleures pratiques) :**

*   Utilisez des **minuscules avec les mots séparés par des tirets bas** (ceci est appelé `snake_case`).
    *   Bien : `user_name`, `first_name`, `total_amount`
    *   Non recommandé (mais valide) : `UserName`, `firstname`, `TotalAmount`
*   Choisissez des noms significatifs et descriptifs.
    *   Bien : `student_gpa` (ou `moyenne_etudiant` si vous préférez traduire les noms de variables dans les explications)
    *   Mauvais : `x`, `val`, `sg` (sauf si le contexte est très clair)
*   Évitez d'utiliser les mots-clés Python (comme `print`, `if`, `for`, `while`, `True`, `False`, `None`, etc.) comme noms de variables. Votre éditeur pourrait les surligner.

----------------------------------------------------

Types de Données Fondamentaux
======================

Python possède plusieurs types de données intégrés. Examinons les plus courants.

Entiers (int)
--------------
Les entiers sont des nombres entiers, positifs ou négatifs, sans décimales.

.. code-block:: python

    compteur = 10
    nombre_negatif = -5
    zero = 0
    print(type(compteur)) # Sortie : <class 'int'>

Nombres à Virgule Flottante (float)
------------------------------
Les flottants (floats) représentent des nombres réels et sont écrits avec un point décimal.

.. code-block:: python

    prix = 19.99
    temperature = -3.5
    gravite = 9.8
    print(type(prix)) # Sortie : <class 'float'>

Chaînes de Caractères (str)
-------------
Les chaînes de caractères (strings) représentent des séquences de caractères (texte). Elles sont définies en utilisant soit des guillemets simples (`'...'`) soit des guillemets doubles (`"..."`).

.. code-block:: python

    message = "Bonjour, apprenants Python !"
    nom = 'Guido van Rossum'
    chaine_vide = ""

    print(type(message)) # Sortie : <class 'str'>

    # Vous pouvez utiliser des guillemets à l'intérieur des chaînes s'ils sont différents de ceux qui les encadrent :
    citation1 = "Il a dit, 'Python c'est amusant !'"
    citation2 = 'Elle a répondu, "En effet, ça l\'est."'

    # Pour les chaînes multi-lignes, utilisez des triples guillemets ('''...''' ou """...""") :
    texte_multi_lignes = """Ceci est une
    chaîne qui s'étend
    sur plusieurs lignes."""
    print(texte_multi_lignes)

Booléens (bool)
---------------
Les booléens représentent l'une des deux valeurs : `True` ou `False`. Ils sont cruciaux pour prendre des décisions dans votre code (ce que nous aborderons plus tard). Notez la majuscule.

.. code-block:: python

    est_actif = True
    a_la_permission = False
    print(type(est_actif)) # Sortie : <class 'bool'>

Vérification des Types de Données avec `type()`
---------------------------------
Vous pouvez utiliser la fonction intégrée `type()` pour découvrir le type de données d'une variable ou d'une valeur.

.. code-block:: python

    num = 42
    salutation = "Salut"
    pi = 3.14
    est_valide = True

    print(type(num))        # Sortie : <class 'int'>
    print(type(salutation))   # Sortie : <class 'str'>
    print(type(pi))         # Sortie : <class 'float'>
    print(type(est_valide))   # Sortie : <class 'bool'>
    print(type(2.0 + 5))    # Que pensez-vous que cela sera ? (Indice : <class 'float'>)

----------------------------------------------------

Travailler avec les Données
=================

Opérations de Base
----------------

**Avec les Nombres (int, float) :**
Python supporte les opérations arithmétiques standards :

.. code-block:: python

    a = 10
    b = 3

    sum_val = a + b        # Addition : 13
    diff_val = a - b       # Soustraction : 7
    prod_val = a * b       # Multiplication : 30
    div_val = a / b        # Division réelle : 3.333...
    floor_div_val = a // b # Division entière (élimine le reste) : 3
    mod_val = a % b        # Modulo (reste) : 1
    exp_val = a ** b       # Exponentiation (a à la puissance b) : 1000

    print(f"Somme : {sum_val}")
    print(f"Division réelle : {div_val}")
    print(f"Division entière : {floor_div_val}")
    print(f"Modulo : {mod_val}")

.. note::
   Lorsque vous effectuez une opération avec un `int` et un `float`, le résultat est généralement un `float`.
   Exemple : `5 + 2.0` donne `7.0`.

**Avec les Chaînes de Caractères :**

*   **Concaténation (joindre des chaînes) :** Utilisez l'opérateur `+`.
    .. code-block:: python

        prenom = "Ada"
        nom_famille = "Lovelace"
        nom_complet = prenom + " " + nom_famille
        print(nom_complet) # Sortie : Ada Lovelace

*   **Répétition de chaîne :** Utilisez l'opérateur `*`.
    .. code-block:: python

        separateur = "-" * 10
        print(separateur) # Sortie : ----------

*   **f-strings (Chaînes de caractères formatées littérales) :** Un moyen puissant et pratique d'intégrer des expressions à l'intérieur de chaînes de caractères littérales. C'est généralement la manière privilégiée de formater les chaînes.
    .. code-block:: python

        name = "Charlie"
        age = 7
        # Ancienne méthode (concaténation, peut être fastidieux)
        # greeting_old_way = "My dog's name is " + name + " and he is " + str(age) + " years old."

        # Nouvelle méthode (f-string)
        greeting = f"My dog's name is {name} and he is {age} years old."
        print(greeting) # Sortie : My dog's name is Charlie and he is 7 years old.

    Vous placez un `f` ou `F` avant le guillemet ouvrant, puis vous pouvez mettre des variables ou des expressions entre accolades `{}`.

Conversion de Type (Transtypage)
-------------------------
Parfois, vous devez convertir une valeur d'un type de données à un autre. C'est ce qu'on appelle la conversion de type (ou transtypage).

*   `int(valeur)` : Convertit `valeur` en un entier.
*   `float(valeur)` : Convertit `valeur` en un nombre à virgule flottante.
*   `str(valeur)` : Convertit `valeur` en une chaîne de caractères.

.. code-block:: python

    chaine_nombre = "100"
    # print(chaine_nombre + 5) # Ceci causerait une TypeError ! Impossible d'additionner une chaîne et un entier.

    nombre_entier = int(chaine_nombre)
    print(nombre_entier + 5) # Sortie : 105

    nombre_flottant = float(chaine_nombre)
    print(nombre_flottant) # Sortie : 100.0

    nombre = 42
    nombre_en_chaine = str(nombre)
    print("Le nombre est : " + nombre_en_chaine) # "Le nombre est : 42"

    # Attention :
    # int("bonjour") # Ceci causerait une ValueError car "bonjour" ne peut pas être converti en entier.
    # int("3.14")  # Ceci causerait aussi une ValueError. Utilisez d'abord float("3.14").
    print(int(float("3.14"))) # Sortie : 3

----------------------------------------------------

Obtenir des Entrées Utilisateur avec `input()`
=================================

Les programmes ont souvent besoin d'obtenir des informations de l'utilisateur. La fonction `input()` de Python vous permet de le faire. Elle invite l'utilisateur à taper quelque chose et renvoie ensuite ce qu'il a tapé sous forme de **chaîne de caractères**.

.. code-block:: python

    nom_utilisateur = input("Veuillez entrer votre nom : ")
    print(f"Bonjour, {nom_utilisateur} !")

    # La fonction input() renvoie TOUJOURS une chaîne de caractères.
    age_str = input("Veuillez entrer votre âge : ")
    print(type(age_str)) # Sortie : <class 'str'>

    # Si vous avez besoin de l'âge en tant que nombre, vous devez le convertir :
    try:
        age_num = int(age_str)
        age_an_prochain = age_num + 1
        print(f"L'année prochaine, vous aurez {age_an_prochain} ans.")
    except ValueError:
        print("Âge invalide saisi. Veuillez entrer un nombre.")

.. tip::
   Le bloc `try-except` dans l'exemple ci-dessus est un moyen de gérer les erreurs potentielles (comme l'utilisateur tapant "dix" au lieu de "10" pour son âge). Nous aborderons la gestion des erreurs plus en détail ultérieurement, mais il est bon de le voir en contexte.

----------------------------------------------------

Mini-projet : Collecteur d'Informations Simple
===================================

Mettons en pratique ce que vous avez appris.

**Objectif :** Écrire un programme Python qui :
1.  Demande à l'utilisateur son nom.
2.  Demande à l'utilisateur son âge.
3.  Demande à l'utilisateur son loisir préféré.
4.  Affiche un message récapitulatif en utilisant une f-string, comme :
    "Bonjour [Nom] ! Vous avez [Âge] ans, et vous aimez [Loisir]. C'est cool !"

**Exemple d'interaction :**

.. code-block:: text

    Veuillez entrer votre nom : Bob
    Veuillez entrer votre âge : 25
    Quel est votre loisir préféré ? Coder
    Bonjour Bob ! Vous avez 25 ans, et vous aimez Coder. C'est cool !

**Étapes :**

1.  Créez un nouveau fichier (par ex., `collecteur_infos.py`).
2.  Utilisez `input()` pour obtenir le nom, l'âge et le loisir. Stockez-les dans des variables.
3.  Rappelez-vous que `input()` renvoie des chaînes de caractères. Si vous prévoyez de faire des calculs avec l'âge (bien que non requis pour la sortie de ce projet spécifique), vous devrez le convertir en `int`. Pour ce projet, l'utiliser comme chaîne dans la f-string est suffisant.
4.  Utilisez une f-string et `print()` pour afficher le message récapitulatif.
5.  Enregistrez et exécutez votre programme.

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # collecteur_infos.py
       # Ce programme collecte des informations auprès de l'utilisateur et affiche un résumé.

       # 1. Demander le nom
       user_name = input("Veuillez entrer votre nom : ")

       # 2. Demander l'âge
       user_age_str = input("Veuillez entrer votre âge : ")
       # Pour ce projet, nous pouvons conserver l'âge sous forme de chaîne pour la sortie.
       # Si nous avions besoin de faire des calculs, nous le convertirions :
       # user_age_int = int(user_age_str)

       # 3. Demander le loisir préféré
       user_hobby = input("Quel est votre loisir préféré ? ")

       # 4. Afficher le message récapitulatif en utilisant une f-string
       summary_message = f"Bonjour {user_name} ! Vous avez {user_age_str} ans, et vous aimez {user_hobby}. C'est cool !"
       print(summary_message)

----------------------------------------------------

Résumé du Module 1
================

Excellent travail ! Vous avez parcouru beaucoup de chemin dans ce module :

*   Les **variables** sont des conteneurs nommés pour stocker des données.
*   Vous avez appris à **nommer les variables** en suivant les règles et conventions de Python (`snake_case`).
*   Vous avez été initié aux **types de données** fondamentaux : `int`, `float`, `str`, et `bool`.
*   La fonction `type()` aide à identifier le type de données d'une variable.
*   Vous pouvez effectuer des **opérations de base** sur les nombres et les chaînes de caractères, les **f-strings** étant un excellent moyen de formater la sortie.
*   La **conversion de type** (`int()`, `float()`, `str()`) vous permet de convertir entre les types de données.
*   La fonction `input()` permet à vos programmes de devenir **interactifs** en obtenant des données de l'utilisateur (en se rappelant qu'elle renvoie toujours une chaîne de caractères).

Ces concepts sont les éléments de base de presque tout ce que vous ferez en Python. Avec les variables et les types de données, vous pouvez commencer à représenter et à manipuler des informations du monde réel dans vos programmes.

Prochaine étape, nous apprendrons comment contrôler le flux de nos programmes et prendre des décisions en utilisant :ref:`module2-control-flow-fr` !