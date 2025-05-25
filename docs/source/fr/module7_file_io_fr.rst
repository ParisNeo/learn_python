.. _module7-file-io-fr:

=================================================================================
Module 7 : Entrées/Sorties de Fichiers - Interaction avec le Stockage de Données
=================================================================================

Bienvenue dans le Module 7 ! Jusqu'à présent, nos programmes ont fonctionné avec des données qui n'existent que pendant l'exécution du programme. Une fois le programme terminé, toutes les données générées ou modifiées sont perdues. Pour rendre les données **persistantes** — c'est-à-dire qu'elles restent disponibles même après la fin du programme — nous devons les stocker dans des **fichiers**. Les **Entrées/Sorties de Fichiers (E/S)** désignent le processus de lecture de données depuis des fichiers et d'écriture de données dans des fichiers sur un périphérique de stockage (comme un disque dur). Cela permet à vos programmes de sauvegarder leur état, de traiter de grands ensembles de données et d'interagir avec d'autres programmes.

.. image:: ../_static/images/file_io_concept.png
   :alt: Un ordinateur lisant et écrivant dans un document fichier
   :width: 650px
   :align: center

Objectifs d'Apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Comprendre l'importance des E/S de fichiers pour la persistance des données.
*   Ouvrir des fichiers dans différents modes (lecture, écriture, ajout, etc.) en utilisant la fonction `open()`.
*   Comprendre l'importance de fermer les fichiers et comment utiliser l'instruction `with` pour la gestion automatique des ressources.
*   Lire des données à partir de fichiers texte en utilisant des méthodes comme `read()`, `readline()`, et `readlines()`.
*   Itérer sur le contenu d'un fichier ligne par ligne.
*   Écrire des données dans des fichiers texte en utilisant `write()` et `writelines()`.
*   Comprendre la différence entre l'écrasement et l'ajout de contenu dans les fichiers.
*   Gérer les exceptions courantes liées aux fichiers comme `FileNotFoundError` et `PermissionError`.
*   Comprendre brièvement le fonctionnement des chemins de fichiers et utiliser les fonctions de base de `os.path`.
*   Avoir un aperçu du travail avec des formats de fichiers structurés comme CSV et JSON (bien qu'une exploration détaillée interviendra plus tard).

----------------------------------------------------

Qu'est-ce que les E/S de Fichiers ?
===================================

Les **Entrées/Sorties de Fichiers (E/S)** font référence aux opérations qui permettent à un programme de lire des données d'un fichier (entrée) ou d'écrire des données dans un fichier (sortie). Les fichiers sont stockés sur des périphériques de stockage secondaires (disques durs, SSD, clés USB, etc.) et offrent un moyen de conserver les données au-delà de la durée d'exécution d'un seul programme.

Types de Fichiers
-----------------
Globalement, les fichiers peuvent être classés en :

1.  **Fichiers Texte :**
    *   Stockent les données sous forme de séquences de caractères lisibles par l'homme (texte).
    *   Exemples : `.txt`, `.py` (scripts Python), `.html`, `.csv`.
    *   Chaque ligne se termine généralement par un caractère de nouvelle ligne (`\n`).
    *   Python gère automatiquement l'encodage et le décodage des caractères dans la plupart des cas (UTF-8 est un encodage par défaut courant).

2.  **Fichiers Binaires :**
    *   Stockent les données sous forme de séquences brutes d'octets, exactement telles qu'elles sont en mémoire informatique.
    *   Non directement lisibles par l'homme avec un simple éditeur de texte.
    *   Exemples : `.jpg` (images), `.mp3` (audio), `.exe` (exécutables), code compilé, fichiers de base de données.
    *   Nécessitent une connaissance spécifique du format de fichier pour être interprétés correctement.

Ce module se concentrera principalement sur les **fichiers texte**, car ils sont courants et plus faciles à aborder pour commencer.

----------------------------------------------------

Ouvrir et Fermer des Fichiers
=============================

Avant de pouvoir lire ou écrire dans un fichier, vous devez d'abord l'**ouvrir**. La fonction intégrée `open()` de Python est utilisée à cet effet.

La fonction `open()`
--------------------
Syntaxe : `objet_fichier = open(nom_fichier, mode, encoding=None)`

*   `nom_fichier` : Une chaîne représentant le nom (et le chemin) du fichier.
*   `mode` : Une chaîne spécifiant comment le fichier doit être ouvert. C'est crucial.
*   `encoding` (optionnel) : Spécifie l'encodage à utiliser pour les fichiers texte (par ex., `"utf-8"`, `"ascii"`). Il est de bonne pratique de spécifier `utf-8` pour une compatibilité plus large, bien que Python puisse l'utiliser par défaut selon votre système.

Modes de Fichier Courants :
--------------------------
*   `'r'` : **Mode lecture (par défaut).** Ouvre le fichier en lecture. Lève une erreur si le fichier n'existe pas.
*   `'w'` : **Mode écriture.** Ouvre le fichier en écriture.
    *   Si le fichier existe, son contenu est **tronqué (effacé)**.
    *   Si le fichier n'existe pas, il est **créé**.
*   `'a'` : **Mode ajout.** Ouvre le fichier en écriture.
    *   Les données sont ajoutées à la **fin du fichier** s'il existe.
    *   Si le fichier n'existe pas, il est **créé**.
*   `'x'` : **Mode création exclusive.** Crée un nouveau fichier et l'ouvre en écriture. Lève une erreur si le fichier existe déjà.
*   `'b'` : **Mode binaire.** Peut être ajouté à d'autres modes (par ex., `'rb'`, `'wb'`). Traite le fichier comme un fichier binaire.
*   `'+'` : **Mode mise à jour (lecture et écriture).** Peut être ajouté à d'autres modes (par ex., `'r+'`, `'w+'`, `'a+'`).

Exemple :
.. code-block:: python

    # Ouvrir un fichier en lecture
    # f = open("monfichier.txt", "r")

    # Ouvrir un fichier en écriture (crée s'il n'existe pas, tronque s'il existe)
    # f = open("sortie.txt", "w")

    # Ouvrir un fichier en mode ajout
    # f = open("log.txt", "a")

Fermeture des Fichiers : `objet_fichier.close()`
------------------------------------------------
Une fois que vous avez terminé de travailler avec un fichier, il est très important de le **fermer** en utilisant la méthode `close()` de l'objet fichier.

.. code-block:: python

    fichier = open("exemple.txt", "w")
    # ... effectuer des opérations sur le fichier ...
    fichier.write("Bonjour de Python !\n")
    fichier.close() # Essentiel pour s'assurer que les données sont écrites et les ressources libérées

Pourquoi fermer les fichiers ?
*   **Mise en Tampon des Données :** Lorsque vous écrivez dans un fichier, les données peuvent être temporairement stockées dans un tampon. La fermeture du fichier garantit que toutes les données du tampon sont écrites sur le disque (vidées).
*   **Gestion des Ressources :** Les systèmes d'exploitation ont une limite au nombre de fichiers qu'un programme peut avoir ouverts simultanément. La fermeture des fichiers libère ces ressources.
*   **Verrouillage de Fichier :** Sur certains systèmes, un fichier ouvert peut être verrouillé, empêchant d'autres programmes (ou même d'autres parties de votre programme) d'y accéder.

