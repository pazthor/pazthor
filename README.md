## Julio Pastor

Full Stack Engineer with a Computer Science background, passionate about building scalable software solutions.

### About
I'm currently seeking new opportunities to apply my expertise in full-stack development and software architecture. Beyond coding, I enjoy rock climbing and playing guitar.

### Connect
- [GitHub Repositories][repos]
- [LinkedIn Profile][linkedin]
- [Twitter](https://twitter.com/pazthor)

[repos]: https://github.com/pazthor?tab=repositories
[linkedin]: https://www.linkedin.com/in/pazthor/

## Commit Overview Tool

A Python utility for aggregating and summarizing recent commits across GitHub and GitLab projects.

### Usage

```bash
python commit_overview.py \
  --github-token YOUR_GITHUB_TOKEN \
  --github-owner YOUR_GITHUB_USER \
  --github-repo YOUR_GITHUB_REPO \
  --gitlab-token YOUR_GITLAB_TOKEN \
  --gitlab-project YOUR_GITLAB_PROJECT_ID
```

The script retrieves the latest commits from both platforms and generates a consolidated summary.

#### AI-Powered Summaries

For enhanced commit analysis, provide an OpenAI API key using the `--openai-key` parameter. This enables automatic generation of intelligent summaries from commit messages.

### GitHub Actions Integration

This repository includes an automated workflow at `.github/workflows/commit_overview.yml` for scheduled execution.

#### Configuration

Configure the following repository secrets:
- `GITHUB_TOKEN` - GitHub personal access token
- `GITHUB_OWNER` - GitHub username or organization
- `GITHUB_REPO` - Repository name
- `GITLAB_TOKEN` - GitLab personal access token
- `GITLAB_PROJECT` - GitLab project ID
- `OPENAI_API_KEY` - (Optional) OpenAI API key for AI summaries

The workflow can be triggered manually from the Actions tab or configured for automatic execution.
