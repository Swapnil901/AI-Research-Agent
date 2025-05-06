from langchain.tools import BaseTool
import requests
import os

class GitHubRepoTool(BaseTool):
    name: str = "GitHubRepoFinder"
    description: str = "Finds popular and relevant GitHub repositories for a given research topic."

    def _run(self, topic: str) -> str:
        query = topic.replace(" ", "+")
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page=10"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ.get('GITHUB_API_KEY')}" if os.environ.get("GITHUB_API_KEY") else None
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"⚠️ GitHub API error: {response.status_code} – {response.text}"

        repos = response.json().get("items", [])
        if not repos:
            return "❌ No relevant GitHub repositories found."

        output = "### 🔗 Top GitHub Repositories:\n\n"
        for repo in repos:
            name = repo["name"]
            url = repo["html_url"]
            stars = repo["stargazers_count"]
            desc = repo["description"] or "No description provided."
            lang = repo["language"] or "N/A"
            updated = repo["updated_at"][:10]
            output += (
                f"- **[{name}]({url})** ⭐ {stars} | 🖥️ {lang} | 📅 Last updated: {updated}\n"
                f"  - {desc}\n\n"
            )
        return output

    def _arun(self, topic: str) -> str:
        raise NotImplementedError("Async not supported.")