L'Instruction `with` (Gestionnaire de Contexte)
----------------------------------------------
Oublier de fermer les fichiers est une source courante de bogues et de fuites de ressources. Python offre un moyen plus élégant et plus sûr de gérer les fichiers en utilisant l'instruction `with`, également connue sous le nom de gestionnaire de contexte.

L'instruction `with` s'occupe automatiquement de la fermeture du fichier, même si des erreurs se produisent dans le bloc.

.. code-block:: python

    # Manière préférée d'ouvrir et de travailler avec les fichiers
    try:
        with open("monfichier.txt", "w", encoding="utf-8") as f:
            f.write("Ceci est une ligne.\n")
            f.write("Une autre ligne utilisant l'instruction 'with'.\n")
            # Pas besoin d'appeler f.close() explicitement.
            # Elle est appelée automatiquement lorsque le bloc 'with' se termine.
        print("Données écrites dans monfichier.txt")
    except IOError as e:
        print(f"Une erreur d'E/S s'est produite : {e}")

C'est la manière recommandée de travailler avec les fichiers en Python.

----------------------------------------------------

Lire depuis des Fichiers
========================

Une fois qu'un fichier est ouvert en mode lecture (par ex., `'r'` ou `'r+'`), vous pouvez lire son contenu.

1.  `fichier.read(taille=-1)` :
    *   Lit et retourne une chaîne contenant jusqu'à `taille` octets/caractères du fichier.
    *   Si `taille` est omise ou négative, elle lit et retourne tout le contenu du fichier.
    *   Soyez prudent avec les fichiers très volumineux, car `read()` sans `taille` chargera tout le fichier en mémoire.

    .. code-block:: python

        try:
            with open("monfichier.txt", "r", encoding="utf-8") as f:
                contenu = f.read()
                print("--- Contenu Entier ---")
                print(contenu)
        except FileNotFoundError:
            print("Erreur : monfichier.txt non trouvé.")
        except IOError as e:
            print(f"Une erreur d'E/S s'est produite : {e}")

