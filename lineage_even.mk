#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from even device
$(call inherit-product, device/realme/even/device.mk)

PRODUCT_DEVICE := even
PRODUCT_NAME := lineage_even
PRODUCT_BRAND := even
PRODUCT_MODEL := realme C25
PRODUCT_MANUFACTURER := realme

PRODUCT_GMS_CLIENTID_BASE := android-realme

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="sys_mssi_64_cn_armv82-user 13 TP1A.220905.001 1716367279348 release-keys"

BUILD_FINGERPRINT := realme/RMX3191/RMX3191:13/TP1A.220905.001/1716367279348:user/release-keys
