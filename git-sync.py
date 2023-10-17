# Import required modules
import git
import os
import tempfile
import argparse

# Function to sync a single repository
def sync_repo(source_repo_url, destination_repo_url):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Try to clone the source repository into the temporary directory
        try:
            print(f"Cloning source repository {source_repo_url}...")
            git.Repo.clone_from(source_repo_url, tmpdirname)
        except Exception as e:
            print(f"Error cloning source repository: {e}")
            return

        # Change directory to the cloned repository
        os.chdir(tmpdirname)

        # Try to push the repository to the destination
        try:
            print(f"Pushing to destination repository {destination_repo_url}...")
            repo = git.Repo(tmpdirname)
            remote = repo.create_remote('destination', destination_repo_url)
            remote.push(mirror=True)
        except Exception as e:
            print(f"Error pushing to destination repository: {e}")
            return

# Main execution starts here
if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description='Sync source repository to destination repository.')
    parser.add_argument('--source', required=True, help='Source repository URL')
    parser.add_argument('--destination', required=True, help='Destination repository URL')
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Perform the sync using the provided source and destination URLs
    sync_repo(args.source, args.destination)