2.  `fichier.readline(taille=-1)` :
    *   Lit et retourne une seule ligne du fichier, y compris le caractère de nouvelle ligne (`\n`) à la fin.
    *   Si `taille` est spécifiée, elle lit au plus `taille` octets/caractères.
    *   Retourne une chaîne vide (`""`) si la fin du fichier (EOF) est atteinte.

    .. code-block:: python

        try:
            with open("monfichier.txt", "r", encoding="utf-8") as f:
                print("--- Lecture ligne par ligne ---")
                ligne1 = f.readline()
                print(f"Ligne 1 : {ligne1.strip()}") # .strip() supprime les espaces de début/fin comme \n
                ligne2 = f.readline()
                print(f"Ligne 2 : {ligne2.strip()}")
        except FileNotFoundError:
            print("Erreur : monfichier.txt non trouvé.")

3.  `fichier.readlines()` :
    *   Lit toutes les lignes restantes du fichier et les retourne sous forme de liste de chaînes.
    *   Chaque chaîne de la liste inclut le caractère de nouvelle ligne (`\n`).
    *   Comme `read()`, cela peut consommer beaucoup de mémoire pour les fichiers volumineux.

    .. code-block:: python

        try:
            with open("monfichier.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
                print("--- Toutes les lignes sous forme de liste ---")
                for i, ligne in enumerate(lignes):
                    print(f"Ligne de la liste {i} : {ligne.strip()}")
        except FileNotFoundError:
            print("Erreur : monfichier.txt non trouvé.")

4.  Itérer sur un Objet Fichier :
    C'est la manière la plus économe en mémoire de lire un fichier ligne par ligne, en particulier pour les fichiers volumineux, car elle ne charge pas tout le fichier en mémoire en une seule fois.

    .. code-block:: python

        try:
            with open("monfichier.txt", "r", encoding="utf-8") as f:
                print("--- Itération sur le fichier ---")
                for numero_ligne, ligne_actuelle in enumerate(f):
                    # ligne_actuelle inclut le caractère de nouvelle ligne
                    print(f"Ligne itérée {numero_ligne} : {ligne_actuelle.strip()}")
        except FileNotFoundError:
            print("Erreur : monfichier.txt non trouvé.")

----------------------------------------------------

Écrire dans des Fichiers
========================

Pour écrire des données dans un fichier, vous devez l'ouvrir en mode écriture (`'w'`, `'a'`, `'x'`) ou en mode mise à jour (`'+'`).

1.  `fichier.write(chaine)` :
    *   Écrit la `chaine` donnée dans le fichier.
    *   Elle n'ajoute **pas** automatiquement de caractère de nouvelle ligne. Vous devez inclure `\n` si vous voulez de nouvelles lignes.
    *   Retourne le nombre de caractères écrits.

    .. code-block:: python

        try:
            with open("sortie.txt", "w", encoding="utf-8") as f: # 'w' écrase ou crée
                f.write("Bonjour, monde des fichiers !\n")
                f.write("Ceci est la deuxième ligne.\n")
                nb_caracteres = f.write("Python c'est amusant.")
                print(f"{nb_caracteres} caractères écrits lors de la dernière écriture.")
            print("Données écrites dans sortie.txt")

            with open("sortie.txt", "a", encoding="utf-8") as f: # 'a' ajoute à la fin
                f.write("\nCette ligne est ajoutée.")
            print("Données ajoutées à sortie.txt")
        except IOError as e:
            print(f"Une erreur d'E/S s'est produite : {e}")

2.  `fichier.writelines(liste_de_chaines)` :
    *   Écrit une liste (ou tout itérable) de chaînes dans le fichier.
    *   Comme `write()`, elle n'ajoute **pas** de caractères de nouvelle ligne entre les chaînes. Vous devez vous assurer que vos chaînes dans la liste les contiennent déjà si désiré.

    .. code-block:: python

        lignes_a_ecrire = [
            "Première ligne pour writelines.\n",
            "Deuxième ligne.\n",
            "Et une troisième.\n"
        ]
        try:
            with open("writelines_exemple.txt", "w", encoding="utf-8") as f:
                f.writelines(lignes_a_ecrire)
            print("Données écrites avec writelines() dans writelines_exemple.txt")
        except IOError as e:
            print(f"Une erreur d'E/S s'est produite : {e}")

Écrasement vs. Ajout :
----------------------
*   **`'w'` (Mode écriture) :** Si le fichier existe, son contenu est complètement effacé avant l'écriture de nouvelles données. S'il n'existe pas, il est créé. Utilisez ceci lorsque vous voulez repartir de zéro.
*   **`'a'` (Mode ajout) :** Si le fichier existe, les nouvelles données sont ajoutées à la fin du contenu existant. S'il n'existe pas, il est créé. Utilisez ceci pour la journalisation ou l'ajout à des données existantes.

----------------------------------------------------

Travailler avec les Chemins de Fichiers
=======================================

Un **chemin de fichier** spécifie l'emplacement d'un fichier ou d'un répertoire dans un système de fichiers.

*   **Chemin Absolu :** Spécifie l'emplacement à partir de la racine du système de fichiers (par ex., `C:\Utilisateurs\VotreNom\Documents\fichier.txt` sous Windows, ou `/home/votrenom/documents/fichier.txt` sous Linux/macOS).
*   **Chemin Relatif :** Spécifie l'emplacement par rapport au répertoire de travail actuel de votre script (par ex., `donnees/fichier.txt` ou `../images/photo.jpg`).

Le Module `os`
--------------
Le module `os` de Python fournit des fonctions pour interagir avec le système d'exploitation, y compris la manipulation des chemins. Le sous-module `os.path` est particulièrement utile.

.. code-block:: python

    import os

    # Obtenir le répertoire de travail actuel
    rdc = os.getcwd()
    print(f"Répertoire de Travail Actuel : {rdc}")

    # Construire un chemin de manière indépendante du SE
    nom_fichier = "mes_notes.txt"
    chemin_fichier = os.path.join(rdc, "dossier_notes", nom_fichier) # Bonne pratique !
    print(f"Chemin de Fichier Construit : {chemin_fichier}")

    # Vérifier si un fichier ou un répertoire existe
    if os.path.exists(chemin_fichier):
        print(f"'{chemin_fichier}' existe.")
    else:
        print(f"'{chemin_fichier}' n'existe pas.")
        # Vous pourriez vouloir créer le répertoire s'il n'existe pas
        # os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True) # Crée les répertoires parents si nécessaire

    # Obtenir la partie répertoire d'un chemin
    nom_repertoire = os.path.dirname(chemin_fichier)
    print(f"Partie répertoire : {nom_repertoire}")

    # Obtenir le nom de base (fichier ou dernier répertoire)
    nom_base = os.path.basename(chemin_fichier)
    print(f"Nom de base : {nom_base}")

Le Module `pathlib` (Alternative Moderne)
----------------------------------------
Python 3.4+ a introduit le module `pathlib`, qui offre une approche orientée objet des chemins de fichiers. Il est souvent considéré comme plus pratique et Pythonique.

.. code-block:: python

    from pathlib import Path

    # Répertoire de travail actuel
    chemin_rdc = Path.cwd()
    print(f"Chemin Actuel (pathlib) : {chemin_rdc}")

    # Construction de chemins avec l'opérateur /
    fichier_p = chemin_rdc / "dossier_notes" / "mes_notes.txt"
    print(f"Chemin Construit (pathlib) : {fichier_p}")

    # Vérifier l'existence
    if fichier_p.exists():
        print(f"'{fichier_p}' existe (pathlib).")
    else:
        print(f"'{fichier_p}' n'existe pas (pathlib).")
        # Créer les répertoires parents s'ils n'existent pas lors de l'écriture
        # fichier_p.parent.mkdir(parents=True, exist_ok=True)


    # Obtenir des parties du chemin
    print(f"Répertoire parent (pathlib) : {fichier_p.parent}")
    print(f"Nom de fichier (pathlib) : {fichier_p.name}")
    print(f"Racine du fichier (nom sans suffixe) (pathlib) : {fichier_p.stem}")
    print(f"Suffixe du fichier (extension) (pathlib) : {fichier_p.suffix}")

    # Lecture de texte (pathlib simplifie les lectures/écritures simples)
    # try:
    #    contenu = fichier_p.read_text(encoding="utf-8")
    #    print(contenu)
    # except FileNotFoundError:
    #    print(f"{fichier_p} non trouvé.")

    # Écriture de texte
    # try:
    #    fichier_p.parent.mkdir(parents=True, exist_ok=True) # S'assurer que le répertoire existe
    #    fichier_p.write_text("Bonjour de pathlib !", encoding="utf-8")
    #    print(f"Écrit dans {fichier_p}")
    # except IOError as e:
    #    print(f"Erreur d'écriture avec pathlib : {e}")

Pour ce module, `open()` basique avec des chemins de chaînes est suffisant, mais `pathlib` est bon à connaître pour une gestion plus complexe des chemins.

----------------------------------------------------

Gestion des Erreurs dans les Opérations sur les Fichiers
======================================================

Les opérations sur les fichiers sont sujettes aux erreurs. Par exemple :
*   `FileNotFoundError` : Se produit si vous essayez d'ouvrir un fichier en mode lecture (`'r'`) qui n'existe pas.
*   `PermissionError` : Se produit si vous n'avez pas les permissions nécessaires pour lire ou écrire dans un fichier/répertoire.
*   `IsADirectoryError` / `NotADirectoryError` : Essayer de traiter un répertoire comme un fichier ou vice-versa.
*   `IOError` : Une erreur d'E/S générale (peut être une classe de base pour d'autres comme `FileNotFoundError`).

