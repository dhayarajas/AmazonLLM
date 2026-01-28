#!/usr/bin/env python3
"""
Script to Remove Specific Author Papers and Renumber References
================================================================
Removes papers by M. Nasir, D.-N. Nguyen, and S. G. K. Patro
Then renumbers all remaining references sequentially.
"""

import re
from pathlib import Path

# References to remove
REFS_TO_REMOVE = [5, 16, 28, 31, 34, 36, 38]

def create_renumbering_map():
    """Create mapping from old ref numbers to new ref numbers."""
    mapping = {}
    new_num = 1
    
    for old_num in range(1, 53):  # ref1 to ref52
        if old_num in REFS_TO_REMOVE:
            mapping[old_num] = None  # Mark as removed
        else:
            mapping[old_num] = new_num
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
    skip_next = False
    
    for i, line in enumerate(lines):
        # Check if this line contains a bibitem to remove
        should_skip = False
        for ref_num in refs_to_remove:
            if f'\\bibitem{{ref{ref_num}}}' in line:
                should_skip = True
                # Also skip the next blank line if it exists
                if i + 1 < len(lines) and lines[i + 1].strip() == '':
                    skip_next = True
                break
        
        if skip_next:
            skip_next = False
            continue
            
        if not should_skip:
            new_lines.append(line)
    
    return '\n'.join(new_lines)

def update_citations(content, mapping):
    """Update all citations in the text with new numbering."""
    # Sort by old number in descending order to avoid conflicts
    # (e.g., ref52 before ref5 to avoid replacing ref5 in ref52)
    sorted_refs = sorted(mapping.items(), key=lambda x: x[0], reverse=True)
    
    for old_num, new_num in sorted_refs:
        if new_num is not None:  # Not removed
            old_cite = f'\\cite{{ref{old_num}}}'
            new_cite = f'\\cite{{ref{new_num}}}'
            content = content.replace(old_cite, new_cite)
        else:  # Removed - should delete these citations
            # Remove citation and clean up extra spaces
            old_cite = f'\\cite{{ref{old_num}}}'
            content = content.replace(old_cite, '')
            # Clean up double spaces
            content = re.sub(r'  +', ' ', content)
            # Clean up space before punctuation
            content = re.sub(r' +([.,;:])', r'\1', content)
    
    return content

def update_bibliography_labels(content, mapping):
    """Update bibliography item labels with new numbering."""
    # Sort by old number in descending order
    sorted_refs = sorted(mapping.items(), key=lambda x: x[0], reverse=True)
    
    for old_num, new_num in sorted_refs:
        if new_num is not None:  # Not removed
            old_label = f'\\bibitem{{ref{old_num}}}'
            new_label = f'\\bibitem{{ref{new_num}}}'
            content = content.replace(old_label, new_label)
    
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
    print(f"   • Removing: ref{', ref'.join(map(str, REFS_TO_REMOVE))}")
    print(f"   • Renumbering: 52 refs → 45 refs")
    
    # Show some mappings
    print(f"\n   Sample mappings:")
    for old_num in [1, 4, 5, 6, 15, 16, 17, 27, 28, 29, 50, 51, 52]:
        new_num = mapping[old_num]
        if new_num is None:
            print(f"   • ref{old_num} → REMOVED")
        else:
            print(f"   • ref{old_num} → ref{new_num}")
    
    # Remove bibliography entries
    print(f"\n🗑️  Step 3: Removing bibliography entries...")
    content = remove_bibliography_entries(content, REFS_TO_REMOVE)
    removed_count = len(REFS_TO_REMOVE)
    print(f"   ✓ Removed {removed_count} bibliography entries")
    
    # Update citations in text
    print(f"\n🔄 Step 4: Updating citations in text...")
    content = update_citations(content, mapping)
    print(f"   ✓ Updated all citations")
    
    # Update bibliography labels
    print(f"\n📝 Step 5: Renumbering bibliography entries...")
    content = update_bibliography_labels(content, mapping)
    print(f"   ✓ Renumbered all bibliography entries")
    
    # Save updated file
    print(f"\n💾 Step 6: Saving updated file...")
    write_file(output_file, content)
    print(f"   ✓ Saved: {output_file}")
    
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
    print(f"\nFiles:")
    print(f"  ✓ Backup: {backup_file}")
    print(f"  ✓ Updated: {output_file}")
    print(f"\nNext Steps:")
    print(f"  1. Review the changes in {output_file}")
    print(f"  2. Compile LaTeX: pdflatex Amazon_review.tex")
    print(f"  3. Check for any orphaned citations")
    print(f"  4. Verify PDF compiles correctly")
    print("="*70)
    
    # Create detailed mapping file
    mapping_file = Path('reference_renumbering_map.txt')
    with open(mapping_file, 'w') as f:
        f.write("Reference Renumbering Map\n")
        f.write("="*50 + "\n\n")
        f.write("Old Ref → New Ref\n")
        f.write("-"*50 + "\n")
        for old_num in range(1, 53):
            new_num = mapping[old_num]
            if new_num is None:
                f.write(f"ref{old_num:2d} → REMOVED\n")
            else:
                f.write(f"ref{old_num:2d} → ref{new_num:2d}\n")
    
    print(f"\n📋 Detailed mapping saved: {mapping_file}")
    print("\n✨ Done!")

if __name__ == '__main__':
    main()
