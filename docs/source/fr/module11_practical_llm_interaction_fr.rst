.. _module11-practical-llm-interaction-fr:

====================================================================================
Module 11 : Orchestration Avancée de LLM avec `lollms-client`
====================================================================================

Bienvenue dans le Module 11 ! Nous avons exploré les aspects théoriques du "Vibe Coding" et il est maintenant temps de plonger plus profondément dans des interactions pratiques et avancées avec les Grands Modèles de Langage en utilisant la bibliothèque Python `lollms-client`. Ce module ira au-delà de la génération de texte basique, en montrant comment `lollms-client` peut orchestrer des tâches complexes telles que la résumé séquentiel, la génération de texte vers image (TTI), et l'interaction directe avec diverses liaisons (bindings) LLM comme Ollama ou OpenAI, le tout géré via un backend `lollms`.

Ce module pratique vous permettra de construire des applications Python assistées par IA sophistiquées.

.. image:: ../_static/images/ai_orchestration.png
   :alt: Un chef d'orchestre (script Python) dirigeant un orchestre de modèles et d'outils IA
   :width: 650px
   :align: center

**Prérequis Importants :**
1.  **Une instance de `lollms` en cours d'exécution :** Votre `lollms-webui` (ou serveur headless) doit être opérationnel (par défaut : `http://localhost:9600`). Pour des fonctionnalités spécifiques comme le TTI ou l'utilisation directe de liaisons Ollama/OpenAI, assurez-vous que les modèles et services pertinents sont correctement configurés et actifs dans votre environnement `lollms`.
2.  **La bibliothèque `lollms-client` et ses dépendances installées.**
3.  **Optionnel (pour des exemples spécifiques) :**
    *   `pipmaster` et `docling` pour l'exemple de résumé.
    *   `Pillow` (PIL) pour le traitement d'images dans les exemples TTI.
    *   Un serveur Ollama en cours d'exécution si vous testez la liaison Ollama, avec des modèles comme `llava` ou `llama3` téléchargés.
    *   Une clé API OpenAI si vous testez la liaison OpenAI.

Objectifs d'Apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Initialiser `LollmsClient` pour divers backends et interactions avec des modèles spécifiques.
*   Effectuer des tâches de traitement de texte avancées comme `sequential_summarize` pour de grands documents.
*   Utiliser les capacités de Texte-vers-Image (TTI) de `lollms-client` pour :
    *   Lister les services TTI disponibles.
    *   Obtenir et (conceptuellement) définir les paramètres du service TTI.
    *   Générer des images à partir de prompts textuels.
*   Interagir directement avec différentes liaisons LLM (par ex., `lollms` par défaut, `ollama`, `openai`) via `LollmsClient`.
*   Gérer efficacement les réponses en streaming avec des callbacks personnalisés.
*   Intégrer des entrées multimodales (texte et images) pour la génération avec des modèles capables.
*   Comprendre la gestion des erreurs du client et les structures de réponse.

----------------------------------------------------

Initialisation et Utilisation de Base de `LollmsClient`
=======================================================

Le `LollmsClient` est votre passerelle vers le backend `lollms`. Son initialisation permet de spécifier l'hôte, le modèle cible, les paramètres de génération, et même la liaison de communication sous-jacente.

.. admonition:: Code
   :class: dropdown

   .. code-block:: python
    
    # client_setup_example.py
    from lollms_client import LollmsClient, ELF_GENERATION_FORMAT
    from ascii_colors import ASCIIColors # For colored console output

    # Default lollms server
    LOLLMS_HOST = "http://localhost:9600"

    try:
        # Basic client for default lollms server interaction
        lc_default = LollmsClient(host_address=LOLLMS_HOST)
        ASCIIColors.green(f"Default client initialized for: {lc_default.host_address}")
        ASCIIColors.info(f"Using binding: {lc_default.binding_name}, Model: {lc_default.binding.model_name if lc_default.binding else 'N/A'}")

        # Example: Client targeting an Ollama binding (if lollms is configured to proxy it or client talks directly)
        # Ensure Ollama server is running, e.g., at http://localhost:11434
        # lc_ollama = LollmsClient(
        #     binding_name="ollama", # Instructs client to use OllamaBinding
        #     host_address="http://localhost:11434", # Ollama's direct address
        #     model_name="llama3:latest" # Specific model in Ollama
        # )
        # ASCIIColors.green(f"\nOllama client initialized for: {lc_ollama.host_address}")
        # ASCIIColors.info(f"Using binding: {lc_ollama.binding_name}, Model: {lc_ollama.binding.model_name}")

    except Exception as e:
        ASCIIColors.error(f"Error during client initialization: {e}")