Encadrez toujours les opérations sur les fichiers dans des blocs `try...except`.

.. code-block:: python

    fichier_a_lire = "fichier_inexistant.txt"
    try:
        with open(fichier_a_lire, "r", encoding="utf-8") as f:
            donnees = f.read()
            print(donnees)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier_a_lire}' n'a pas été trouvé.")
    except PermissionError:
        print(f"Erreur : Vous n'avez pas la permission de lire '{fichier_a_lire}'.")
    except IOError as e: # Attrape d'autres erreurs liées aux E/S
        print(f"Une erreur d'E/S s'est produite : {e}")
    except Exception as e: # Attrape toute autre erreur inattendue
        print(f"Une erreur inattendue s'est produite : {e}")

----------------------------------------------------

Brève Introduction aux Formats de Fichiers Structurés
=====================================================

Bien que ce module se concentre sur les fichiers texte bruts, de nombreuses applications utilisent des formats de fichiers structurés pour stocker les données de manière plus organisée. Deux formats très courants sont :

1.  **CSV (Comma-Separated Values / Valeurs Séparées par des Virgules) :**
    *   Un format de fichier texte où les données sont stockées sous forme tabulaire.
    *   Chaque ligne représente une rangée, et les valeurs au sein d'une rangée sont séparées par des virgules (ou d'autres délimiteurs comme des tabulations ou des points-virgules).
    *   Le module `csv` de Python aide à lire et écrire facilement des fichiers CSV.

    Exemple `donnees.csv` :
    ```csv
    Nom,Age,Ville
    Alice,30,New York
    Bob,24,Paris
    Charlie,35,Londres
    ```

