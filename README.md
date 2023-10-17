# GitLab CI/CD Configuration for Repository Sync

This repository contains a `.gitlab-ci.yml` file configured to sync a source repository to a destination repository.

## How it Works

1. **Initialization**: The script initializes an SSH agent and adds the necessary SSH keys.
2. **Preparation**: The script sets up the environment, including SSH configurations and known hosts.
3. **Execution**: A Python script `git-sync.py` performs the actual syncing of the repositories.

## Variables

- `GIT_STRATEGY`: Git strategy used for checking out the code. Set to `clone`.
- `SOURCE_REPO`: The SSH URL of the source repository.
- `DEST_REPO`: The SSH URL of the destination repository.

## Jobs

### sync_job_1

This is the first job that performs the syncing operation.

#### Script

- Installs necessary Python packages.
- Executes the `git-sync.py` Python script to perform the sync.

## Rules

- The job runs automatically for scheduled pipelines.
- The job can also be triggered manually.

## How to Use

1. Update the `SOURCE_REPO` and `DEST_REPO` variables with your source and destination repository URLs.
2. Make sure that the SSH keys are configured correctly in your GitLab CI/CD settings.
3. Run the pipeline either manually or through a schedule.
