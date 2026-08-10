# thedurdencompany-site

The public website for thedurdencompany.com.

The whole site is a single file: `index.html`. Edit that file, commit, and push in
GitHub Desktop. A GitHub Action then republishes the site to the existing
"the-durden-company" Cloudflare Pages project, and thedurdencompany.com updates
automatically within a minute or two. No more zip uploads.

## One-time setup

1. Create this repo on GitHub (named `thedurdencompany-site`) and add these files.
2. In the repo on GitHub.com: Settings > Secrets and variables > Actions > New
   repository secret.
   - Name: `CLOUDFLARE_API_TOKEN`
   - Value: the Cloudflare API token (provided separately)
3. Push to the `main` branch. The Action runs automatically and deploys.

## How deploys work

- `index.html` is the site.
- `.github/workflows/deploy.yml` runs `wrangler pages deploy` to the
  `the-durden-company` project on every push to `main`.
- The custom domains (thedurdencompany.com + www) are attached to that same
  project, so they pick up each new deploy with no DNS changes.
