echo start cloning repos
VT=vendor/realme/even/even-vendor.mk
if ! [ -a $VT ]; then git clone https://github.com/Badmaneers/vendor_realme_even_rui4 -bb main-oss vendor/realme/even
fi
KT=kernel/realme/even/build.sh
if ! [ -a $KT ]; then git clone --recurse-submodules --depth=1 https://github.com/Badmaneers/kernel_even_4.19 kernel/realme/even
fi
MTK_SEPOLICY=device/mediatek/sepolicy_vndr/SEPolicy.mk
if ! [ -a $MTK_SEPOLICY ]; then git clone https://github.com/LineageOS/android_device_mediatek_sepolicy_vndr -b lineage-21 device/mediatek/sepolicy_vndr
fi
MTK=hardware/mediatek/Android.bp
if ! [ -a $MTK ]; then git clone https://github.com/LineageOS/android_hardware_mediatek -b lineage-21  hardware/mediatek
fi
OPLUS=hardware/oplus/Android.bp
if ! [ -a $OPLUS ]; then git clone https://github.com/LineageOS/android_hardware_oplus -b lineage-21 hardware/oplus
fi
echo end cloning
