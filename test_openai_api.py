
"""
Standalone OpenAI API diagnostic for the Agentic RAG project.

Tests:
1. Whether the API key is loaded from Settings.
2. Whether the chat model is accessible.
3. Whether the embedding model is accessible.
4. The actual HTTP status and API error body on failure.

This script does not modify your application or database.
"""
import traceback    
import sys
from openai import OpenAI, APIStatusError, APIConnectionError
from app.core.config import get_settings


def print_result(name: str, success: bool, details: str) -> None:
    status = "PASS" if success else "FAIL"
    print(f"\n[{status}] {name}")
    print(details)


def main() -> None:
    print("=" * 60)
    print("OPENAI API DIAGNOSTIC")
    print("=" * 60)

    # Load settings using your existing configuration.
    settings = get_settings()

    print("\nConfiguration")
    print("-" * 40)
    print(f"Environment: {settings.app_env}")
    print(f"Chat model: {settings.openai_model}")
    print(f"Embedding model: {settings.embedding_model}")
    print(f"API key loaded: {bool(settings.openai_api_key.strip())}")

    if not settings.openai_api_key.strip():
        print_result(
            "API key configuration",
            False,
            "No API key was loaded. Check OPENAI_API_KEY in your .env file.",
        )
        sys.exit(1)

    # Disable automatic retries so the original error is easier to diagnose.
    client = OpenAI(
        api_key=settings.openai_api_key.strip(),
        max_retries=0,
        timeout=30.0,
    )

    # Test 1: Chat completions.
    print("\n" + "=" * 60)
    print("TEST 1: CHAT COMPLETION")
    print("=" * 60)

    try:
        response = client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: API_TEST_OK",
                }
            ],
            max_tokens=20,
        )

        answer = response.choices[0].message.content
        print_result(
            "Chat API",
            True,
            f"Model responded successfully.\nResponse: {answer}",
        )

    except APIStatusError as exc:
        print(f"Error type: {type(exc).__name__}")
        print(f"Underlying cause: {repr(exc.__cause__)}")

        if exc.__cause__ is not None:
            traceback.print_exception(exc.__cause__)

    except APIConnectionError as exc:
        print(f"Error type: {type(exc).__name__}")
        print(f"Underlying cause: {repr(exc.__cause__)}")
        
        if exc.__cause__ is not None:
            traceback.print_excep 

    except Exception as exc:
        print_result(
            "Chat API",
            False,
            f"Unexpected error: {type(exc).__name__}: {exc}",
        )

    # Test 2: Embeddings.
    print("\n" + "=" * 60)
    print("TEST 2: EMBEDDINGS")
    print("=" * 60)

    try:
        response = client.embeddings.create(
            model=settings.embedding_model,
            input="Testing the IT Support Agentic RAG API.",
        )

        vector = response.data[0].embedding

        print_result(
            "Embedding API",
            True,
            f"Embedding generated successfully.\n"
            f"Vector dimensions: {len(vector)}",
        )

    except APIStatusError as exc:
        print_result(
            "Embedding API",
            False,
            f"HTTP status: {exc.status_code}\n"
            f"Response body: {exc.response.text}",
        )

    except APIConnectionError as exc:
        print_result(
            "Embedding API",
            False,
            f"Connection failed: {type(exc).__name__}: {exc}",
        )

    except Exception as exc:
        print_result(
            "Embedding API",
            False,
            f"Unexpected error: {type(exc).__name__}: {exc}",
        )

    print("\n" + "=" * 60)
    print("DIAGNOSTIC FINISHED")
    print("=" * 60)
    print("Never share your API key or paste it into diagnostic logs.")


if __name__ == "__main__":
    main()
