📚 **Wikipedia Microservice using Python and FastAPI**

**Overview:**
This repository houses a lightweight microservice that leverages Python and FastAPI to harness the power of Wikipedia's vast knowledge base. 🌍

**Features:**
- 📖 **Wikipedia Page Retrieval:** Utilize the `/wiki/{name}` endpoint to fetch information on a specific topic from Wikipedia. Just provide the desired topic, and you'll receive a concise summary.

- 🔎 **Search Wikipedia:** Access the `/search/{value}` endpoint to perform Wikipedia searches with ease. Retrieve a list of relevant pages based on your query.

- 💬 **Phrase Extraction:** Need insights beyond the summary? The `/phrases/{phrase}` endpoint extracts noun phrases from Wikipedia pages, providing you with a deeper understanding of the content.

**Getting Started:**
1. Clone the repository to your local environment.
2. Run `make install` to install the necessary dependencies.
3. Use `make run` to start the microservice locally. It will be accessible at `http://127.0.0.1:8080`.

**Docker Support:**
- Deploy the microservice as a Docker container with `make build` and `make deploy`. It will be available on port 8080.

**Testing:**
- Verify the microservice's functionality by running `make test`. Comprehensive tests are included to ensure reliability.

**Development Tools:**
- Code formatting is handled by Black (`make format`) to maintain clean and consistent code.
- Linting using pylint (`make lint`) ensures code quality and adherence to best practices.

Explore the vast world of knowledge through this Wikipedia microservice! 📚🌐