2.  **JSON (JavaScript Object Notation) :**
    *   Un format d'échange de données textuel léger.
    *   Lisible par l'homme et facile à analyser et à générer par les machines.
    *   Utilise une structure similaire aux dictionnaires Python (paires clé-valeur) et aux listes.
    *   Le module `json` de Python est utilisé pour encoder des objets Python en chaînes/fichiers JSON et pour décoder du JSON en objets Python.

    Exemple `donnees.json` :
    ```json
    {
      "nom": "Alice",
      "age": 30,
      "ville": "New York",
      "estEtudiant": false,
      "cours": [
        {"titre": "Histoire", "credits": 3},
        {"titre": "Maths", "credits": 4}
      ]
    }
    ```

Nous explorerons ces formats plus en détail dans des modules ultérieurs ou des sujets avancés. Pour l'instant, la compréhension des E/S de fichiers texte de base est fondamentale.

----------------------------------------------------

Mini-Projet : Gestionnaire Simple de Liste de Tâches
===================================================

Créons un gestionnaire de liste de tâches en ligne de commande qui sauvegarde les tâches dans un fichier texte (`todo.txt`). Chaque tâche sera sur une nouvelle ligne.

**Fonctionnalités :**
1.  **Ajouter une tâche :** Demande à l'utilisateur une tâche et l'ajoute à `todo.txt`.
2.  **Voir les tâches :** Lit `todo.txt` et affiche toutes les tâches numérotées.
3.  **Supprimer une tâche :** Affiche les tâches numérotées, demande à l'utilisateur laquelle supprimer et met à jour `todo.txt`.
4.  **Quitter :** Sauvegarde les modifications et quitte le programme.
5.  Le programme doit charger les tâches existantes de `todo.txt` à son démarrage.

