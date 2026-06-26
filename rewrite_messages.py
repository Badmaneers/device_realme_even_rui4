#!/usr/bin/env python3
"""
Git commit message rewrite filter for Realme even (MT6768) device tree.
Reads original commit message from stdin, outputs rewritten message to stdout.
"""
import sys
import re

def rewrite(msg):
    subject = msg.split('\n', 1)[0] if '\n' in msg else msg
    body = msg[len(subject):] if '\n' in msg else ''

    stripped_subject = subject.strip()

    # ============================================================
    # SPECIFIC COMMIT MESSAGE REWRITES (exact match on subject)
    # ============================================================
    rewrites = {
        "Initial commit.":
            "even: Initial device tree for Realme even (MT6768)",
        "Add NFC support configuration and permissions files":
            "even: Add NFC support configuration and permission files",
        "Add proprietary-files.txt":
            "even: Add initial proprietary files list",
        "Add rro_overlays":
            "even: Add runtime resource overlay (RRO) configuration",
        "Add LOS overlays":
            "even: Add LineageOS overlay configuration",
        "Add rootdir":
            "even: Add root directory configuration and init scripts",
        "Add recovery initialization scripts for MT6768":
            "even: Add recovery initialization scripts for MT6768",
        "Add initialization files for device properties and NFC support":
            "even: Add init files for device properties and NFC support",
        "Add libshim_sink, libjni_shim, and libshim_ui implementations":
            "even: Add libshim_sink, libjni_shim, and libshim_ui shim libraries",
        "Add SELinux policy files for camera, fingerprint, charging, and other vendor services":
            "even: Add SELinux policies for camera, fingerprint, charging, and vendor services",
        "device: Update device.mk and add LiveDisplay HAL service":
            "even: Update device.mk and add LiveDisplay HAL service",
        "Add Bluetooth A2DP packages to device.mk":
            "even: Add Bluetooth A2DP packages to device.mk",
        "device: Update device.mk to include IMS and Pocket Mode support":
            "even: Update device.mk to include IMS and Pocket Mode support",
        "Add Vulkan library to PRODUCT_PACKAGES in device.mk":
            "even: Add Vulkan library to PRODUCT_PACKAGES",
        "Add power scenario configurations, update vendor properties, and modify device.mk for audio and power management":
            "even: Add power scenarios, update vendor properties, and configure audio/power",
        "device: Update blob_fixup function to remove obsolete audio library handling and add power service dependency":
            "even: Update blob_fixup: remove obsolete audio handling, add power service dependency",
        "Remove obsolete libshim_sink files to streamline audio handling":
            "even: Remove obsolete libshim_sink files to streamline audio handling",
        "device: Clean up proprietary files by removing obsolete camera libraries and adding new ones":
            "even: Clean up proprietary files: remove obsolete camera libs and add replacements",
        "device: Remove obsolete camera vendor packages to streamline camera handling":
            "even: Remove obsolete camera vendor packages from PRODUCT_PACKAGES",
        "device: Add Egis HAL for fingerprint sensor support":
            "even: Add Egis HAL for fingerprint sensor support",
        "device: Add new audio libraries and update existing audio hardware files":
            "even: Add new audio libraries and update audio hardware files",
        "device: Add new camera and audio libraries to enhance functionality":
            "even: Add new camera and audio libraries",
        "device: Update graphics composer and add Vulkan support":
            "even: Update graphics composer and add Vulkan support",
        "device: Update vendor properties for graphics and display enhancements":
            "even: Update vendor properties for graphics and display enhancements",
        "device: Enable WFC over IMS and adjust default refresh rates":
            "even: Enable WFC over IMS and adjust default refresh rate",
        "Update README.md with device details and build instructions":
            "even: Update README with device details and build instructions",
        "device: Remove obsolete MtkOmxVdecEx library from proprietary files":
            "even: Remove obsolete MtkOmxVdecEx library from proprietary files",
        "device: Add CRAVE Build Launcher script for streamlined build process":
            "even: Add CRAVE build launcher script for streamlined builds",
        "device: Update crave build script to improve source root handling and output messages":
            "even: Update crave build script: improve source root handling and output messages",
        "device: Enhance crave build script to support listed/unlisted ROMs with repo init logic":
            "even: Enhance crave build script: support listed/unlisted ROMs with repo init",
        "device: Enhance build command to support custom source URLs and improve repo init logic":
            "even: Enhance crave build command: support custom source URLs and improve repo init",
        "device: Add pull commands generator and integrate artifact pulling into build process":
            "even: Add artifact pull commands generator and integrate into build process",
        "device: Update vendor log tag include path in device.mk":
            "even: Update vendor log tag include path in device.mk",
        "device: Update default branch for manifest repo to lineage-21 in crave-build.py":
            "even: Update default manifest branch to lineage-21 in crave-build.py",
        "device: Remove unneeded OMX libraries from proprietary-files.txt":
            "even: Remove unused OMX libraries from proprietary-files.txt",
        "device: Refactor sensor-related packages in device.mk and update blob_fixup in extract-files.sh":
            "even: Refactor sensor packages in device.mk and update blob_fixup in extract-files.sh",
        "device: Update blob_fixup function to replace and add needed libraries for sensor support":
            "even: Update blob_fixup: replace and add libraries for sensor support",
        "Add power hint configuration and remove obsolete power scenario table":
            "even: Add power hint configuration and remove obsolete power scenario table",
        "device: Add libshim_sensors shared library for sensor support":
            "even: Add libshim_sensors shared library for sensor support",
        "device: Set environment variables for build username and hostname":
            "even: Set environment variables for build username and hostname",
        "device: Add hardware/mediatek to PRODUCT_SOONG_NAMESPACES":
            "even: Add hardware/mediatek to PRODUCT_SOONG_NAMESPACES",
        "device: Remove obsolete VNDK libraries from PRODUCT_PACKAGES and blob_fixup function":
            "even: Remove obsolete VNDK libraries from PRODUCT_PACKAGES and blob_fixup",
        "device: Implement android.hardware.light service with necessary files and configurations":
            "even: Implement android.hardware.light service with required files and configs",
        "device: Add clean build option to crave build script":
            "even: Add clean build option to crave build script",
        "device: Enable effects support for vibrator service":
            "even: Enable effects support for vibrator service",
        "device: Remove obsolete USB vendor packages from PRODUCT_PACKAGES":
            "even: Remove obsolete USB vendor packages from PRODUCT_PACKAGES",
        "device: Remove obsolete radio configuration packages from PRODUCT_PACKAGES":
            "even: Remove obsolete radio configuration packages from PRODUCT_PACKAGES",
        "device: use vibrator service from f.23":
            "even: Use vibrator service from pixel-framework 23",
        "device: Update paths in device.mk to use DEVICE_PATH variable":
            "even: Update paths in device.mk to use DEVICE_PATH variable",
        "device: Add HAL configuration for sensor subhal and related libraries":
            "even: Add HAL configuration for sensor sub-HAL and related libraries",
        "device: Add comprehensive task profiles and attributes for CPU and memory management":
            "even: Add comprehensive task profiles and attributes for CPU and memory management",
        "device: Remove obsolete performance types from SELinux policy":
            "even: Remove obsolete performance types from SELinux policy",
        "device: Update kernel clang version to r510928":
            "even: Update kernel clang version to r510928",
        "device: Enable AAL support in vendor properties":
            "even: Enable AAL (Ambient Adaptive Light) support in vendor properties",
        "device: Update Android.mk, device.mk, extract-files.sh, and proprietary-files.txt for new libraries and cleanup":
            "even: Update build files: add new libraries and clean up obsolete entries",
        "device: Add performance type for scheduling assistance in SELinux policy":
            "even: Add performance type for scheduling assistance in SELinux policy",
        "device: Add Android.bp for prebuilt HIDL interfaces for MediaTek hardware":
            "even: Add Android.bp for prebuilt HIDL interfaces for MediaTek hardware",
        "device: Add ScopedWakelock support and enable vibrator service for MediaTek":
            "even: Add ScopedWakelock support and enable vibrator service for MediaTek",
        "device: Remove Mediatek vibrator service and related files from extraction scripts":
            "even: Remove MediaTek vibrator service and related files from extraction scripts",
        "device: Enable MTK hardware support in BoardConfig":
            "even: Enable MediaTek hardware support in BoardConfig",
        "device: Add VNDK support for libbinder-v32 and update extract-files script":
            "even: Add VNDK support for libbinder-v32 and update extract-files script",
        "device: Add libnir_neon_driver support for MediaTek MT6768":
            "even: Add libnir_neon_driver support for MediaTek MT6768",
        "device: Update proprietary-files.txt to include libpq_prot and RbsFlow libraries":
            "even: Add libpq_prot and RbsFlow libraries to proprietary-files.txt",
        "device: Replace libexif with libexpat in PRODUCT_PACKAGES":
            "even: Replace libexif with libexpat in PRODUCT_PACKAGES",
        "device: Add Oplus performance libraries to proprietary-files.txt":
            "even: Add Oplus performance libraries to proprietary-files.txt",
        "device: Add TARGET_SCREEN_DENSITY configuration for display settings":
            "even: Add TARGET_SCREEN_DENSITY configuration for display settings",
        "device: Update userdata mount options in fstab.mt6768 for improved performance":
            "even: Update userdata mount options in fstab.mt6768 for improved performance",
        "device.mk drop lineage health.":
            "even: Remove Lineage health HAL from PRODUCT_PACKAGES",
        "And the missing libs that where left behind.":
            "even: Add missing audio libraries to fix audio playback",
        "device.mk: bluetooth changes":
            "even: Update Bluetooth packages and add A2DP implementation",
        "drop lineage health sepolicy":
            "even: Remove Lineage health HAL SELinux policy",
        "prop: set ro.sf.lcd_density=480":
            "even: Set LCD density to 480 dpi",
        "Adding missing libs. this fixes fingerprint":
            "even: Add missing Oplus performance libraries for fingerprint support",
        "device.mk: fix libutils-v32 was exported twice":
            "even: Fix duplicate libutils-v32 export in device.mk",
        "added more missing libs":
            "even: Add more missing camera and audio libraries",
        "androd.bp: fix typo":
            "even: Fix typo in Android.bp filename",
        "even: we dont have side power button mounted fingerprint sensor.":
            "even: Remove side fingerprint sensor overlay configuration",
        "Reorganise libs in proprietary-files.txt":
            "even: Reorganize library entries in proprietary-files.txt",
        "Proprietary-files.txt: add some more missing libs needed by camerahalserver":
            "even: Add missing camera HAL server libraries",
        "extract.sh: lets not over patch libs":
            "even: Reduce unnecessary library patching in extract-files.sh",
        'Revert "device.mk: bluetooth changes"':
            "even: Revert Bluetooth A2DP package changes",
        "sepolicy: add rules for enforcing mode":
            "sepolicy: Add SELinux rules for enforcing mode",
        "BoardConfig: switch to enforcing selinux":
            "BoardConfig: Switch SELinux to enforcing mode",
        "Drop NFC support.":
            "even: Drop NFC support and remove related configuration",
        "hals.conf: duplicate cleanup":
            "even: Remove duplicate entries from hals.conf",
        "device.mk: fix path":
            "even: Fix typo in privileged permission path",
        "proprietary-files.txt: Add missing OLC and camera libraries":
            "even: Add missing OLC and camera libraries",
        "sepolicy: Fix neverallow violations and cleanup":
            "sepolicy: Fix SELinux neverallow violations and clean up policy",
        "proprietary-files.txt: Add libVDBlurless.so and libvdblurless.so for MFLL":
            "even: Add libVDBlurless libraries for MFLL support",
        "vndk: drop because los22.2 already has them":
            "even: Remove VNDK libraries already provided by LineageOS 22.2",
        "device: Update touch HAL service and add soong config for OPLUS_LINEAGE_TOUCH":
            "even: Update touch HAL service and add OPLUS_LINEAGE_TOUCH soong config",
        "sepolicy: Use existing proc_dirty type for dirty_writeback_centisecs":
            "sepolicy: Use existing proc_dirty type for dirty_writeback_centisecs",
        "kernel: Update clang version to r536225":
            "kernel: Update clang version to r536225",
        "init: Remove orphaned user/group keywords outside of service block":
            "init: Remove orphaned user/group keywords from non-service blocks",
        "libshims: Add libprocessgroup shim for hwcomposer":
            "libshims: Add libprocessgroup shim for hwcomposer",
        "device: Add libtinyalsa for audio.usb vendor blob":
            "even: Add libtinyalsa for audio.usb vendor blob",
        "audio: Add libalsautils-v31 compat shim for audio HAL blobs":
            "audio: Add libalsautils-v31 compatibility shim for audio HAL blobs",
        "device.mk: drop livedisplay":
            "even: Remove LiveDisplay from device.mk",
        "device: Install libtinyalsa to vendor partition for Mediatek audio HAL":
            "even: Install libtinyalsa to vendor partition for MediaTek audio HAL",
        "device.mk: fix whitespace":
            "even: Fix whitespace formatting in device.mk",
        "proprietary-files.txt: Remove duplicate osense and performance prebuilts":
            "even: Remove duplicate osense and performance prebuilt entries",
        'Revert "proprietary-files.txt: Remove duplicate osense and performance prebuilts"':
            "even: Revert: restore osense and performance duplicate prebuilt entries",
        "device.mk: add back ramdisk fstab":
            "even: Restore ramdisk fstab entries in device.mk",
        "even: Stop pinning kernel clang version":
            "even: Stop pinning kernel clang version",
        "device: Enable DOZE_FIX for dt2w wakeup support":
            "even: Enable DOZE_FIX for double-tap-to-wake support",
        "proprietary-files: Add missing mcRegistry TEE blob":
            "even: Add missing mcRegistry TEE blob to proprietary files",
        "init: Replace timezone-based camera detection with fixed prjname mapping":
            "init: Replace timezone-based camera detection with fixed prjname mapping",
        "BoardConfig.mk: Switch SELinux to enforcing mode":
            "BoardConfig: Switch SELinux to enforcing mode",
        "init: Set device model based on prjname for unified DT":
            "init: Set device model based on prjname for unified device tree",
        "init: Remove redundant dalvik heap override":
            "init: Remove redundant dalvik heap override",
        "init: Refactor to use set_device_props across all ro.product sources":
            "init: Refactor to use set_device_props across all ro.product sources",
        "device.mk: Restore hardware/lineage/compat namespace for libstagefright_foundation-v33":
            "even: Restore hardware/lineage/compat namespace for libstagefright_foundation-v33",
        "proprietary-files.txt: Add MODULE_SUFFIX for osense and performance NDK backend libs":
            "even: Add MODULE_SUFFIX for osense and performance NDK backend libs",
        "device.mk: Install libstagefright_foundation-v33 as vendor module":
            "even: Install libstagefright_foundation-v33 as vendor module",
        'Revert "vndk: drop because los22.2 already has them"':
            "even: Restore VNDK libraries removed for LineageOS 22.2 compatibility",
        "overlay: Import activity open/close animations":
            "even: overlay: Import activity open/close animations for Android 16",
        "device.mk: remove duplicate entries for libstagefright_foundation-v33":
            "even: Remove duplicate libstagefright_foundation-v33 entries",
        "device.mk: Reorganize gatekeeper packages and fix libgatekeeper.vendor":
            "even: Reorganize gatekeeper packages and fix libgatekeeper.vendor",
        "device.mk & vendorsetup.sh: Drop PocketMode as InfinityX has its own implementation":
            "even: Drop PocketMode as InfinityX has its own implementation",
        "infinity_even.mk: Add INFINITY_MAINTAINER build flag":
            "infinity_even.mk: Add INFINITY_MAINTAINER build flag",
        "infinity: Switch from LineageOS to Infinity ROM as base":
            "infinity: Switch from LineageOS to Infinity ROM base",
        "init: Set per-variant market name, SOC, and timezone-based camera props.":
            "init: Set per-variant market name, SOC, and timezone-based camera properties",
        "even: Switch rootdir to Android.bp and update device.mk":
            "even: Switch rootdir to Android.bp and update device.mk",
        "even: BoardConfig.mk: Drop lineage device_framework_matrix.xml include":
            "even: BoardConfig: Drop Lineage device_framework_matrix.xml include",
        "device.mk: Update memtrack service name":
            "even: Update memtrack service name",
        "device.mk: Add libinit_even soong config, remove deprecated keymaster V3 ndk":
            "even: Add libinit_even soong config and remove deprecated keymaster V3 NDK",
        "BoardConfig.mk: Add TARGET_RECOVERY_DEVICE_MODULES for libinit_even":
            "BoardConfig: Add TARGET_RECOVERY_DEVICE_MODULES for libinit_even",
        "rootdir: Update CPU governor, cpuset, and uclamp tuning in init.mt6768.power.rc":
            "rootdir: Update CPU governor, cpuset, and uclamp tuning in power init rc",
        "device.mk: Add oplus NDK AIDL backends, sensors 1.0-convert-shared, and custom USB gadget":
            "even: Add Oplus NDK AIDL backends, sensors 1.0-convert-shared, and custom USB gadget",
        "rro_overlays: Add LauncherOverlayEven and notification shade blur radius":
            "rro_overlays: Add LauncherOverlayEven and notification shade blur radius",
        "extract-files.sh: Switch sensors subhal to 1.0-convert-shared and add libbase_shim to sensors service":
            "extract-files.sh: Switch sensors sub-HAL to 1.0-convert-shared and add libbase_shim",
        "sepolicy/vendor/init.te: Remove proc filesystem associate permission from init":
            "sepolicy/vendor: Remove proc filesystem associate permission from init",
        "sepolicy/vendor: Add missing mtk_hal_gnss type declaration":
            "sepolicy/vendor: Add missing mtk_hal_gnss type declaration",
        "sepolicy: Allow audioserver to read vendor_default_prop":
            "sepolicy: Allow audioserver to read vendor_default_prop",
        "Init: Set device props and Axion persist props per prjname":
            "init: Set device properties and Axion persist props per project name",
        "even: Patch mtkfusionrild to load libutils-v32 * Fixes RIL in Android 16":
            "even: Patch mtkfusionrild to load libutils-v32 for RIL on Android 16",
        "Refactor vendor variant handling in setup-makefiles.sh":
            "even: Refactor vendor variant handling in setup-makefiles.sh",
        "even: camera: Build libexif module":
            "even: camera: Build libexif module",
        "device.mk: correct the maintainer name":
            "even: Correct maintainer name in device.mk",
        "sh: change address for kernel vendor setup":
            "vendorsetup: Update kernel vendor setup repository URL",
        "device.mk: copy permission file for eng apk":
            "even: Add privileged permission for engineer mode APK",
        "tree: adapt for axion":
            "even: Adapt device tree for Axion OS",
        "enable axion specific props and features":
            "even: Enable Axion-specific vendor properties and features",
        "drop dolby for axionfx":
            "even: Remove Dolby Atmos support for AxionFX",
        "vendorsetup: add ViPER4AndroidFX":
            "vendorsetup: Add ViPER4AndroidFX",
        "Boardconfig: update vendor security patch":
            "BoardConfig: Update vendor security patch level",
        "BoardConfig: update vendor security patch":
            "BoardConfig: Update vendor security patch level",
    }

    # Handle the merge commit WIP messages
    if stripped_subject.startswith("WIP on lineage-23.2:"):
        return "even: Merge branch 'lineage-23.2' into axion"
    if stripped_subject.startswith("index on lineage-23.2:"):
        return "even: Stash index state for lineage-23.2 merge" + body

    # Post-rewrite dedup: clean body duplication from first filter-branch run
    # Detect if the body has duplicate content by checking paragraph containment
    if body.strip():
        body = clean_duplicated_body(body)

    # Handle commits with body text embedded in subject (multi-line subjects)
    if stripped_subject.startswith("even: : props: remove obsolete HWUI tuning properties"):
        return ("even: props: Remove obsolete HWUI tuning properties\n\n"
                "Remove debug.hwui.target_cpu_time_percent and debug.hwui.use_hint_manager.\n"
                "These properties are either deprecated or ignored on\n"
                "modern Android releases and provide no measurable\n"
                "benefit on Android 16 QPR2.")

    if stripped_subject.startswith("even: : Fix permissions for oplusreserve1"):
        return ("even: Fix permissions for oplusreserve1 sensor node\n\n"
                "oplusSensor service needs to read oplusreserve1 for\n"
                "sensor calibration data.")

    if stripped_subject.startswith("even: : Allocate 4 buffers for SurfaceFlinger"):
        return ("even: Allocate 4 buffers for SurfaceFlinger FrameBufferSurface\n\n"
                "This prevents GC overhead and improves UI fluidity.")

    if stripped_subject.startswith("init: Remove meta"):
        return ("init: Remove engineering meta init files\n\n"
                "These are only used on stock engineering firmware,\n"
                "which we do not have or ship.")

    if stripped_subject.startswith("init: Remove MediaTek gauge and power on property"):
        return ("init: Remove MediaTek gauge and power on property actions\n\n"
                "These properties are not set within the device tree and serve no purpose.")

    if stripped_subject.startswith("even: Explicitly disable Audio HAL PCM dumping"):
        return ("even: Explicitly disable Audio HAL PCM dumping\n\n"
                "MediaTek's Audio HAL can dump all audio streams into\n"
                "/data/vendor/audiohal/audio_dump. This has privacy and\n"
                "security implications, so ensure it is disabled.")

    if stripped_subject.startswith("overlay: Import activity open/close animations"):
        return ("even: overlay: Import activity open/close animations\n\n"
                "After Android 16, there has been significant lag when transitioning\n"
                "between menus such as the Settings app. Import the activity\n"
                "open/close animations from frameworks/base commit\n"
                "aa4b1a18da3e561653d3aed9090deb5d6cbd7c82.\n\n"
                "We will tweak them later to resolve the lag.")

    if stripped_subject.startswith("even:: overlay: Disable NearbyMessagesService"):
        return ("even: overlay: Disable NearbyMessagesService\n\n"
                "This fixes slow Internet speed while using Bluetooth.")

    # Commits with body text in subject line - split them
    if stripped_subject.startswith("even: props:"):
        return fix_multi_line_subject(stripped_subject, body)
    if stripped_subject.startswith("init:") and stripped_subject.count(" ") > 4:
        return fix_multi_line_subject(stripped_subject, body)

    # Handle Boardconfig: with different capitalization
    if stripped_subject.startswith("Boardconfig:"):
        stripped_subject = "BoardConfig:" + stripped_subject[12:]

    # Exact match first (after special cases)
    if stripped_subject in rewrites:
        new_subject = rewrites[stripped_subject]
        if body.strip():
            return new_subject + body
        return new_subject

    # Check for "spaced:" prefix and replace with "even:"
    if subject.startswith("spaced:") or subject.startswith("spaced :"):
        new_subject = re.sub(r'^spaced\s*:\s*', 'even: ', subject)
        return fix_message(new_subject, body)

    # Check for "even:" with various formatting issues
    if subject.startswith("even:") or subject.startswith("even :"):
        return fix_message(subject, body)

    # General prefix-based rewrites
    if subject.startswith("device:"):
        return fix_message(re.sub(r'^device:', 'even:', subject), body)
    if subject.startswith("Device:"):
        return fix_message(re.sub(r'^Device:', 'even:', subject), body)
    if subject.startswith("device.mk:"):
        return fix_message(re.sub(r'^device\.mk:', 'even:', subject), body)

    # Default: apply general fixes
    return fix_message(stripped_subject, body)


