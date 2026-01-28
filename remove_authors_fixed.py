#!/usr/bin/env python3
"""
Fixed Script to Remove Specific Author Papers and Renumber References
====================================================================
Removes papers by M. Nasir, D.-N. Nguyen, and S. G. K. Patro
Then renumbers all remaining references sequentially.
"""

import re
from pathlib import Path

# References to remove (OLD numbers)
REFS_TO_REMOVE = {5, 16, 28, 31, 34, 36, 38}

def create_renumbering_map():
    """Create mapping from old ref numbers to new ref numbers."""
    mapping = {}
    new_num = 1
    
    for old_num in range(1, 53):  # ref1 to ref52
        if old_num in REFS_TO_REMOVE:
            mapping[f'ref{old_num}'] = None  # Mark as removed
        else:
            mapping[f'ref{old_num}'] = f'ref{new_num}'
            new_num += 1
    
    return mapping

def read_file(filepath):
    """Read the LaTeX file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def remove_bibliography_entries(content, refs_to_remove):
    """Remove bibliography entries for specified references."""
    lines = content.split('\n')
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line contains a bibitem to remove
        should_skip = False
        for ref_num in refs_to_remove:
            if f'\\bibitem{{ref{ref_num}}}' in line:
                should_skip = True
                # Skip this line and the next blank line if exists
                i += 1
                if i < len(lines) and lines[i].strip() == '':
                    i += 1
                break
        
        if not should_skip:
            new_lines.append(line)
            i += 1
    
    return '\n'.join(new_lines)

def update_content_with_mapping(content, mapping):
    """Update both citations and bibliography labels with new mapping."""
    
    # Process in reverse order to avoid conflicts (ref52 before ref5)
    sorted_refs = sorted(mapping.items(), key=lambda x: int(x[0][3:]), reverse=True)
    
    for old_ref, new_ref in sorted_refs:
        if new_ref is None:
            # Remove citations to deleted references
            # Pattern: \cite{refX}
            pattern = r'~?\\cite\{' + old_ref + r'\}'
            content = re.sub(pattern, '', content)
            
            # Clean up resulting double spaces or spaces before punctuation
            content = re.sub(r'  +', ' ', content)
            content = re.sub(r' +([.,;:])', r'\1', content)
            content = re.sub(r'~([.,;:])', r'\1', content)
        else:
            # Update citations: \cite{refX} -> \cite{refY}
            old_cite = f'\\cite{{{old_ref}}}'
            new_cite = f'\\cite{{{new_ref}}}'
            content = content.replace(old_cite, new_cite)
            
            # Update bibliography labels: \bibitem{refX} -> \bibitem{refY}
            old_bibitem = f'\\bibitem{{{old_ref}}}'
            new_bibitem = f'\\bibitem{{{new_ref}}}'
            content = content.replace(old_bibitem, new_bibitem)
    
    return content

def main():
    """Main execution function."""
    print("="*70)
    print("REMOVING AUTHOR PAPERS AND RENUMBERING REFERENCES")
    print("="*70)
    
    # File paths
    input_file = Path('Amazon_review.tex')
    backup_file = Path('Amazon_review_backup_before_removal.tex')
    output_file = Path('Amazon_review.tex')
    
    # Create backup
    print(f"\n📋 Step 1: Creating backup...")
    content = read_file(input_file)
    write_file(backup_file, content)
    print(f"   ✓ Backup saved: {backup_file}")
    
    # Create renumbering map
    print(f"\n📊 Step 2: Creating renumbering map...")
    mapping = create_renumbering_map()
    print(f"   ✓ Mapping created")
    print(f"   • Removing: ref{', ref'.join(map(str, sorted(REFS_TO_REMOVE)))}")
    print(f"   • Renumbering: 52 refs → 45 refs")
    
    # Show some mappings
    print(f"\n   Sample mappings:")
    for old_num in [1, 4, 5, 6, 15, 16, 17, 27, 28, 29, 50, 51, 52]:
        old_ref = f'ref{old_num}'
        new_ref = mapping[old_ref]
        if new_ref is None:
            print(f"   • {old_ref} → REMOVED")
        else:
            print(f"   • {old_ref} → {new_ref}")
    
    # Remove bibliography entries first
    print(f"\n🗑️  Step 3: Removing bibliography entries...")
    content = remove_bibliography_entries(content, REFS_TO_REMOVE)
    print(f"   ✓ Removed {len(REFS_TO_REMOVE)} bibliography entries")
    
    # Update all citations and bibliography labels
    print(f"\n🔄 Step 4: Updating citations and renumbering...")
    content = update_content_with_mapping(content, mapping)
    print(f"   ✓ Updated all citations and bibliography labels")
    
    # Save updated file
    print(f"\n💾 Step 5: Saving updated file...")
    write_file(output_file, content)
    print(f"   ✓ Saved: {output_file}")
    
    # Verify
    print(f"\n🔍 Step 6: Verifying...")
    final_content = read_file(output_file)
    bibitem_count = len(re.findall(r'\\bibitem\{ref\d+\}', final_content))
    cite_count = len(re.findall(r'\\cite\{ref\d+\}', final_content))
    print(f"   ✓ Bibliography entries: {bibitem_count}")
    print(f"   ✓ Citations in text: {cite_count}")
    
    # Summary
    print("\n" + "="*70)
    print("✅ COMPLETION SUMMARY")
    print("="*70)
    print(f"Removed Authors:")
    print(f"  • M. Nasir (3 papers): ref5, ref31, ref34")
    print(f"  • D.-N. Nguyen (2 papers): ref16, ref38")
    print(f"  • S. G. K. Patro (2 papers): ref28, ref36")
    print(f"\nReferences:")
    print(f"  Before: 52 references")
    print(f"  After:  45 references")
    print(f"  Removed: 7 references")
    print(f"\nVerification:")
    print(f"  Bibliography entries: {bibitem_count} (expected: 45)")
    print(f"  Citations in text: {cite_count}")
    print(f"\nFiles:")
    print(f"  ✓ Backup: {backup_file}")
    print(f"  ✓ Updated: {output_file}")
    print(f"\nNext Steps:")
    print(f"  1. Review the changes in {output_file}")
    print(f"  2. Compile LaTeX: pdflatex Amazon_review.tex (run twice)")
    print(f"  3. Check PDF for correctness")
    print("="*70)
    
    # Create detailed mapping file
    mapping_file = Path('reference_renumbering_map.txt')
    with open(mapping_file, 'w') as f:
        f.write("Reference Renumbering Map\n")
        f.write("="*50 + "\n\n")
        f.write("Old Ref → New Ref\n")
        f.write("-"*50 + "\n")
        for old_num in range(1, 53):
            old_ref = f'ref{old_num}'
            new_ref = mapping[old_ref]
            if new_ref is None:
                f.write(f"{old_ref:6s} → REMOVED\n")
            else:
                f.write(f"{old_ref:6s} → {new_ref}\n")
    
    print(f"\n📋 Detailed mapping saved: {mapping_file}")
    print("\n✨ Done!")

if __name__ == '__main__':
    main()
