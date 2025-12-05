# OPAL Developer Worktrees

## Folder Structure

```
G:\Projects\OPALproject\
├── ProjectWork/                    ← master (golden baseline - DO NOT WORK HERE)
├── ProjectWork-jason/              ← Jason's workspace
├── ProjectWork-alex/               ← Alex's workspace
├── ProjectWork-hubert/             ← Hubert's workspace
├── ProjectWork-staging-demo/       ← Demo product staging
└── ProjectWork-staging-enterprise/ ← Enterprise product staging
```

## For Developers (Jason, Alex, Hubert)

### Your Daily Workflow

1. Open your folder in your IDE:
   - Jason: `G:\Projects\OPALproject\ProjectWork-jason`
   - Alex: `G:\Projects\OPALproject\ProjectWork-alex`
   - Hubert: `G:\Projects\OPALproject\ProjectWork-hubert`

2. Work normally - code, build, test

3. Save your work:
   ```bash
   git add .
   git commit -m "what you did"
   git push
   ```

That's it. No branch switching needed.

### Want updates from master? (Optional - only when you want them)

```bash
git fetch origin master
git merge origin/master
```

### Found a bug fix worth sharing?

Tell the team: "commit abc123 in my folder fixes the XYZ issue"

They can cherry-pick it, or the lead can merge it to master.

## For Build Lead

### Merge developer work to master

```bash
cd G:\Projects\OPALproject\ProjectWork
git merge variant/jason   # or cherry-pick specific commits
git push
```

### Promote to staging

```bash
cd G:\Projects\OPALproject\ProjectWork-staging-demo
git merge master
git push
```

### Tag a release

```bash
git tag -a v1.0.0-demo -m "Demo release 1.0.0"
git push origin --tags
```

## Branch Summary

| Folder | Branch | Purpose |
|--------|--------|---------|
| ProjectWork | master | Golden baseline |
| ProjectWork-jason | variant/jason | Jason's work |
| ProjectWork-alex | variant/alex | Alex's work |
| ProjectWork-hubert | variant/hubert | Hubert's work |
| ProjectWork-staging-demo | staging/demo | Demo pre-release |
| ProjectWork-staging-enterprise | staging/enterprise | Enterprise pre-release |