def body_without_changeid(body):
    """Strip Change-Id and Signed-off-by lines from body for reformatted messages."""
    if not body:
        return ""
    lines = body.split('\n')
    clean = []
    for line in lines:
        if line.startswith('Change-Id:') or line.startswith('Signed-off-by:'):
            continue
        clean.append(line)
    return '\n' + '\n'.join(clean).strip()


def fix_multi_line_subject(subject, body):
    """Split a subject that has body text embedded in it."""
    # Find where the body text starts (after a * or similar marker)
    parts = re.split(r'\s*\*\s*', subject, maxsplit=1)
    if len(parts) > 1:
        desc = parts[0].strip()
        rest = parts[1].strip()
        # Clean up rest
        rest = rest.rstrip('.')
        result = desc + '\n\n' + rest
        if body.strip():
            result += '\n' + body.strip()
        return result
    
    # Try splitting on dash
    parts = re.split(r'\s+-\s+', subject, maxsplit=1)
    if len(parts) > 1 and len(parts[1]) > 20:
        desc = parts[0].strip()
        rest = parts[1].strip().rstrip('.')
        result = desc + '\n\n' + rest
        if body.strip():
            result += '\n' + body.strip()
        return result
    
    return fix_message(subject, body)


def clean_duplicated_body(body):
    """Remove duplicated body content.

    Handles the case where a commit was run through filter-branch twice:
    the first run embedded custom body + original body, creating duplication
    where one paragraph is a subset (or duplicate) of another.
    """
    if not body or not body.strip():
        return body

    paragraphs = re.split(r'\n\n+', body.strip())
    if len(paragraphs) <= 1:
        return body

    # Build normalized versions (collapse whitespace, lowercase)
    norm = [' '.join(p.split()).lower() for p in paragraphs]

    # Keep only paragraphs that are NOT a subset of an earlier paragraph
    keep = []
    keep_norm = []
    for i, (para, n) in enumerate(zip(paragraphs, norm)):
        is_duplicate = False
        for kn in keep_norm:
            if n in kn or kn in n:
                is_duplicate = True
                break
        if not is_duplicate:
            keep.append(para)
            keep_norm.append(n)

    if len(keep) == len(paragraphs):
        return body

    return '\n\n'.join(keep)


