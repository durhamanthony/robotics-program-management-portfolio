# Collaboration Guide for the Repository Owner

## Safest access model

1. Send reviewers the public website link. They do not need GitHub access.
2. Ask feedback-only reviewers to open an Issue.
3. Ask occasional contributors to fork the public repository and submit a Pull Request.
4. Invite only trusted co-builders as collaborators because a collaborator on a personal-account repository can push changes.
5. Require changes to `main` to come through a Pull Request and review them before merge.

## Repository separation

- `robotics-program-management-portfolio`: public, recruiter-facing, fictional scenarios, completed artifacts, simulations, and generated website.
- `anthony-career-workspace`: private, career strategy, resumes, prompts, source research, publishing work, and editable working material.

Never invite a portfolio reviewer to the private career workspace unless that person specifically needs all of its contents and is trusted with write access.

## Suggested collaborator process

- Branch name: `name/short-change`, for example `alex/airport-risk-review`.
- One topic per Pull Request.
- Anthony remains Code Owner and publication approver.
- Delete the branch after merge.
- Remove collaborator access when the work ends.
- Audit `Settings` → `Collaborators` periodically.