**Structure du Fichier (`todo.txt`) :**
```
Faire les courses
Payer les factures
Appeler maman
```

**Étapes :**

1.  **Fonction `charger_taches(nom_fichier)` :**
    *   Prend `nom_fichier` en entrée.
    *   Essaie d'ouvrir et de lire les tâches du fichier. Chaque ligne est une tâche.
    *   Retourne une liste de tâches.
    *   Si le fichier n'existe pas, elle doit retourner une liste vide (et peut-être afficher un message indiquant qu'un nouveau fichier sera créé). Gérer `FileNotFoundError`.
2.  **Fonction `sauvegarder_taches(nom_fichier, taches)` :**
    *   Prend `nom_fichier` et une `liste` de `taches` en entrée.
    *   Ouvre le fichier en mode écriture (`'w'`) et écrit chaque tâche sur une nouvelle ligne. Gérer une `IOError` potentielle.
3.  **Fonction `ajouter_tache(taches, description)` :**
    *   Ajoute la `description` à la liste `taches`.
4.  **Fonction `voir_taches(taches)` :**
    *   Si `taches` est vide, affiche "Aucune tâche dans la liste."
    *   Sinon, affiche les tâches avec une numérotation commençant à 1.
5.  **Fonction `supprimer_tache(taches, numero_tache)` :**
    *   Prend la liste `taches` et un `numero_tache` (basé sur 1) à supprimer.
    *   Valide `numero_tache`. Si valide, supprime la tâche. Si invalide, affiche une erreur.
