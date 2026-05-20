# briefing-post — POST the session briefing to Mattermost

`python -m memory_system.events.cli briefing-post` renders the
briefing (the same one `briefing` prints to stdout) and POSTs it to a
Mattermost incoming webhook. Pure stdlib, zero new dependencies.

## Quickstart

```bash
export MATTERMOST_BRIEFING_WEBHOOK_URL='https://mattermost.example.com/hooks/abc...'

# Preview what would land — no HTTP call
python -m memory_system.events.cli briefing-post --lookback-days 1 --dry-run

# Real post (defaults: lookback 1 day, username "Briefing Bot",
# emoji :calendar:, channel from the webhook config)
python -m memory_system.events.cli briefing-post --lookback-days 1
```

## Flags

| flag | default | purpose |
|------|---------|---------|
| `--lookback-days` | 1 | window for the briefing (daily cron default) |
| `--webhook-url` | env | overrides env lookup |
| `--channel` | webhook default | override channel (e.g. `town-square`) |
| `--username` | `Briefing Bot` | post author display name |
| `--icon-emoji` | `:calendar:` | post avatar emoji shortcode |
| `--dry-run` | off | compute + chunk but skip the HTTP POST |
| `--log-dir` | `memory_system/events/log` | JSONL directory |

## Webhook URL resolution

In order of precedence:

1. `--webhook-url` argument
2. `MATTERMOST_BRIEFING_WEBHOOK_URL` env (more specific — preferred for cron)
3. `MATTERMOST_WEBHOOK_URL` env

If none are set, the command exits with code 2 and a clear message.

## Chunking

Mattermost has a ~16k char post limit. `briefing-post` splits the
briefing on blank-line boundaries (preserves markdown structure),
falling back to hard splits only if a single paragraph exceeds the
chunk size. Chunks after the first are prefixed with `_(continued
N/M)_` so they read in order in the channel.

## Scheduling

### Linux / macOS — crontab

```cron
# 9 AM weekdays, Eastern time
0 9 * * 1-5  TZ='America/New_York' \
  /usr/bin/env MATTERMOST_BRIEFING_WEBHOOK_URL='https://...' \
  /usr/bin/python3 -m memory_system.events.cli briefing-post \
    --lookback-days 1 \
    --log-dir /path/to/OPALproject/memory_system/events/log \
  >> /var/log/opal-briefing.log 2>&1
```

### Windows — Task Scheduler

```powershell
$action = New-ScheduledTaskAction -Execute 'python.exe' `
  -Argument '-m memory_system.events.cli briefing-post --lookback-days 1' `
  -WorkingDirectory 'G:\Downloads\OPALproject'

$trigger = New-ScheduledTaskTrigger -Daily -At 9am -DaysOfWeek Mon,Tue,Wed,Thu,Fri

Register-ScheduledTask -TaskName 'OPAL Briefing Post' `
  -Action $action -Trigger $trigger
```

(set `MATTERMOST_BRIEFING_WEBHOOK_URL` in the user / system environment beforehand.)

### Inside the Node bot (alternative)

The bot in `bots/gtm/` is already a long-running process with
`node-cron` available. To schedule the briefing from there, shell
out to the Python CLI:

```js
import cron from 'node-cron';
import { exec } from 'node:child_process';

cron.schedule('0 9 * * 1-5', () => {
  exec(
    'python -m memory_system.events.cli briefing-post --lookback-days 1',
    { env: process.env },
    (err, stdout, stderr) => {
      if (err) console.error('briefing failed:', stderr);
      else console.log('briefing posted:', stdout.trim());
    },
  );
}, { timezone: 'America/New_York' });
```

This keeps the briefing inside the bot's existing lifecycle but adds
no new Python ↔ Node coupling beyond the subprocess call.

## What this composes with

- **`memory_system.events.cli briefing`** — same briefing rendered to
  stdout / file; share the rendering code so the briefing you preview
  is the briefing that posts.
- **`bots/gtm/daily-digest.js`** — separate, complementary. The
  advisory-board digest is LLM-generated interpretation; this
  briefing-post is raw memory-log signal. They are useful side-by-side,
  not as substitutes.