*   Le paramètre `binding_name` dans `LollmsClient` est crucial pour indiquer au client comment communiquer et avec quel type de service (par ex., "lollms" pour l'API LoLLMs standard, "ollama", "openai").
*   `host_address` et `model_name` sont ensuite interprétés en fonction de la liaison choisie.

----------------------------------------------------

Traitement de Texte Avancé : Résumé Séquentiel
==============================================

Pour les documents très volumineux qui dépassent la fenêtre de contexte d'un LLM, `lollms-client` offre des méthodes puissantes comme `sequential_summarize`. Celle-ci divise le document en morceaux gérables, résume chaque morceau de manière itérative (en maintenant le contexte des résumés précédents), puis compile un résumé final.

.. admonition:: Code
   :class: dropdown

   .. code-block:: python
    
    # sequential_summarize_example.py
    from lollms_client import LollmsClient
    import pipmaster as pm
    from ascii_colors import ASCIIColors

    # Ensure docling is installed for document conversion
    if not pm.is_installed("docling"):
        ASCIIColors.info("Installing docling...")
        pm.install("docling")
    from docling.document_converter import DocumentConverter

    ASCIIColors.set_log_file("lollms_client_module_log.log") # Optional logging

    try:
        lc = LollmsClient() # Assumes default http://localhost:9600
        ASCIIColors.info("LollmsClient initialized for summarization.")

        # Example: Summarize an online PDF (ensure network access)
        # Replace with a URL of a text-heavy document or a long local text file
        # article_url = "https://arxiv.org/pdf/2109.09572" # Example ArXiv paper
        # For a local file, you'd read its content into article_text
        # For this example, let's use a long string to avoid external dependencies for running the snippet easily
        article_text = """
        The field of artificial intelligence (AI) has seen remarkable advancements in recent years,
        particularly in the domain of natural language processing (NLP). Large Language Models (LLMs)
        have emerged as powerful tools capable of understanding, generating, and manipulating human
        language with unprecedented fluency. This document explores the architecture of LLMs,
        focusing on the Transformer model which underpins many state-of-the-art systems.
        Transformers utilize a mechanism called self-attention, allowing them to weigh the
        importance of different parts of the input sequence when processing information.
        This enables them to handle long-range dependencies effectively.
        Training these models typically involves two stages: pre-training on vast unlabeled
        text corpora, followed by fine-tuning on smaller, task-specific datasets.
        The ethical implications of LLMs, including bias, misinformation, and potential misuse,
        are also critical areas of ongoing research and discussion. As LLMs become more integrated
        into various applications, ensuring their responsible development and deployment is paramount.
        Further research is needed to enhance their reasoning capabilities, reduce computational costs,
        and improve their factual accuracy and robustness against adversarial attacks.
        The development of smaller, more efficient models is also a key trend.
        """*5 # Multiply to make it longer for summarization demo

        ASCIIColors.info("Simulated article text loaded.")

        # Define the summarization prompt (instructions for the LLM for each chunk)
        # This prompt guides the LLM on what to extract or how to build the summary iteratively.
        summarization_instructions = """
        Please extract the key points and main arguments from this text chunk.
        Integrate this information with any summary content already provided in the memory.
        Focus on novel information presented in the current chunk.
        The goal is to build a comprehensive yet concise summary of the entire document.
        Maintain a neutral and objective tone.
        Output the updated summary.
        """

        # Define the final formatting prompt (how to structure the complete summary)
        final_report_instructions = """
        Compile the accumulated information into a final, coherent summary.
        Organize the summary into logical paragraphs.
        Ensure the summary flows well and captures all essential aspects of the document.
        Present the output as a single block of text.
        ## Final Summary
        [Place the comprehensive summary here]
        """
        ASCIIColors.info("Starting sequential summarization...")
        # Note: Adjust ctx_size and chunk_size based on your model's capabilities
        # and the nature of the document. Larger ctx_size for the LLM is generally better.
        # The 'chunk_size' here is for how DocumentConverter or lc breaks down the input text.
        summary_output = lc.sequential_summarize(
            full_text_content=article_text,
            instruction_prompt=summarization_instructions,
            output_format_prompt=final_report_instructions, # Use this for final formatting stage
            # text_format="markdown", # Not a direct param, output_format_prompt implies structure
            context_size=8192,  # LLM's context size
            chunk_size=2048,    # How text is chunked for LLM processing
            # bootstrap_chunk_size=1024, # For initial context building, if needed
            # bootstrap_steps=1,         # Number of bootstrap steps
            debug=False # Set to True for verbose output from lollms_client
        )

        ASCIIColors.green("\n--- Generated Summary ---")
        ASCIIColors.yellow(summary_output)

    except Exception as e:
        ASCIIColors.error(f"An error occurred during summarization: {e}")
        # from ascii_colors import trace_exception # Already imported if using from example
        # trace_exception(e) # For detailed traceback

*   `sequential_summarize` est idéal pour traiter des textes plus longs que la fenêtre de contexte directe du LLM.
*   `instruction_prompt` : Guide le LLM sur la manière de traiter chaque morceau individuel et de mettre à jour le résumé progressif.
*   `output_format_prompt` : Indique au LLM comment structurer le résumé combiné final.
*   `context_size`, `chunk_size` : Paramètres critiques à ajuster en fonction du LLM que vous utilisez avec `lollms`.

----------------------------------------------------

Génération de Texte vers Image (TTI)
====================================

`lollms-client` peut interagir avec les services Texte-vers-Image configurés dans votre backend `lollms`. Cela implique de lister les services, de gérer les paramètres et de générer des images.

.. admonition:: Code
   :class: dropdown

   .. code-block:: python
    
    # tti_example.py
    from lollms_client import LollmsClient
    from ascii_colors import ASCIIColors, trace_exception
    from PIL import Image
    from pathlib import Path
    import io
    import os
    import platform # For os.name and platform.system()
    import subprocess # for platform.system() == "Darwin" or os.name == 'posix'

    try:
        # Initialize LollmsClient, specifying the tti_binding_name if you want to
        # target a specific TTI binding configured in lollms.
        # If not specified, it might use a default or require selection.
        lc = LollmsClient(
            host_address="http://localhost:9600",
            tti_binding_name="lollms" # 'lollms' TTI binding often proxies to a service like Automatic1111, ComfyUI, etc.
                                      # Ensure this binding is active and configured in your lollms server.
        )

        if not lc.tti:
            ASCIIColors.error("TTI binding could not be initialized. Ensure 'lollms' TTI binding is active and configured in your LoLLMs server.")
            # exit() # In a real script, you might exit or handle this
        else:
            # 1. List available TTI services (backends configured in lollms for image generation)
            ASCIIColors.cyan("\n--- Listing TTI Services ---")
            services = lc.tti.list_services()
            if services:
                ASCIIColors.green("Available TTI Services:")
                for i, service in enumerate(services):
                    print(f"  {i+1}. Name: {service.get('name')}, Caption: {service.get('caption')}")
            else:
                ASCIIColors.yellow("No TTI services listed. Check lollms TTI configuration.")

            # 2. Get current TTI settings (template/schema for the active service)
            ASCIIColors.cyan("\n--- Getting Active TTI Settings ---")
            # This usually returns a settings template that shows what parameters are configurable.
            settings_template = lc.tti.get_settings()
            if isinstance(settings_template, list) and settings_template : # Template is a list of setting dicts
                ASCIIColors.green("Active TTI Settings Template:")
                for setting_item in settings_template[:5]: # Show first 5 for brevity
                    print(f"  - Name: {setting_item.get('name')}, Type: {setting_item.get('type')}, Value: {setting_item.get('value')}, Help: {setting_item.get('help')}")
            elif not settings_template:
                 ASCIIColors.yellow("No active TTI service or settings template configured on the server.")
            else:
                ASCIIColors.yellow(f"Could not retrieve TTI settings or format unexpected: {settings_template}")

            # 3. Generate an Image
            ASCIIColors.cyan("\n--- Generating Image ---")
            prompt = "A majestic owl with glowing eyes, perched on a mythical tree, fantasy art"
            negative_prompt = "blurry, ugly, low quality, watermark, text, human"
            width = 768
            height = 512
            
            # Ensure output directory exists
            output_dir = Path.home() / "Documents" / "lollms_generated_images"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_filename = output_dir / "ai_fantasy_owl.png"

            ASCIIColors.info(f"Prompt: {prompt}")
            ASCIIColors.info(f"Output to: {output_filename}")

            image_bytes = lc.tti.generate_image(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                # Other parameters like 'seed', 'steps', 'cfg_scale' can be passed as kwargs
                # if supported by the active TTI service in lollms.
                # E.g., seed=12345
            )

            if image_bytes:
                ASCIIColors.green(f"Image generated successfully ({len(image_bytes)} bytes).")
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    image.save(output_filename)
                    ASCIIColors.green(f"Image saved as {output_filename}")
                    # Attempt to open the image
                    if os.name == 'nt': os.startfile(output_filename)
                    elif platform.system() == "Darwin": subprocess.call(["open", output_filename])
                    elif os.name == 'posix': subprocess.call(["xdg-open", output_filename])
                except Exception as e_save:
                    ASCIIColors.error(f"Error processing or saving image: {e_save}")
            else:
                ASCIIColors.red("Image generation failed (returned empty bytes). Check lollms server logs.")

    except Exception as e:
        ASCIIColors.error(f"An TTI-related error occurred: {e}")
        trace_exception(e)

*   `lc.tti` : Accède à l'interface Texte-vers-Image du client.
*   `lc.tti.list_services()` : Vous informe sur les backends de génération d'images configurés dans `lollms`.
*   `lc.tti.get_settings()` : Récupère les paramètres configurables pour le service TTI actuellement actif.
*   `lc.tti.generate_image(...)` : La méthode principale pour la génération d'images, prenant des prompts, des dimensions, et d'autres paramètres spécifiques au service.

----------------------------------------------------

Interaction Directe avec les Liaisons LLM (par ex., Ollama, OpenAI)
===================================================================

`LollmsClient` peut être initialisé pour interagir avec des liaisons spécifiques, vous permettant de tirer parti des modèles servis par Ollama, OpenAI (via une clé API), ou d'autres, le tout orchestré via la structure API unifiée de `lollms-client`.

.. admonition:: Code
   :class: dropdown

   .. code-block:: python
    
    # direct_binding_interaction.py
    from lollms_client import LollmsClient
    from lollms_client.lollms_types import MSG_TYPE
    from ascii_colors import ASCIIColors, trace_exception
    from pathlib import Path # For image path

    # --- Configuration ---
    # Choose your target binding and its parameters
    # BINDING_NAME = "ollama"
    # HOST_ADDRESS = "http://localhost:11434" # Ollama's default
    # OLLAMA_MODEL_NAME = "llava:latest" # A multi-modal model in Ollama
    # OLLAMA_IMAGE_PATH = str(Path(__file__).parent / "path_to_your_test_image.jpg") # Replace with actual image path

    BINDING_NAME = "lollms" # Or "openai" if you have OPENAI_API_KEY set
    HOST_ADDRESS = "http://localhost:9600" if BINDING_NAME == "lollms" else None
    MODEL_NAME = None # For 'lollms', uses server default. For 'openai', e.g., "gpt-4-turbo"

    # --- Callback for streaming ---
    def binding_streaming_callback(chunk: str, msg_type: MSG_TYPE, params=None, metadata=None) -> bool:
        if msg_type == MSG_TYPE.MSG_TYPE_CHUNK and chunk is not None:
            print(chunk, end="", flush=True)
        elif msg_type == MSG_TYPE.MSG_TYPE_EXCEPTION:
            ASCIIColors.error(f"\nStreaming Error from binding: {chunk}")
        return True

    try:
        client_params = {
            "binding_name": BINDING_NAME,
            "host_address": HOST_ADDRESS,
            "model_name": MODEL_NAME,
        }
        if client_params["host_address"] is None and BINDING_NAME in ["openai"]: # OpenAI binding doesn't need host if using official API
             del client_params["host_address"]
        
        lc = LollmsClient(**client_params)
        ASCIIColors.cyan(f"--- Interacting with '{lc.binding_name}' binding ---")
        ASCIIColors.info(f"Host: {lc.host_address or 'Default API'}, Model: {lc.binding.model_name or 'Default'}")

        # 1. List models available through this binding
        ASCIIColors.magenta("\n1. Listing Models from Binding:")
        models = lc.listModels() # Should list models specific to the binding
        if isinstance(models, list) and models:
            ASCIIColors.green("Available models:")
            for m_info in models[:5]: # Show first 5
                 model_id = m_info.get('model_name', m_info.get('id', str(m_info)))
                 print(f"  - {model_id}")
        else:
            ASCIIColors.yellow(f"No models listed or error: {models}")

        # 2. Text Generation (potentially multi-modal if model and binding support it)
        ASCIIColors.magenta("\n2. Generating Text (and maybe processing an image):")
        prompt = "What is the capital of France?"
        images_for_prompt = []

        # Example for Ollama with LLaVA (multi-modal)
        if lc.binding_name == "ollama" and "llava" in (lc.binding.model_name or "").lower():
            # Create a dummy image if OLLAMA_IMAGE_PATH doesn't exist
            # OLLAMA_IMAGE_PATH = "test_ollama_image.png" # Define this path
            # if not Path(OLLAMA_IMAGE_PATH).exists():
            #     # Code to create a dummy image (e.g., using Pillow)
            #     ASCIIColors.yellow(f"Dummy image created/used for LLaVA: {OLLAMA_IMAGE_PATH}")
            # images_for_prompt = [OLLAMA_IMAGE_PATH]
            # prompt = "Describe this image in detail."
            ASCIIColors.yellow("To test LLaVA with Ollama, uncomment image path and set prompt.")


        ASCIIColors.yellow(f"Prompt: {prompt}")
        if images_for_prompt: ASCIIColors.yellow(f"Images: {images_for_prompt}")
        ASCIIColors.green("Response (streaming):")

        full_response = lc.generate_text(
            prompt=prompt,
            images=images_for_prompt if images_for_prompt else None, # Pass images if any
            stream=True,
            streaming_callback=binding_streaming_callback,
            n_predict=200,
            temperature=0.6
        )
        print() # Newline after stream

        if isinstance(full_response, dict) and "error" in full_response:
            ASCIIColors.error(f"Generation error: {full_response['error']}")


    except Exception as e:
        ASCIIColors.error(f"An error occurred with binding '{BINDING_NAME}': {e}")
        trace_exception(e)

*   En définissant `binding_name` lors de l'initialisation de `LollmsClient`, vous indiquez au client quelle classe de liaison interne utiliser (par ex., `OllamaBinding`, `OpenAIBinding`).
*   Des méthodes comme `generate_text` et `listModels` fonctionneront alors dans le contexte de cette liaison spécifique.
*   Pour les modèles multimodaux comme LLaVA via Ollama, le paramètre `images` de `generate_text` est utilisé.

----------------------------------------------------

Résumé du Module 11
===================

Ce module vous a doté des connaissances nécessaires pour utiliser `lollms-client` pour une gamme d'interactions IA avancées. Vous avez appris à :

*   Initialiser `LollmsClient` à des fins différentes, y compris pour cibler des liaisons spécifiques.
*   Effectuer un traitement de texte sophistiqué comme `sequential_summarize`.
*   Interagir avec les services de génération Texte-vers-Image gérés par votre backend `lollms`.
*   Utiliser directement divers backends LLM (comme Ollama, OpenAI) via le système de liaison du client.
*   Utiliser efficacement le streaming pour des applications réactives.
*   Comprendre comment fournir des entrées multimodales (texte + images) à des modèles capables.

`lollms-client` agit comme un puissant orchestrateur, simplifiant l'accès à diverses fonctionnalités d'IA. Cette capacité à contrôler et combiner par programmation différents services d'IA est la clé pour construire des applications innovantes et intelligentes.

**Et Ensuite ? RAG et GraphRAG avec `safe_store` !**
Dans le prochain module, nous explorerons une technique essentielle pour améliorer les performances et la fiabilité des LLM : la **Génération Augmentée par Récupération (RAG)**. Nous verrons comment fournir aux LLM des connaissances externes à partir de vos propres sources de données. Nous examinerons spécifiquement `GraphRAG`, une forme plus avancée utilisant des graphes de connaissances, et présenterons la bibliothèque `safe_store` comme un outil potentiel pour gérer et interroger les données utilisées dans les systèmes RAG.

Préparez-vous à rendre vos LLM plus intelligents avec des connaissances personnalisées dans :ref:`module12-rag-graphrag-safestore-fr` !