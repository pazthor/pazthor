### Julio Pastor 👋

Hey, I'm a Full Stack Engineer coming from Computer Science background


- 🔭 I’m currently looking for a new oportunities. 
- 🌱 I’m currently learning climb stuff, play guitar & software architecture. 
- 😄 Pronouns: he/him

You can  explore my [repositories][repos], my [LinkedIn profile][linkedin], or just send me a [mention](https://twitter.com/pazthor) on Twitter.

[repos]: https://github.com/pazthor?tab=repositories
[linkedin]: https://www.linkedin.com/in/pazthor/

## Commit overview

Use `commit_overview.py` to print recent commits from your GitHub and GitLab projects.

```bash
python commit_overview.py \
  --github-token YOUR_GITHUB_TOKEN \
  --github-owner YOUR_GITHUB_USER \
  --github-repo YOUR_GITHUB_REPO \
  --gitlab-token YOUR_GITLAB_TOKEN \
  --gitlab-project YOUR_GITLAB_PROJECT_ID
```

The script fetches the latest commits from each platform and prints a short summary.

If you provide an OpenAI API key via `--openai-key`, the script will also
generate an AI summary of the commit messages.

### Running in GitHub Actions

This repository includes a workflow in `.github/workflows/commit_overview.yml`
that runs the script. Configure the required secrets (`GITHUB_TOKEN`,
`GITHUB_OWNER`, `GITHUB_REPO`, `GITLAB_TOKEN`, `GITLAB_PROJECT`, and optionally
`OPENAI_API_KEY`) and trigger the workflow manually from the Actions tab.
