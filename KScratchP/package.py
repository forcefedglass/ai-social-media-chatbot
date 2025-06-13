#!/usr/bin/env python3
"""
Packaging script for KScratchP Krita plugin.
Creates a ZIP file containing all necessary files for installation.
"""

import os
import zipfile
import sys
from pathlib import Path

def create_plugin_package(output_dir='dist'):
    """
    Create a ZIP package of the KScratchP plugin.
    
    Args:
        output_dir (str): Directory where the ZIP file will be created
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Define the files to include
        files_to_package = [
            '__init__.py',
            'kscratchp.py',
            'kscratchp_widget.py',
            'kscratchp_utils.py',
            'kscratchp.desktop',
            'README.md',
            'LICENSE'
        ]
        
        # Create ZIP file
        zip_path = os.path.join(output_dir, 'KScratchP.zip')
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Add each file to the ZIP
            for file in files_to_package:
                if os.path.exists(file):
                    # Create the correct path in the ZIP file
                    zip_path = os.path.join('kscratchp', file)
                    zf.write(file, zip_path)
                else:
                    print(f"Warning: File {file} not found")
        
        print(f"\nPackage created successfully: {zip_path}")
        print("\nInstallation Instructions:")
        print("1. Extract the ZIP file to your Krita resources folder:")
        print("   - Windows: %APPDATA%\\krita\\pykrita\\")
        print("   - Linux: ~/.local/share/krita/pykrita/")
        print("   - macOS: ~/Library/Application Support/Krita/pykrita/")
        print("2. Restart Krita")
        print("3. Enable the plugin in Settings > Configure Krita > Python Plugin Manager")
        print("4. Restart Krita again")
        
    except Exception as e:
        print(f"Error creating package: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    create_plugin_package()
