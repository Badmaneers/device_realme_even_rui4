#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/realme/even

# Installs gsi keys into ramdisk, to boot a developer GSI with verified boot.
$(call inherit-product, $(SRC_TARGET_DIR)/product/developer_gsi_keys.mk)

# RealmeParts
$(call inherit-product, packages/apps/RealmeParts/parts.mk)

# Inherit Vendor Blobs
$(call inherit-product, vendor/realme/even/even-vendor.mk)

# Enable updating of APEXes
$(call inherit-product, $(SRC_TARGET_DIR)/product/updatable_apex.mk)

# Boot Animation
TARGET_SCREEN_HEIGHT := 1600
TARGET_SCREEN_WIDTH := 720

# AAPT
PRODUCT_AAPT_CONFIG := normal
PRODUCT_AAPT_PREF_CONFIG := xxhdpi

# Dynamic Partition
PRODUCT_USE_DYNAMIC_PARTITIONS := true
PRODUCT_BUILD_SUPER_PARTITION := false

# fastbootd
PRODUCT_PACKAGES += \
    fastbootd

# The first api level, device has been commercially launched on.
PRODUCT_SHIPPING_API_LEVEL := 30

# Extra VNDK Versions
PRODUCT_EXTRA_VNDK_VERSIONS := 31


# Dex/ART optimization
PRODUCT_ART_TARGET_INCLUDE_DEBUG_BUILD := false
PRODUCT_DEX_PREOPT_DEFAULT_COMPILER_FILTER := everything
PRODUCT_MINIMIZE_JAVA_DEBUG_INFO := true
USE_DEX2OAT_DEBUG := false
DONT_DEXPREOPT_PREBUILTS := true
# Enable whole-program R8 Java optimizations for SystemUI and system_server
SYSTEM_OPTIMIZE_JAVA := true
SYSTEMUI_OPTIMIZE_JAVA := true

# Health
PRODUCT_PACKAGES += \
    android.hardware.health@2.1-impl \
    android.hardware.health@2.1-impl.recovery \
    android.hardware.health@2.1-service


# Lights
PRODUCT_PACKAGES += \
    android.hardware.light@2.0-service.even

# Biometrics
PRODUCT_PACKAGES += \
    android.hardware.biometrics.fingerprint@2.3-service.even

PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.hardware.fingerprint.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/permissions/android.hardware.fingerprint.xml

# Rootdir
PRODUCT_PACKAGES += \
    init.insmod.sh \
    install-recovery.sh \
    swap_enable.sh 

PRODUCT_PACKAGES += \
    fstab.mt6768 \
    init.mt6768.rc \
    init.recovery.mt6768 

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/rootdir/etc/fstab.mt6768:$(TARGET_COPY_OUT_RAMDISK)/fstab.mt6768

# Properties
-include $(DEVICE_PATH)/configs/props/system_prop.mk
PRODUCT_COMPATIBLE_PROPERTY_OVERRIDE := true

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH) \
     hardware/mediatek 

# RenderScript
PRODUCT_PACKAGES += \
    android.hardware.renderscript@1.0-impl
    
# RRO-Overlays
PRODUCT_PACKAGES += \
    CarrierConfigOverlayEven \
    FrameworksResOverlayEven \
    SystemUIOverlayEven \
    SettingsOverlayEven \
    OplusDozeOverlayEven \
    TetheringConfigOverlay \
    TelephonyOverlayEven \
    WifiOverlay

# NFC
PRODUCT_PACKAGES += \
    com.android.nfc_extras \
    NfcNci \
    SecureElement \
    Tag

# Doze
PRODUCT_PACKAGES += \
    OplusDoze

# PowerOffAlarm
PRODUCT_PACKAGES += \
    PowerOffAlarm

# HIDL
PRODUCT_PACKAGES += \
    libhardware \
    libhidltransport \
    libhwbinder

# Bluetooth Audio (System-side HAL, sysbta)
PRODUCT_PACKAGES += \
    audio.sysbta.default \
    android.hardware.bluetooth.audio-service-system

PRODUCT_COPY_FILES += \
    $(DEVICE_PATH)/bluetooth/audio/config/sysbta_audio_policy_configuration.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/sysbta_audio_policy_configuration.xml \
    $(DEVICE_PATH)/bluetooth/audio/config/sysbta_audio_policy_configuration_7_0.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/sysbta_audio_policy_configuration_7_0.xml

# DRM
PRODUCT_PACKAGES += \
    libdrm

# KPOC
PRODUCT_PACKAGES += \
    libsuspend

# Speed up
PRODUCT_DEXPREOPT_SPEED_APPS += \
    Launcher3QuickStep \
    Settings \
    SystemUI

# Parts
PRODUCT_PACKAGES += \
    RealmeParts

# InCall Service
PRODUCT_PACKAGES += \
    BesLoudness \
    MtkInCallService

# IMS
PRODUCT_BOOT_JARS += \
    mediatek-common \
    mediatek-framework \
    mediatek-ims-base \
    mediatek-ims-common \
    mediatek-telecom-common \
    mediatek-telephony-base \
    mediatek-telephony-common

PRODUCT_PACKAGES += \
    libshim_sink

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/permissions/privapp-permissions-mediatek.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/permissions/privapp-permissions-mediatek.xml


# USB
PRODUCT_PACKAGES += \
    android.hardware.usb@1.0.vendor \
    android.hardware.usb@1.1.vendor \
    android.hardware.usb@1.2.vendor \
    android.hardware.usb@1.3.vendor \
    android.hardware.usb.gadget@1.0.vendor \
    android.hardware.usb.gadget@1.1.vendor

# Wi-Fi
PRODUCT_PACKAGES += \
    wpa_supplicant \
    hostapd \
    libwifi-hal-wrapper \
    android.hardware.wifi-service

PRODUCT_PACKAGES += \
    android.hardware.tetheroffload.config@1.0.vendor \
    android.hardware.tetheroffload.control@1.0.vendor \
    android.hardware.tetheroffload.control@1.1.vendor

PRODUCT_PACKAGES += \
    libnetutils.vendor

PRODUCT_COPY_FILES += \
    $(call find-copy-subdir-files,*,$(LOCAL_PATH)/configs/wifi/,$(TARGET_COPY_OUT_VENDOR)/etc/wifi)

    