def fix_message(subject, body):
    """Apply general fixes to a commit message."""
    s = subject.strip()

    # Fix double colons
    s = re.sub(r'::', ':', s)

    # Fix "even: :" pattern (double colon with space)
    s = re.sub(r'\beven\s*:\s*:', 'even:', s)

    # Remove duplicated body content (when subject also contained body text)
    body = clean_duplicated_body(body)

    # Fix "spaced" references in body
    if body:
        body = body.replace("spaced", "even")
        body = body.replace("MT6781", "MT6768")
        body = body.replace("mt6781", "mt6768")
        body = body.replace("Mt6781", "Mt6768")

    # Remove trailing periods from subject (unless it ends with ellipsis)
    if s.endswith('.') and not s.endswith('...') and not s.endswith('..'):
        s = s[:-1]

    # Remove multiple spaces
    s = re.sub(r'  +', ' ', s)

    # Fix common typos
    typos = {
        "Mediatek": "MediaTek",
        "mediatek": "MediaTek",
        "dublicate": "duplicate",
        "overide": "override",
        "occured": "occurred",
        "recieved": "received",
        "calclulation": "calculation",
        "implmentation": "implementation",
        "diable": "disable",
        "enabel": "enable",
        "privilaged": "privileged",
        "priviledged": "privileged",
        "beleive": "believe",
        "thier": "their",
        "alot": "a lot",
        "inital": "initial",
        "laggish": "laggy",
        "reorganise": "reorganize",
    }
    for wrong, correct in typos.items():
        s = s.replace(wrong, correct)

    # If Change-Id ended up in subject, remove it
    if 'Change-Id:' in s:
        s = s.split('Change-Id:')[0].strip()

    result = s
    if body:
        result += body

    # Final cleanup
    result = result.strip()

    # If no newline, just return the subject
    if '\n' not in result:
        return result

    # Split and rejoin to clean up
    parts = result.split('\n', 1)
    new_subject = parts[0].strip()
    new_body = parts[1] if len(parts) > 1 else ''

    result = new_subject
    if new_body:
        result += '\n' + new_body

    return result


if __name__ == '__main__':
    msg = sys.stdin.read()
    rewritten = rewrite(msg)
    sys.stdout.write(rewritten)