6.  **Boucle Principale du Programme (fonction `main`) :**
    *   Définir `NOM_FICHIER_TODO = "todo.txt"`.
    *   Charger les tâches en utilisant `charger_taches()`.
    *   Utiliser une boucle `while True` pour afficher un menu :
        ```
        Gestionnaire de Liste de Tâches
        1. Ajouter une Tâche
        2. Voir les Tâches
        3. Supprimer une Tâche
        4. Quitter
        Entrez votre choix :
        ```
    *   En fonction du choix de l'utilisateur, appeler les fonctions appropriées.
    *   Pour "Ajouter", obtenir la description de la tâche.
    *   Pour "Supprimer", d'abord voir les tâches, puis obtenir le numéro de la tâche.
    *   Pour "Quitter", appeler `sauvegarder_taches()` et `break` la boucle.
    *   Inclure une validation de base des entrées et des messages d'erreur.

**Exemple d'Interaction :**
.. code-block:: text
    Gestionnaire de Liste de Tâches
    1. Ajouter une Tâche
    2. Voir les Tâches
    3. Supprimer une Tâche
    4. Quitter
    Entrez votre choix : 2
    Tâches Actuelles :
    1. Faire les courses
    2. Payer les factures
    ---
    Entrez votre choix : 1
    Entrez la description de la tâche : Promener le chien
    Tâche ajoutée.
    ---
    Entrez votre choix : 2
    Tâches Actuelles :
    1. Faire les courses
    2. Payer les factures
    3. Promener le chien
    ---
    Entrez votre choix : 3
    Tâches Actuelles :
    1. Faire les courses
    2. Payer les factures
    3. Promener le chien
    Entrez le numéro de la tâche à supprimer : 2
    Tâche "Payer les factures" supprimée.
    ---
    Entrez votre choix : 4
    Tâches sauvegardées. Fermeture.

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # gestionnaire_todo.py
       import os

       NOM_FICHIER_TODO = "todo.txt"

       def charger_taches(nom_fichier=NOM_FICHIER_TODO):
           """Charge les tâches depuis le fichier spécifié."""
           taches = []
           try:
               with open(nom_fichier, "r", encoding="utf-8") as f:
                   for ligne in f:
                       taches.append(ligne.strip()) # Supprimer les caractères de nouvelle ligne
               print(f"Tâches chargées depuis {nom_fichier}.")
           except FileNotFoundError:
               print(f"'{nom_fichier}' non trouvé. Démarrage avec une liste vide.")
           except IOError as e:
               print(f"Erreur lors du chargement des tâches depuis '{nom_fichier}' : {e}")
           return taches

       def sauvegarder_taches(taches, nom_fichier=NOM_FICHIER_TODO):
           """Sauvegarde la liste des tâches dans le fichier spécifié."""
           try:
               with open(nom_fichier, "w", encoding="utf-8") as f:
                   for tache in taches:
                       f.write(tache + "\n")
               print(f"Tâches sauvegardées dans {nom_fichier}.")
           except IOError as e:
               print(f"Erreur lors de la sauvegarde des tâches dans '{nom_fichier}' : {e}")

       def ajouter_tache_a_liste(liste_taches, description):
           """Ajoute une nouvelle tâche à la liste."""
           if description:
               liste_taches.append(description)
               print(f"Tâche '{description}' ajoutée.")
           else:
               print("La description de la tâche ne peut pas être vide.")

       def voir_taches_dans_liste(liste_taches):
           """Affiche toutes les tâches de la liste avec numérotation."""
           if not liste_taches:
               print("Aucune tâche dans la liste.")
               return

           print("\nTâches Actuelles :")
           print("-" * 20) # Augmenté pour correspondre au titre français
           for i, tache in enumerate(liste_taches):
               print(f"{i + 1}. {tache}")
           print("-" * 20)

       def supprimer_tache_de_liste(liste_taches):
           """Supprime une tâche de la liste en fonction de son numéro."""
           if not liste_taches:
               print("Aucune tâche à supprimer.")
               return False # Indiquer qu'aucune suppression n'a eu lieu

           voir_taches_dans_liste(liste_taches)
           try:
               num_tache_str = input("Entrez le numéro de la tâche à supprimer : ")
               num_tache = int(num_tache_str)

               if 1 <= num_tache <= len(liste_taches):
                   tache_supprimee = liste_taches.pop(num_tache - 1) # Ajuster pour l'index basé sur 0
                   print(f"Tâche '{tache_supprimee}' supprimée.")
                   return True # Indiquer la suppression réussie
               else:
                   print("Numéro de tâche invalide.")
           except ValueError:
               print("Entrée invalide. Veuillez entrer un nombre.")
           return False # Indiquer aucune suppression ou tentative échouée

       def afficher_menu():
           """Affiche les options du menu principal."""
           print("\nGestionnaire de Liste de Tâches")
           print("-------------------------------") # Augmenté pour correspondre au titre français
           print("1. Ajouter une Tâche")
           print("2. Voir les Tâches")
           print("3. Supprimer une Tâche")
           print("4. Sauvegarder et Quitter")
           print("5. Quitter Sans Sauvegarder")


       def main():
           """Fonction principale pour exécuter l'application de Liste de Tâches."""
           taches = charger_taches()
           modifications_effectuees = False

           while True:
               afficher_menu()
               choix = input("Entrez votre choix (1-5) : ")

               if choix == '1':
                   description = input("Entrez la description de la tâche : ").strip()
                   ajouter_tache_a_liste(taches, description)
                   modifications_effectuees = True
               elif choix == '2':
                   voir_taches_dans_liste(taches)
               elif choix == '3':
                   if supprimer_tache_de_liste(taches):
                       modifications_effectuees = True
               elif choix == '4':
                   sauvegarder_taches(taches)
                   print("Fermeture du Gestionnaire de Liste de Tâches.")
                   break
               elif choix == '5':
                   if modifications_effectuees:
                       confirmation = input("Vous avez des modifications non enregistrées. Êtes-vous sûr de vouloir quitter sans enregistrer ? (oui/non) : ").lower()
                       if confirmation == 'oui':
                           print("Fermeture du Gestionnaire de Liste de Tâches sans sauvegarder.")
                           break
                   else:
                       print("Fermeture du Gestionnaire de Liste de Tâches.")
                       break
               else:
                   print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

       if __name__ == "__main__":
           main()

