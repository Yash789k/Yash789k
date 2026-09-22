# Profile maintenance

This is the public profile repository for [Yash789k](https://github.com/Yash789k). The README appears on the account overview.

## Editing

- **Biography, links, and featured-project descriptions:** edit `README.md`.
- **Terminal header, project cards, toolbox, and snapshot layout:** edit `scripts/render_profile.py` and run `python3 scripts/render_profile.py`.
- **Offline preview:** run `python3 scripts/render_profile.py --offline` to use the saved public metadata.
- **Contribution snake:** color options live in `.github/workflows/profile-visuals.yml`.

The README preserves the learning interests, hobby, and contact information from the previous profile. Project descriptions reflect the linked public repositories. No private repository names or activity are published by the statistics script.

## Automatic updates

The workflow runs daily at 03:27 UTC, on changes to the renderer/workflow, or manually from Actions → Refresh profile visuals → Run workflow. GitHub schedules can be delayed and can become disabled after repository inactivity; manual dispatch remains available. A failed update keeps the last committed images available. The snapshot date makes its age visible.

The workflow uses a standard Ubuntu runner, Python’s standard library, and GitHub’s automatically supplied repository token. It does not require a personal access token, external secrets, paid APIs, a database, or deployed web service. No workflow caches or uploaded artifacts are retained. Only generated files under `assets/` are committed by the bot.

Public repository counts include public forks; “original projects” excludes forks, empty repositories, and the profile repository. Languages count the primary language of each original project, not bytes or expertise. Recent-project timestamps reflect repository pushes, not claims about the author of every commit. The snake visualizes the contribution calendar returned by GitHub; profile visibility settings apply.

## Features and sources

- [GitHub profile READMEs](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [GitHub image theme support](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-images)
- [Platane/snk](https://github.com/Platane/snk), pinned to commit `d8f6715049803e982ee5ff501b6b9b7d5deeb09b`, generates the contribution animation.
- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats) was evaluated; repository-owned snapshot images avoid relying on its best-effort public image server.
- [GitHub scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

The custom SVG artwork uses no scripts, external fonts, tracking pixels, or embedded foreign objects. The header has a reduced-motion CSS fallback. GitHub controls its own page layout and image caching, so this is a profile README design, not a custom GitHub theme.
