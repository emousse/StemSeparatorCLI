# Stem Separator v1.0.2

**Bug Fix Release - Export Loops Time-Stretched Fix**

This release fixes a critical bug in the Export Loops widget where the "Use Time-Stretched Loops" checkbox was not working correctly.

## 🐛 What Was Fixed

### Export Loops Widget - Time-Stretched Loops Export
- **Fixed**: "Use Time-Stretched Loops" checkbox now correctly switches between time-stretched and original loops
- **Fixed**: Export now properly uses time-stretched loops from the Looping tab cache when checkbox is enabled
- **Fixed**: Loop segment inconsistency between Looping tab and Export Loops tab
- **Fixed**: Stem name normalization for consistent cache access
- **Fixed**: Checkbox state management now aligned with export logic
- **Fixed**: Proper handling of intro loops (leading loops with padding are correctly filtered out)
- **Fixed**: Export aborts with clear warning if time-stretching is incomplete (no silent fallback to original loops)

### Technical Details
- Export widget now uses the same `valid_loops` (filtered to exclude intro loops with negative start times) that were used during time-stretching
- Loop indices now match between time-stretching cache and export logic
- Stem names are normalized to lowercase for consistent cache access
- Works correctly for both export modes (Mixed Audio and Individual Stems)

## 📥 Downloads

Choose the version for your Mac:

- **Apple Silicon (M1/M2/M3)**: Download `StemSeparator-arm64.dmg`
- **Intel Macs**: Download `StemSeparator-intel.dmg` (if available)

### Installation
1. Download the DMG file for your Mac
2. Open the DMG and drag "Stem Separator" to Applications
3. Right-click the app and select "Open" (first time only)

## 🔧 System Requirements

- macOS 10.15 (Catalina) or newer
- 8 GB RAM (16 GB recommended)
- ~1.5 GB storage for models
- Apple Silicon (M1/M2/M3) recommended for best performance

## 📚 Documentation

- **[Changelog](./CHANGELOG.md)**: Full version history
- **[User Guide](./docs/USER_GUIDE.md)**: Complete usage guide
- **[Troubleshooting](./README.md#-troubleshooting)**: Common issues and solutions

## 🙏 Credits

Special thanks to all contributors and testers who helped identify and fix this issue.

---

**Full Changelog**: [v1.0.1...v1.0.2](https://github.com/MaurizioFratello/StemSeparator/compare/v1.0.1...v1.0.2)

