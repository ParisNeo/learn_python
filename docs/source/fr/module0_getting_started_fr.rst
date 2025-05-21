.. _module0-getting-started-fr:

=====================================================
Module 0 : Premiers pas - La rampe de lancement
=====================================================

Bienvenue dans votre aventure Python ! Ce premier module a pour but de vous aider à vous installer et à vous familiariser avec les bases. Nous passerons de la compréhension de ce qu'est Python à l'écriture et à l'exécution de votre tout premier programme.

.. image:: ../_static/images/rocket_launch.png
   :alt: Lancement de fusée - Votre aventure Python commence !
   :width: 200px
   :align: center

Objectifs d'apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Comprendre ce qu'est la programmation en termes simples.
*   Expliquer pourquoi Python est un excellent langage à apprendre.
*   Installer Python avec succès sur votre ordinateur.
*   Configurer un éditeur de code de base (VS Code recommandé).
*   Écrire, enregistrer et exécuter un programme Python simple (« Hello, World! »).
*   Comprendre ce que sont les commentaires et comment les utiliser.
*   Reconnaître un message d'erreur Python de base.

----------------------------------------------------

Qu'est-ce que la programmation ?
====================

Pensez à la programmation comme le fait de donner un ensemble d'instructions très spécifiques à un ordinateur. Les ordinateurs sont puissants, mais ils sont aussi très littéraux. Ils feront *exactement* ce que vous leur direz de faire, ni plus, ni moins.

Un **programme** est une séquence de ces instructions, écrites dans un langage que l'ordinateur peut comprendre (ou qui peut être traduit dans un tel langage). Nous, en tant que programmeurs, écrivons ces instructions pour résoudre des problèmes, automatiser des tâches, créer des jeux, construire des sites web, analyser des données, et bien plus encore !

.. tip::
   Analogie : Imaginez que vous donnez des instructions à un robot cuisinier pour faire un sandwich. Vous ne pouvez pas simplement dire "fais-moi un sandwich". Vous devez spécifier :
   1. Prends deux tranches de pain.
   2. Ouvre le pot de beurre de cacahuète.
   3. Étale le beurre de cacahuète sur une tranche.
   4. ...et ainsi de suite.
   La programmation est similaire – décomposer une tâche en petites étapes précises.

----------------------------------------------------

Pourquoi Python ?
===========

Il existe de nombreux langages de programmation, alors pourquoi commencer par Python ?

