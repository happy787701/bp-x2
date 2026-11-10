# BP-X2 की मुख्य सेटिंग्स

MODELS = {
    "coder": "Qwen/Qwen2.5-Coder-7B-Instruct",
    "general": "meta-llama/Meta-Llama-3-8B-Instruct",
}

# तीन मोड
MODES = ["coder", "general", "mixed"]

# रनटाइम प्लेटफ़ॉर्म (क्रम से आज़माए जाएँगे)
RUNTIMES = ["colab", "kaggle", "lightning"]
