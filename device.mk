#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/realme/even

# Installs gsi keys into ramdisk, to boot a developer GSI with verified boot.
$(call inherit-product, $(SRC_TARGET_DIR)/product/developer_gsi_keys.mk)

# # RealmeParts
# $(call inherit-product, packages/apps/RealmeParts/parts.mk)

# Inherit Vendor Blobs
$(call inherit-product, vendor/realme/even/even-vendor.mk)

# Enable updating of APEXes
$(call inherit-product, $(SRC_TARGET_DIR)/product/updatable_apex.mk)

# Boot Animation
TARGET_SCREEN_HEIGHT := 1600
TARGET_SCREEN_WIDTH := 720

# Screen density
PRODUCT_AAPT_CONFIG := xxxhdpi
PRODUCT_AAPT_PREF_CONFIG := xxxhdpi
PRODUCT_AAPT_PREBUILT_DPI := xxxhdpi xxhdpi xhdpi hdpi

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
     hardware/mediatek \
     hardware/oplus

# RenderScript
PRODUCT_PACKAGES += \
    android.hardware.renderscript@1.0-impl
    
    # Permissions
PRODUCT_COPY_FILES += \
    $(DEVICE_PATH)/configs/permissions/privapp-permissions-mediatek.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/permissions/privapp-permissions-mediatek.xml

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

# Audio
PRODUCT_PACKAGES += \
    audio.a2dp.default

PRODUCT_COPY_FILES += \
    $(DEVICE_PATH)/configs/audio/audio_policy_configuration.xml:system/etc/audio_policy_configuration.xml \
    $(DEVICE_PATH)/configs/audio/audio_policy_configuration.xml:$(TARGET_COPY_OUT_PRODUCT)/vendor_overlay/$(PLATFORM_VNDK_VERSION)/etc/audio_policy_configuration.xml \
    $(DEVICE_PATH)/configs/audio/audio_policy_configuration.xml:$(TARGET_COPY_OUT_ODM)/etc/audio_policy_configuration.xml

# DRM
PRODUCT_PACKAGES += \
    libdrm
    
# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH) \
    hardware/mediatek \
    hardware/oplus

# KPOC
PRODUCT_PACKAGES += \
    libsuspend

# Speed up
PRODUCT_DEXPREOPT_SPEED_APPS += \
    Launcher3QuickStep \
    Settings \
    SystemUI

# InCall Service
PRODUCT_PACKAGES += \
    BesLoudness \
    MtkInCallService

# IMS
PRODUCT_BOOT_JARS += \
    mediatek-gwsd \
    mediatek-gwsdv2 \
    mediatek-common \
    mediatek-framework \
    mediatek-ims-base \
    mediatek-ims-common \
    mediatek-telecom-common \
    mediatek-telephony-base \
    mediatek-telephony-common


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

    