*   **Lisibilité :** La syntaxe de Python (les règles d'écriture) est conçue pour être claire et facile à lire, presque comme de l'anglais simple. Cela le rend idéal pour les débutants.
*   **Polyvalence :** Python est un langage polyvalent. Vous pouvez l'utiliser pour :
    *   Le développement web (comme Instagram, YouTube, Spotify)
    *   La science des données et l'apprentissage automatique (machine learning)
    *   L'automatisation et le scripting
    *   Le calcul scientifique
    *   Le développement de jeux
    *   Et bien plus encore !
*   **Grande communauté et bibliothèques :** Python dispose d'une communauté massive et active. Cela signifie beaucoup d'aide disponible en ligne et une vaste collection de code pré-écrit (appelées bibliothèques ou paquets) que vous pouvez utiliser pour faire des choses complexes facilement.
*   **Adapté aux débutants :** Sa courbe d'apprentissage est douce, vous permettant de construire des choses intéressantes relativement rapidement, ce qui est très motivant !
*   **Forte demande :** Les développeurs Python sont très demandés sur le marché du travail.

----------------------------------------------------

Configuration de votre environnement
===========================

Pour commencer à écrire et à exécuter du code Python, vous avez besoin de deux choses principales :

1.  **L'interpréteur Python :** C'est le programme qui comprend et exécute votre code Python.
2.  **Un éditeur de code :** C'est un éditeur de texte spécialisé où vous écrirez vos fichiers de code Python (scripts).

Installation de Python
-----------------

1.  **Allez sur le site officiel :** Le meilleur endroit pour obtenir Python est son site officiel : `python.org <https://www.python.org/downloads/>`_
2.  **Téléchargez le programme d'installation :** Téléchargez la dernière version stable pour votre système d'exploitation (Windows, macOS, Linux).
3.  **Exécutez le programme d'installation :**
    *   **Windows :** Assurez-vous de cocher la case "Add Python to PATH" (Ajouter Python au PATH) lors de l'installation. C'est important !
    *   **macOS :** Python peut déjà être pré-installé (une version plus ancienne). Il est généralement recommandé d'installer la dernière version depuis python.org. Le programme d'installation fonctionne comme la plupart des installateurs d'applications macOS.
    *   **Linux :** Python est généralement pré-installé. Vous pouvez vérifier avec `python3 --version`. Si vous devez installer ou mettre à jour, utilisez le gestionnaire de paquets de votre distribution (par ex., `sudo apt-get install python3` sur Debian/Ubuntu).
4.  **Vérifiez l'installation :** Ouvrez un terminal (Invite de commandes ou PowerShell sous Windows, Terminal sous macOS/Linux) et tapez :
    .. code-block:: bash

        python --version
        # ou, sur certains systèmes, vous pourriez avoir besoin de :
        # python3 --version

    Vous devriez voir le numéro de version de Python s'afficher, par ex., `Python 3.10.4`. Si vous obtenez une erreur, Python n'est peut-être pas installé correctement ou pas ajouté au PATH de votre système.

.. note::
   Si vous rencontrez des problèmes d'installation, une recherche rapide sur le web comme "installer python 3 sur [Votre SE]" fournit souvent des guides détaillés spécifiques à votre SE et des solutions de dépannage.

Choix et configuration d'un éditeur de code
---------------------------------------

Bien que vous *pourriez* écrire du code Python dans un simple éditeur de texte comme le Bloc-notes, un éditeur de code dédié offre de nombreuses fonctionnalités utiles comme la coloration syntaxique (colorer votre code pour le rendre plus facile à lire), l'auto-complétion et des outils de débogage.

Nous recommandons **Visual Studio Code (VS Code)** :

1.  **Téléchargez VS Code :** Obtenez-le sur `code.visualstudio.com <https://code.visualstudio.com/>`_
2.  **Installez-le :** Suivez les instructions d'installation pour votre SE.
3.  **Installez l'extension Python :**
    *   Ouvrez VS Code.
    *   Allez dans la vue Extensions (cliquez sur l'icône carrée dans la barre latérale ou appuyez sur ``Ctrl+Shift+X``).
    *   Recherchez "Python" (par Microsoft).
    *   Cliquez sur "Installer". Cette extension offre un support riche pour le développement Python.

.. tip::
    Prenez quelques minutes pour vous familiariser avec VS Code :
    *   L'**Explorateur** (barre latérale) pour ouvrir des fichiers et des dossiers.
    *   La zone d'**Édition** où vous taperez le code.
    *   Le **Terminal intégré** (vous pouvez l'ouvrir via `Terminal > Nouveau Terminal` ou ``Ctrl+` ``) où vous exécuterez vos scripts Python.

L'interpréteur Python : Mode interactif vs. Mode script
-----------------------------------------------------

Vous pouvez interagir avec Python de deux manières principales :

1.  **Mode interactif (REPL) :**
    *   REPL signifie Read-Evaluate-Print Loop (Boucle Lire-Évaluer-Afficher).
    *   Vous tapez les commandes Python une par une, et Python les exécute immédiatement et affiche le résultat.
    *   Pour le démarrer, ouvrez votre terminal et tapez `python` ou `python3`. Vous verrez une invite `>>>`.
    *   Exemple :
        .. code-block:: pycon

            >>> print("Bonjour depuis le mode interactif !")
            Bonjour depuis le mode interactif !
            >>> 2 + 2
            4
            >>> exit()

    *   C'est idéal pour tester de petits extraits de code ou explorer.

2.  **Mode script :**
    *   Vous écrivez votre code Python dans un fichier (généralement avec une extension `.py`, par ex., `mon_programme.py`).
    *   Vous demandez ensuite à l'interpréteur Python d'exécuter toutes les instructions de ce fichier, du haut vers le bas.
    *   C'est ainsi que vous construirez des applications plus importantes.

----------------------------------------------------

Votre premier programme Python : « Hello, World! »
==========================================

C'est une tradition en programmation de faire en sorte que votre premier programme affiche le texte "Hello, World!". Faisons-le.

1.  **Créez un dossier :** Créez un dossier sur votre ordinateur pour vos projets Python (par ex., `cours_python`).
2.  **Ouvrez VS Code dans ce dossier :**
    *   Dans VS Code, allez à `Fichier > Ouvrir le dossier...` et sélectionnez le dossier que vous avez créé.
3.  **Créez un nouveau fichier :**
    *   Dans l'Explorateur de VS Code, cliquez sur l'icône "Nouveau fichier" (ou `Fichier > Nouveau fichier`).
    *   Nommez le fichier `hello.py`. Assurez-vous qu'il se termine par `.py`.
4.  **Écrivez le code :** Tapez la ligne suivante dans `hello.py` :
    .. code-block:: python

        print("Hello, World!")

5.  **Enregistrez le fichier :** Appuyez sur ``Ctrl+S`` (Windows/Linux) ou ``Cmd+S`` (macOS).
6.  **Exécutez le programme :**
    *   Ouvrez le terminal intégré dans VS Code (`Terminal > Nouveau Terminal`).
    *   Assurez-vous que votre terminal est dans le bon répertoire (où `hello.py` est enregistré). Si vous avez ouvert le dossier dans VS Code, c'est généralement le cas.
    *   Tapez la commande suivante et appuyez sur Entrée :
        .. code-block:: bash

            python hello.py
            # ou si cela ne fonctionne pas, essayez :
            # python3 hello.py

7.  **Voyez le résultat :** Vous devriez voir `Hello, World!` s'afficher dans le terminal.

.. image:: /_static/images/hello_world_output.png
   :alt: Terminal affichant la sortie 'Hello, World!'
   :width: 400px
   :align: center

   (Imaginez une capture d'écran d'un terminal affichant la commande et la sortie)

**Félicitations ! Vous avez écrit et exécuté votre premier programme Python !** C'est une première étape importante.

----------------------------------------------------

Comprendre les erreurs de base
==========================

Les erreurs font partie intégrante de la programmation. N'en ayez pas peur ! Python essaiera de vous dire ce qui n'a pas fonctionné.

Faisons intentionnellement une erreur. Modifiez votre `hello.py` comme suit :

.. code-block:: python
    :emphasize-lines: 1

    print("Hello, World! # Parenthèse fermante manquante

Si vous essayez d'exécuter cela, Python vous donnera une `SyntaxError` :

.. code-block:: text

    File "hello.py", line 1
      print("Hello, World!
            ^
    SyntaxError: unterminated string literal (detected at line 1)

Décortiquons ce que cela signifie :

*   `File "hello.py", line 1`: Vous indique que l'erreur se trouve dans le fichier `hello.py` à la ligne 1.
*   `print("Hello, World!`: Vous montre la ligne où Python pense que l'erreur se trouve.
*   `^`: Pointe vers l'endroit où Python a détecté le problème.
*   `SyntaxError: unterminated string literal`: C'est le type d'erreur. Une "chaîne de caractères littérale" (string literal) est du texte entre guillemets. "Unterminated" (non terminée) signifie qu'elle n'a pas été correctement fermée.

Apprendre à lire les messages d'erreur est une compétence cruciale. Ce sont vos indices pour corriger votre code.

Corrigez l'erreur en ajoutant la parenthèse et le guillemet fermants, puis exécutez-le à nouveau pour confirmer que cela fonctionne.

----------------------------------------------------

Commentaires
========

Les commentaires sont des notes dans votre code qui sont ignorées par l'interpréteur Python. Ils sont destinés aux humains – pour vous (pour vous souvenir de ce que fait votre code plus tard) ou pour les autres (pour comprendre votre code).

En Python, tout ce qui se trouve sur une ligne après un symbole dièse (`#`) est un commentaire.

.. code-block:: python

    # Ceci est un commentaire sur une ligne entière.
    # Il explique ce que fait la ligne de code suivante.
    print("Hello, World!") # Ceci est un commentaire en fin de ligne.

    # Vous pouvez également utiliser les commentaires pour "désactiver" temporairement du code :
    # print("Cette ligne ne s'exécutera pas.")
    print("Cette ligne s'exécutera.")

De bons commentaires expliquent *pourquoi* vous faites quelque chose, ou clarifient des parties complexes de votre code. Ne commentez pas excessivement des choses évidentes.

----------------------------------------------------

Mini-projet : Salutation personnalisée
====================================

C'est l'heure de pratiquer !

**Objectif :** Écrire un programme Python qui :
1.  Affiche une salutation personnalisée pour vous.
2.  Affiche un fait amusant sur Python (vous pouvez en inventer un ou en trouver un en ligne).

**Exemple de sortie :**

.. code-block:: text

    Bonjour, [Votre Nom] ! Bienvenue dans le monde de Python !
    Le saviez-vous ? Python a été nommé d'après Monty Python's Flying Circus !

**Étapes :**

1.  Créez un nouveau fichier dans VS Code (par ex., `salutation.py`).
2.  Écrivez des instructions `print()` pour atteindre l'objectif.
3.  Utilisez des commentaires pour expliquer ce que fait votre programme.
4.  Enregistrez et exécutez votre programme depuis le terminal.

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # salutation.py
       # Ce programme affiche une salutation personnalisée et un fait amusant sur Python.

       # Afficher une salutation personnalisée
       print("Bonjour, Alex ! Bienvenue dans le monde de Python !") # Remplacez Alex par votre nom

       # Afficher un fait amusant sur Python
       print("Le saviez-vous ? Python est souvent utilisé pour des choses sympas comme l'IA et les applications web !")

----------------------------------------------------

Résumé du Module 0
================

Bravo d'avoir terminé le Module 0 ! Vous avez appris :

*   Le concept de base de la programmation.
*   Pourquoi Python est un langage populaire et utile.
*   Comment installer Python et configurer VS Code.
*   L'excitation d'exécuter votre premier programme « Hello, World! ».
*   Comment comprendre les erreurs de base et utiliser les commentaires.

Vous avez maintenant la configuration de base pour approfondir Python. Dans le prochain module, nous explorerons les variables et les différents types de données avec lesquels vous pouvez travailler.

Prêt pour la suite ? Allons au :ref:`module1-variables-and-data-types-fr` !