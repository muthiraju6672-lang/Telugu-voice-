import os
import zipfile

def create_project_zip(output_path):
    # Exclude directories
    exclude_dirs = {
        'node_modules', '.git', '.playwright-cli', 'dist', '__pycache__',
        '.cache', '.npm', '.aistudio'
    }
    exclude_files = {
        'output_path', 'bun.lock', '.DS_Store'
    }

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            # Modify dirs in-place to avoid descending into excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
            
            for file in files:
                if file in exclude_files or file.endswith('.zip') or file.endswith('.pyc') or file.startswith('.tmp'):
                    continue
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, os.path.join('telugu-real-voice-ai', rel_path))

    print(f"Created zip archive: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    dest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'telugu-real-voice-ai-source.zip'))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    create_project_zip(dest)