----------------------------------------------------

Résumé du Module 7
==================

Excellent travail pour avoir terminé le Module 7 ! Vous avez maintenant acquis des compétences essentielles pour faire interagir vos programmes Python avec le système de fichiers, permettant la persistance des données et des applications plus complexes. Vous avez appris :

*   Les principes fondamentaux des **E/S de fichiers** et la différence entre les fichiers texte et binaires.
*   Comment **ouvrir des fichiers** en utilisant `open()` avec différents modes (`'r'`, `'w'`, `'a'`, etc.).
*   L'importance cruciale de la **fermeture des fichiers** et la commodité d'utiliser l'instruction `with` pour une gestion automatique.
*   Diverses méthodes pour **lire depuis des fichiers** (`read()`, `readline()`, `readlines()`, et l'itération).
*   Comment **écrire dans des fichiers** (`write()`, `writelines()`) et comprendre l'ajout par rapport à l'écrasement.
*   La manipulation de base des **chemins de fichiers** en utilisant `os.path` (et un aperçu de `pathlib`).
*   À anticiper et gérer les **exceptions courantes liées aux fichiers** comme `FileNotFoundError`.
*   Une brève introduction aux formats de fichiers structurés comme **CSV et JSON**, préparant le terrain pour l'apprentissage futur.

Savoir lire et écrire dans des fichiers est une compétence fondamentale qui ouvre un large éventail de possibilités, de la simple journalisation de données aux applications complexes de traitement de données.

Prochaine étape, nous explorerons comment organiser davantage votre code Python en unités réutilisables et comment exploiter le code écrit par d'autres : :ref:`module8-modules-packages-fr` !