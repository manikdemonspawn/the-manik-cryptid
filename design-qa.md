# Nexus reconstruction QA

Reference: user-supplied Fairy Forest Nexus screenshot (`1000016424.png`), with `1000016423.png` used only for supporting realm-directory structure.

## Implemented

- Replaced the construction-stage placeholder with `assets/images/nexus/nexus-master-v1.png`.
- Added eight semantic, keyboard-focusable HTML realm links over the image.
- Added a non-visual realm directory, separate Katakombs descent, and a clear posthumous-only Mausoleum note.
- Preserved all eight primary realm destinations and the Apothekary's physical nesting under the Kurio Shop.

## Static checks

- HTML asset reference resolves locally.
- All realm destinations in the new Nexus map resolve locally.
- The map has exactly eight primary realm links and the directory has exactly eight matching cards.
- No active Mausoleum destination was added.
- `visual-targets.json` parses after recording the new image as a local review candidate, not an approved lore artifact.

## Visual comparison

Prototype capture is blocked: this session has no permitted local/cloud browser path for opening the un-deployed construction files. The build must not be described as visually verified until the construction preview is opened in a permitted browser and compared against the reference at desktop and mobile widths.

final result: blocked
