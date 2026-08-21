# Contributing and Review Workflow

Thank you for helping improve Anthony Durham's robotics program-management portfolio.

## Choose the right path

- Preview only: use the GitHub Pages site. No repository access is needed.
- Feedback only: open a GitHub Issue using the portfolio-review template.
- Proposed improvement: create a branch or fork, make one focused change, and open a Pull Request.
- Direct collaborator: use a named branch and Pull Request. Do not commit directly to `main`.

## Public-content boundary

This repository is recruiter-facing. Never add resumes, private contact information, job-search prompts, credentials, employer/customer confidential information, local Windows paths, application records, or unpublished personal documents.

All scenario names and operational results are fictional. Public source claims need a direct source link. Planning assumptions must be labeled. Percentages must include a denominator or source calculation. Acronyms must be written in full the first time they appear.

## Pull Request checklist

1. Create a branch such as `review/restroom-quality-notes`.
2. Keep the change focused and explain the reason.
3. For any number, identify public benchmark, fictional scenario input, derived calculation, quote-required input, or observed simulation output.
4. Rebuild and validate locally:

   ```text
   python scripts/build_portfolio_site.py
   python scripts/validate_portfolio.py
   ```

5. Inspect affected pages, links, downloads, and videos.
6. Open a Pull Request and complete the template.
7. Anthony reviews and merges; contributor approval does not authorize publication.

## MuJoCo changes

Include the model name/version, changed source files, exact run command, screenshots from relevant cameras, collision or path observations, and whether the motion is scripted, actuated, or controller-driven. Do not describe a visualization as certified autonomy, safety validation, cleaning efficacy, or vendor performance.

