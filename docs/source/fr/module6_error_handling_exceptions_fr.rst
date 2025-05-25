.. _module6-error-handling-exceptions-fr:

==================================================================
Module 6 : Gestion des Erreurs et Exceptions - Récupération Élégante
==================================================================

Bienvenue dans le Module 6 ! Jusqu'à présent, nous avons écrit des programmes qui, pour la plupart, supposent que tout se déroule comme prévu. Cependant, dans le monde réel, les programmes rencontrent des situations inattendues : les utilisateurs peuvent saisir des données invalides, des fichiers peuvent être manquants, ou des connexions réseau peuvent être interrompues. La **gestion des erreurs** est le processus consistant à anticiper, détecter et répondre à ces erreurs de manière à ce que votre programme puisse soit récupérer élégamment, soit se terminer avec un message clair, plutôt que de planter brusquement. Python utilise les **exceptions** pour gérer ces erreurs d'exécution.

.. image:: ../_static/images/safety_net.png
   :alt: Un filet de sécurité sous un funambule, représentant la gestion des exceptions
   :width: 600px
   :align: center

Objectifs d'Apprentissage
-------------------------

À la fin de ce module, vous serez capable de :

*   Comprendre la différence entre les erreurs de syntaxe et les exceptions (erreurs d'exécution).
*   Identifier les types courants d'exceptions intégrées en Python.
*   Utiliser les blocs `try` et `except` pour attraper et gérer les exceptions.
*   Gérer plusieurs exceptions spécifiques.
*   Accéder à l'objet exception pour obtenir plus d'informations sur une erreur.
*   Utiliser la clause `else` dans un bloc `try` pour exécuter du code lorsque aucune exception ne se produit.
*   Utiliser la clause `finally` pour exécuter du code de nettoyage, qu'une exception se soit produite ou non.
*   Lever des exceptions délibérément en utilisant l'instruction `raise`.
*   Comprendre les meilleures pratiques pour la gestion des exceptions.

----------------------------------------------------

Que sont les Erreurs et les Exceptions ?
=======================================

En programmation, les erreurs peuvent être globalement catégorisées :

1.  **Erreurs de Syntaxe (Erreurs d'Analyse / Parsing Errors):**
    Celles-ci se produisent lorsque votre code enfreint les règles grammaticales de Python. L'interpréteur Python détecte ces erreurs *avant même* que votre programme ne commence à s'exécuter. Vous les avez probablement déjà rencontrées (par ex., deux-points manquants, indentation incorrecte, mots-clés mal orthographiés). Le programme ne s'exécutera pas tant que les erreurs de syntaxe ne seront pas corrigées.

    .. code-block:: python

        # Erreur de Syntaxe : Deux-points manquants
        # def ma_fonction()
        #    print("Bonjour")

        # Erreur de Syntaxe : Syntaxe invalide
        # print "Bonjour" # En Python 3, print est une fonction

2.  **Erreurs d'Exécution (Exceptions):**
    Ces erreurs se produisent *pendant que* votre programme s'exécute. Même si votre code est syntaxiquement correct, il peut rencontrer des situations qu'il ne peut pas gérer, conduisant à une exception. Lorsqu'une exception se produit et n'est pas gérée, le programme se termine et Python affiche un message de "traceback" (trace d'appels), indiquant où l'erreur s'est produite.

    .. code-block:: python

        # Exemple d'erreur d'exécution (ZeroDivisionError)
        # numerateur = 10
        # denominateur = 0
        # resultat = numerateur / denominateur # Cette ligne lèvera une ZeroDivisionError
        # print(resultat)

        # Exemple d'erreur d'exécution (TypeError)
        # age = 30
        # message = "Mon âge est : " + age # Cette ligne lèvera une TypeError (impossible de concaténer str et int)
        # print(message)

Une **exception** est un événement qui se produit pendant l'exécution d'un programme et qui perturbe le flux normal des instructions du programme. Lorsqu'un script Python lève une exception, il doit soit gérer l'exception immédiatement, soit se terminer.

Exceptions Intégrées Courantes
-----------------------------
Python possède de nombreuses exceptions intégrées. Parmi les plus courantes, on trouve :

*   `TypeError`: Opération ou fonction appliquée à un objet de type inapproprié. (par ex., ` "2" + 2`)
*   `ValueError`: Opération ou fonction reçoit un argument du bon type mais avec une valeur inappropriée. (par ex., `int("bonjour")`)
*   `NameError`: Un nom local ou global n'est pas trouvé. (par ex., utilisation d'une variable non définie)
*   `IndexError`: Un indice de séquence est hors limites. (par ex., `ma_liste[10]` quand `ma_liste` n'a que 3 éléments)
*   `KeyError`: Une clé de dictionnaire n'est pas trouvée. (par ex., `mon_dict["cle_inconnue"]`)
*   `ZeroDivisionError`: Le second argument d'une opération de division ou de modulo est zéro.
*   `FileNotFoundError`: Un fichier ou un répertoire est demandé mais n'existe pas.
*   `AttributeError`: Une référence d'attribut ou une assignation échoue. (par ex., ` "chaine".append("x")`)
*   `ImportError`: L'instruction `import` rencontre des difficultés pour charger un module.

----------------------------------------------------

Gestion des Exceptions : Le Bloc `try-except`
=============================================

Pour gérer les exceptions élégamment, vous utilisez les mots-clés `try` et `except`.

*   Le code susceptible de provoquer une exception est placé dans le bloc `try`.
*   Si une exception se produit dans le bloc `try`, Python recherche un bloc `except` correspondant pour la gérer.
*   Si aucune exception ne se produit, le bloc `except` est ignoré.

Syntaxe de Base :
----------------
.. code-block:: python

    try:
        # Code susceptible de lever une exception
        # ...
    except TypeException: # Attrape un type spécifique d'exception
        # Code pour gérer l'exception
        # ...

Exemple : Gestion de `ValueError`
---------------------------------
Supposons que nous voulions obtenir un entier de l'utilisateur. `int()` lèvera une `ValueError` si l'entrée ne peut pas être convertie en entier.

.. code-block:: python

    try:
        age_str = input("Entrez votre âge : ")
        age = int(age_str) # ValueError potentielle
        print(f"Vous aurez {age + 1} ans l'année prochaine.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier pour l'âge.")

Si l'utilisateur entre "trente", l'appel `int("trente")` lève une `ValueError`. Le bloc `except ValueError:` attrape cela, et son code est exécuté. Si l'utilisateur entre "30", aucune exception ne se produit, et le bloc `except` est ignoré.

Gérer des Exceptions Spécifiques
-------------------------------
Il est de bonne pratique de capturer des exceptions spécifiques plutôt que d'utiliser une clause `except:` nue (qui attrape *toutes* les exceptions). Cela vous permet de réagir de manière appropriée à différents types d'erreurs.

.. code-block:: python

    try:
        num1 = int(input("Entrez un numérateur : "))
        num2 = int(input("Entrez un dénominateur : "))
        resultat = num1 / num2 # ZeroDivisionError ou ValueError potentielle
        print(f"Le résultat est : {resultat}")
    except ValueError:
        print("Entrée invalide. Veuillez entrer uniquement des nombres.")
    except ZeroDivisionError:
        print("Erreur : Impossible de diviser par zéro.")
    except Exception as e: # Attraper toute autre exception inattendue
        print(f"Une erreur inattendue s'est produite : {e}")

*   Python essaie les clauses `except` une par une.
*   La partie `Exception as e` est utile :
    *   `Exception` est une classe de base pour la plupart des exceptions intégrées. L'attraper est un peu général mais mieux qu'un `except:` nu.
    *   `as e` assigne l'instance de l'exception à la variable `e`, vous permettant d'accéder à des informations sur l'erreur (par ex., `print(e)` donne souvent le message d'erreur).

Plusieurs Exceptions dans un Seul Bloc `except`
----------------------------------------------
Vous pouvez gérer plusieurs types d'exceptions avec un seul bloc en les fournissant sous forme de tuple.

.. code-block:: python

    nom_fichier = "mes_donnees.txt"
    try:
        with open(nom_fichier, "r") as f:
            contenu = f.read()
            valeur = int(contenu.strip())
        print(f"Valeur du fichier : {valeur}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Erreur lors du traitement du fichier '{nom_fichier}' : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

----------------------------------------------------

La Clause `else`
================

L'instruction `try` peut optionnellement avoir une clause `else`. Le code dans le bloc `else` est exécuté *uniquement si* le bloc `try` ne lève aucune exception.

.. code-block:: python

    try:
        num_str = input("Entrez un nombre : ")
        num = float(num_str)
    except ValueError:
        print("Ce n'était pas un nombre valide.")
    else:
        # Ce bloc ne s'exécute que si aucune ValueError ne s'est produite dans le bloc try
        print(f"Le carré de votre nombre est : {num ** 2}")

Pourquoi utiliser `else` ? Cela aide à séparer le code qui pourrait lever une exception du code qui ne devrait s'exécuter que si les opérations initiales ont réussi, améliorant la lisibilité.

----------------------------------------------------

La Clause `finally`
===================

L'instruction `try` peut également avoir une clause `finally`. Le code dans le bloc `finally` est *toujours* exécuté, qu'une exception se soit produite dans le bloc `try` ou qu'elle ait été gérée. Ceci est souvent utilisé pour des actions de nettoyage, comme la fermeture de fichiers ou la libération de ressources.

.. code-block:: python

    fichier = None # Initialiser fichier à None
    try:
        chemin_fichier = "donnees.txt"
        fichier = open(chemin_fichier, "w") # FileNotFoundError potentielle si le mode était 'r' et que le fichier n'existait pas
                                          # ou PermissionError si pas d'accès en écriture
        fichier.write("Bonjour, monde !")
        # Simuler une erreur :
        # resultat = 10 / 0 # Cela provoquerait une ZeroDivisionError
        print("Écriture réussie dans le fichier.")
    except FileNotFoundError:
        print(f"Erreur : Fichier '{chemin_fichier}' non trouvé.")
    except ZeroDivisionError:
        print("Erreur : Erreur de calcul (division par zéro).")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        # Ce bloc s'exécute toujours
        if fichier: # Vérifier si le fichier a été ouvert avec succès
            fichier.close()
            print("Fichier fermé.")
        else:
            print("Le fichier n'a pas été ouvert, donc pas besoin de le fermer.")

Même si une exception non gérée se produit dans le bloc `try` ou `except`, ou si une instruction `return`, `break` ou `continue` est exécutée, la clause `finally` s'exécutera quand même avant que le programme ne se termine réellement ou ne continue ailleurs.

L'instruction `with` (vue dans le Module 4 pour les fichiers) gère souvent automatiquement le nettoyage des ressources et peut être une alternative plus propre à `try...finally` pour la gestion des ressources comme les fichiers.

----------------------------------------------------

Lever des Exceptions : L'Instruction `raise`
============================================

Vous pouvez lever délibérément une exception dans votre code en utilisant l'instruction `raise`. Ceci est utile lorsque vous détectez une condition d'erreur dans votre fonction et que vous souhaitez la signaler au code appelant.

Syntaxe : `raise TypeException("Message d'erreur optionnel")`

.. code-block:: python

    def obtenir_age(val_age):
        """Retourne l'âge s'il est valide, sinon lève une ValueError."""
        if val_age < 0:
            raise ValueError("L'âge ne peut pas être négatif.")
        if val_age > 120:
            raise ValueError("L'âge semble trop élevé, veuillez vérifier.")
        return val_age

    try:
        entree_age_utilisateur = int(input("Entrez votre âge : "))
        age_valide = obtenir_age(entree_age_utilisateur)
        print(f"Âge validé : {age_valide}")
    except ValueError as e: # Attrape ValueError de int() ou de obtenir_age()
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

Vous pouvez lever des exceptions intégrées ou même définir vos propres exceptions personnalisées (ce qui est un sujet plus avancé, impliquant généralement la création de classes qui héritent de `Exception`).

----------------------------------------------------

Meilleures Pratiques pour la Gestion des Exceptions
===================================================

1.  **Soyez Spécifique :** Attrapez des exceptions spécifiques chaque fois que possible, plutôt qu'un `except:` nu ou `except Exception:`. Cela rend votre gestion des erreurs plus précise.
2.  **Ne Masquez Pas les Erreurs :** Évitez d'attraper des exceptions juste pour les ignorer (par ex., `except: pass`), à moins d'avoir une très bonne raison. Cela peut cacher des bogues.
3.  **Utilisez `finally` pour le Nettoyage :** Assurez-vous que les ressources sont libérées (fichiers fermés, verrous libérés) dans un bloc `finally` ou en utilisant des gestionnaires de contexte (instruction `with`).
4.  **Fournissez des Messages Informatifs :** Lorsque vous gérez ou levez des exceptions, donnez des messages clairs qui aident à diagnostiquer le problème.
5.  **Échouez Rapidement (Parfois) :** Si une erreur se produit que votre fonction actuelle ne peut raisonnablement pas gérer, il est souvent préférable de laisser l'exception se propager (ou d'en lever une nouvelle, plus spécifique) plutôt que d'essayer de deviner une récupération.
6.  **Gardez les Blocs `try` Petits :** N'encadrez que les lignes de code spécifiques qui pourraient lever une exception dans le bloc `try`. Cela rend plus clair l'origine potentielle de l'erreur.
7.  **Utilisez `else` pour le Code en Cas de Succès :** Placez le code qui ne doit s'exécuter que si le bloc `try` réussit dans la clause `else`.

----------------------------------------------------

Mini-Projet : Processeur de Données Robuste
===========================================

Créons un petit programme qui simule le traitement d'éléments de données. La fonction de traitement pourrait rencontrer des problèmes avec certaines données.

**Objectif :**
1.  Créer une fonction `traiter_element(element)` :
    *   Si `element` est `None`, elle doit `lever TypeError` avec le message "L'élément ne peut pas être None."
    *   Si `element` est une chaîne qui ne peut pas être convertie en nombre, essayer `float(element)` lèvera `ValueError`.
    *   Si `element` (après conversion en float) est négatif, elle doit `lever ValueError` avec le message "La valeur de l'élément ne peut pas être négative pour le traitement."
    *   Si `element` est 0, elle doit `lever ZeroDivisionError` (simulant une étape de division qui échoue pour zéro).
    *   En cas de succès, elle doit retourner, disons, la racine carrée de l'élément (utilisez `math.sqrt`, donc vous aurez besoin de `import math`).
2.  La partie principale du programme doit :
    *   Avoir une liste d'échantillons de données (par ex., `[16, "25", "pomme", -4, 0, None, 49]`).
    *   Parcourir chaque élément.
    *   Pour chaque élément, appeler `traiter_element` à l'intérieur d'une structure `try-except-else-finally`.
    *   Gérer `TypeError`, `ValueError` et `ZeroDivisionError` spécifiquement, en affichant un message informatif.
    *   Utiliser un bloc `else` pour afficher le résultat en cas de succès.
    *   Utiliser un bloc `finally` pour afficher un message comme "Fin de la tentative de traitement pour l'élément : [valeur_element]".

**Exemple d'Interaction pour un élément :**

.. code-block:: text

    Traitement de l'élément : 16
    Traitement réussi. Résultat : 4.0
    Fin de la tentative de traitement pour l'élément : 16
    ---
    Traitement de l'élément : pomme
    Erreur lors du traitement de l'élément 'pomme' : impossible de convertir la chaîne en float: 'pomme'
    Fin de la tentative de traitement pour l'élément : pomme
    ---
    Traitement de l'élément : -4
    Erreur lors du traitement de l'élément '-4' : La valeur de l'élément ne peut pas être négative pour le traitement.
    Fin de la tentative de traitement pour l'élément : -4
    ---

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # processeur_donnees_robuste.py
       import math

       def traiter_element(element):
           """
           Traite un seul élément de données.
           Lève TypeError, ValueError, ou ZeroDivisionError pour les éléments invalides.
           Retourne la racine carrée de l'élément s'il est valide.
           """
           print(f"Traitement de l'élément : {repr(element)}") # repr() affiche None comme 'None'

           if element is None:
               raise TypeError("L'élément ne peut pas être None.")

           try:
               # Tenter de convertir en float si c'est une chaîne ou déjà un nombre
               element_numerique = float(element)
           except ValueError as e: # Gère les cas comme float("pomme")
               # Re-lever ou lever une nouvelle erreur plus spécifique si nécessaire,
               # ou laisser la ValueError originale se propager avec son message.
               # Pour cet exemple, nous laissons le message original 'impossible de convertir...'
               raise ValueError(f"Impossible de convertir '{element}' en nombre : {e}")


           if element_numerique < 0:
               raise ValueError("La valeur de l'élément ne peut pas être négative pour le traitement.")
           if element_numerique == 0:
               # Simuler une opération qui causerait cela, ou simplement le lever.
               # Par exemple, si nous calculions 1/sqrt(element)
               raise ZeroDivisionError("La valeur de l'élément est zéro, conduisant à une division par zéro dans une étape hypothétique.")

           return math.sqrt(element_numerique)

       def main():
           """Fonction principale pour tester le processeur de données."""
           echantillons_donnees = [16, "25", "pomme", -4, 0, None, 49, "7.5"]

           for echantillon in echantillons_donnees:
               resultat = None
               try:
                   resultat = traiter_element(echantillon)
               except TypeError as e:
                   print(f"Erreur de Type pour l'élément '{repr(echantillon)}' : {e}")
               except ValueError as e:
                   print(f"Erreur de Valeur pour l'élément '{repr(echantillon)}' : {e}")
               except ZeroDivisionError as e:
                   print(f"Erreur de Division par Zéro pour l'élément '{repr(echantillon)}' : {e}")
               except Exception as e: # Fourre-tout pour toute autre erreur inattendue
                   print(f"Une erreur inattendue s'est produite pour l'élément '{repr(echantillon)}' : {e}")
               else:
                   print(f"Traitement réussi. Résultat : {resultat}")
               finally:
                   print(f"Fin de la tentative de traitement pour l'élément : {repr(echantillon)}")
                   print("---")

       if __name__ == "__main__":
           main()

----------------------------------------------------

Résumé du Module 6
==================

Bravo pour avoir parcouru le Module 6 ! Comprendre et mettre en œuvre la gestion des erreurs est crucial pour écrire des programmes Python robustes et conviviaux. Vous avez appris :

*   La distinction entre les **erreurs de syntaxe** et les **erreurs d'exécution (exceptions)**.
*   Comment utiliser les blocs `try-except` pour attraper et gérer des exceptions spécifiques.
*   Le rôle de la clause `else` pour le code qui doit s'exécuter lorsque aucune exception ne se produit.
*   L'importance de la clause `finally` pour les opérations de nettoyage qui doivent toujours s'exécuter.
*   Comment `lever` des exceptions pour signaler des conditions d'erreur dans votre code.
*   Les **meilleures pratiques** clés pour une gestion efficace des exceptions.

En anticipant les problèmes potentiels et en les gérant élégamment, vous pouvez empêcher vos programmes de planter de manière inattendue et fournir de meilleurs retours aux utilisateurs ou à d'autres parties de votre système.

Dans le prochain module, nous explorerons comment travailler avec les fichiers, lire des données à partir d'eux et y écrire des données, où la gestion des exceptions sera particulièrement pertinente : :ref:`module7-file-io-fr`!