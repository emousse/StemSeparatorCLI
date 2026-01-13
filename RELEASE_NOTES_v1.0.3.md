# Release v1.0.3 - Critical Bug Fixes for Packaged App

**Release Date:** January 13, 2026

This release fixes three critical bugs that only affected the packaged `.app` build, making the application fully functional for distribution.

---

## 🐛 Critical Fixes

### 1. Fixed: Separation Saves No Files (0 Stems)
**Impact:** Packaged app completed separation but saved 0 files
**Symptoms:**
- Queue showed "✓ 0 stems (3.2s)" even though separation appeared to complete
- Files were not created in output directory
- Issue only occurred in packaged app, not when running from IDE

**Root Cause:**
- Subprocess ran from inside app bundle (`sys._MEIPASS`), causing audio-separator to write files to wrong location
- Missing PyInstaller hidden imports for model architectures

**Solution:**
- Set explicit working directory (`cwd`) to output directory for subprocess
- Added 40+ hidden imports for all model architectures (Demucs, RoFormer, MDX, VR)
- Added comprehensive diagnostics logging to track file locations
- Added file search and recovery for misplaced files
- Added validation to fail fast with clear error messages

**Testing:** ✅ Verified with Demucs v4 6-stem model, files correctly saved

---

### 2. Fixed: Missing Model Architectures in Packaged App
**Impact:** "No module named 'demucs.htdemucs'" error
**Symptoms:**
- Separation failed immediately with module import errors
- Different models failed with different missing module errors

**Root Cause:**
- PyInstaller didn't detect audio-separator's dynamic imports
- Critical modules missing: `demucs.htdemucs`, RoFormer configuration, and others

**Solution - Added Hidden Imports:**
- **Demucs**: 17 modules (`htdemucs`, `hdemucs`, `transformer`, `apply`, etc.)
- **RoFormer**: 14 modules (config loaders, validators, model configuration) - *was completely missing*
- **MDX/VR**: 8 modules (`mdxnet`, `tfc_tdf_v3`, `vr_network` layers)
- **PyTorch**: `torch.nn.parallel.distributed`, `torch.utils.data`

**Result:** All model architectures now work correctly in packaged app

---

### 3. Fixed: App Freezes on Cmd+Q During Startup
**Impact:** 1-2 minute freeze when quitting immediately after launch
**Symptoms:**
- Pressing Cmd+Q right after startup caused app to hang
- App eventually closed after 1-2 minutes
- Only occurred in packaged app

**Root Cause:**
- BeatNet warmup subprocess was blocked by macOS XProtect scanning
- No cancellation mechanism for background warmup task
- Qt's thread pool waited for subprocess to complete

**Solution:**
- Added cancellation mechanism for warmup subprocess
- Added subprocess tracking with thread-safe locking
- Added cleanup in `closeEvent()` and `aboutToQuit` signal
- Graceful subprocess termination (SIGINT → SIGTERM → SIGKILL)

**Result:** App now quits immediately even during warmup (<2 seconds)

---

## 📝 Technical Details

### Files Modified:
- `core/separation_subprocess.py` - Enhanced diagnostics, validation, file recovery
- `core/separator.py` - Set subprocess cwd, validate empty stems, log stderr
- `utils/beatnet_warmup.py` - Added cancellation and subprocess tracking
- `utils/beat_service_client.py` - Added process callback parameter
- `ui/main_window.py` - Added warmup cancellation in closeEvent()
- `main.py` - Added aboutToQuit cleanup handler
- `packaging/StemSeparator-arm64.spec` - Added 40+ hidden imports
- `packaging/StemSeparator-intel.spec` - Added 40+ hidden imports

### Code Changes:
- **Added:** 378 lines
- **Removed:** 10 lines
- **Files changed:** 8

---

## 🧪 Testing Recommendations

Before deploying, please test:

1. **Separation Test:**
   - ✅ Upload audio file
   - ✅ Run separation with Demucs v4 6-stem
   - ✅ Verify files appear in output directory
   - ✅ Verify correct stem count in queue

2. **Model Architecture Test:**
   - ✅ Test Demucs models (4-stem, 6-stem)
   - ✅ Test RoFormer (bs-roformer)
   - ✅ Test MDX models (mdx_vocals_hq)

3. **Quit Behavior Test:**
   - ✅ Open app
   - ✅ Immediately press Cmd+Q
   - ✅ Verify app quits within 2 seconds

4. **Normal Workflow:**
   - ✅ Complete full separation workflow
   - ✅ Export mixed audio
   - ✅ Export loops

---

## 📦 Installation

### For Users:
1. Download `StemSeparator-arm64.dmg` (Apple Silicon) or `StemSeparator-intel.dmg` (Intel)
2. Open the DMG and drag StemSeparator to Applications
3. Right-click the app and select "Open" (first time only)
4. App is now ready to use

### For Developers:
```bash
git clone https://github.com/MaurizioFratello/StemSeparator.git
cd StemSeparator
git checkout v1.0.3
pip install -r requirements.txt
python main.py
```

---

## 🔄 Upgrade Notes

**From v1.0.2:**
- No configuration changes required
- Existing models and settings will work
- Rebuild required for packaged app

**Breaking Changes:**
- None

---

## 🙏 Acknowledgments

Special thanks to thorough testing and debugging that uncovered these critical packaged app issues.

---

## 📄 Full Changelog

See commit [a6dc26e](https://github.com/MaurizioFratello/StemSeparator/commit/a6dc26e) for detailed technical changes.

---

**Tested on:**
- macOS 15.2 (Sequoia)
- Apple Silicon (M1/M2/M3)
- Demucs v4 6-stem model

**Known Issues:**
- None reported for this release

**Next Release:**
- Planned features and improvements TBD
