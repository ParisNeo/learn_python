.. _module11-practical-llm-interaction:

==================================================================
Module 11: Advanced LLM Orchestration with `lollms-client`
==================================================================

Welcome to Module 11! We've explored the theoretical aspects of "Vibe Coding" and now it's time to delve deeper into practical, advanced interactions with Large Language Models using the `lollms-client` Python library. This module will go beyond basic text generation, showcasing how `lollms-client` can orchestrate complex tasks such as sequential summarization, text-to-image generation, and direct interaction with various LLM bindings like Ollama or OpenAI, all managed through a `lollms` backend.

This hands-on module will empower you to build sophisticated AI-assisted Python applications.

.. image:: ../_static/images/ai_orchestration.png
   :alt: A conductor (Python script) leading an orchestra of AI models and tools
   :width: 650px
   :align: center

**Important Prerequisites:**
1.  **A running instance of `lollms`:** Your `lollms-webui` (or headless server) must be operational (default: `http://localhost:9600`). For specific features like TTI or direct Ollama/OpenAI binding use, ensure the relevant models and services are correctly configured and active within your `lollms` environment.
2.  **The `lollms-client` library and its dependencies installed.**
3.  **Optional (for specific examples):**
    *   `pipmaster` and `docling` for the summarization example.
    *   `Pillow` (PIL) for image processing in TTI examples.
    *   An Ollama server running if testing the Ollama binding, with models like `llava` or `llama3` pulled.
    *   An OpenAI API key if testing the OpenAI binding.

Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Initialize `LollmsClient` for various backends and specific model interactions.
*   Perform advanced text processing tasks like `sequential_summarize` for large documents.
*   Utilize the Text-to-Image (TTI) capabilities of `lollms-client` to:
    *   List available TTI services.
    *   Get and (conceptually) set TTI service settings.
    *   Generate images from text prompts.
*   Interact directly with different LLM bindings (e.g., `lollms` default, `ollama`, `openai`) through `LollmsClient`.
*   Handle streaming responses effectively with custom callbacks.
*   Integrate multi-modal inputs (text and images) for generation with capable models.
*   Understand the client's error handling and response structures.

----------------------------------------------------

Core `LollmsClient` Initialization and Usage
============================================

The `LollmsClient` is your gateway to the `lollms` backend. Its initialization allows for specifying the host, target model, generation parameters, and even the underlying communication binding.

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

*   The `binding_name` parameter in `LollmsClient` is crucial for telling the client how to communicate and with what type of service (e.g., "lollms" for the standard LoLLMs API, "ollama", "openai").
*   `host_address` and `model_name` are then interpreted based on the chosen binding.

----------------------------------------------------

Advanced Text Processing: Sequential Summarization
==================================================

For very large documents that exceed an LLM's context window, `lollms-client` offers powerful methods like `sequential_summarize`. This breaks the document into manageable chunks, summarizes each chunk iteratively (maintaining context from previous summaries), and then compiles a final summary.

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

*   `sequential_summarize` is ideal for processing texts longer than the LLM's direct context window.
*   `instruction_prompt`: Guides the LLM on how to process each individual chunk and update the rolling summary.
*   `output_format_prompt`: Tells the LLM how to structure the final combined summary.
*   `context_size`, `chunk_size`: Critical parameters to tune based on the LLM you are using with `lollms`.

----------------------------------------------------

Text-to-Image (TTI) Generation
==============================

`lollms-client` can interact with Text-to-Image services configured in your `lollms` backend. This involves listing services, managing settings, and generating images.

.. code-block:: python
    # tti_example.py
    from lollms_client import LollmsClient
    from ascii_colors import ASCIIColors, trace_exception
    from PIL import Image
    from pathlib import Path
    import io
    import os
    import platform # For os.name and platform.system()

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
            exit()

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

*   `lc.tti`: Accesses the Text-to-Image interface of the client.
*   `lc.tti.list_services()`: Informs you about the image generation backends configured in `lollms`.
*   `lc.tti.get_settings()`: Retrieves the configurable parameters for the currently active TTI service.
*   `lc.tti.generate_image(...)`: The core method for image generation, taking prompts, dimensions, and other service-specific parameters.

----------------------------------------------------

Direct Interaction with LLM Bindings (e.g., Ollama, OpenAI)
===========================================================

`LollmsClient` can be initialized to interact with specific bindings, allowing you to leverage models served by Ollama, OpenAI (via API key), or others, all orchestrated through `lollms-client`'s unified API structure.

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

*   By setting `binding_name` during `LollmsClient` initialization, you tell the client which internal binding class to use (e.g., `OllamaBinding`, `OpenAIBinding`).
*   Methods like `generate_text` and `listModels` will then operate in the context of that specific binding.
*   For multi-modal models like LLaVA via Ollama, the `images` parameter of `generate_text` is used.

----------------------------------------------------

Module 11 Summary
=================

This module has equipped you with the knowledge to use `lollms-client` for a range of advanced AI interactions. You've learned to:

*   Initialize `LollmsClient` for different purposes, including targeting specific bindings.
*   Perform sophisticated text processing like `sequential_summarize`.
*   Engage with Text-to-Image generation services managed by your `lollms` backend.
*   Directly utilize various LLM backends (like Ollama, OpenAI) through the client's binding system.
*   Effectively use streaming for responsive applications.
*   Understand how to provide multi-modal inputs (text + images) to capable models.

`lollms-client` acts as a powerful orchestrator, simplifying access to diverse AI functionalities. This ability to programmatically control and combine different AI services is key to building innovative and intelligent applications.

**What's Next? RAG and GraphRAG with `safe_store`!**
In the upcoming module, we will explore a critical technique for enhancing LLM performance and reliability: **Retrieval Augmented Generation (RAG)**. We'll see how to provide LLMs with external knowledge from your own data sources. We'll specifically look at `GraphRAG`, a more advanced form using knowledge graphs, and introduce the `safe_store` library as a potential tool for managing and querying the data used in RAG systems.

Prepare to make your LLMs smarter with custom knowledge in :ref:`module12-rag-graphrag-safestore`!