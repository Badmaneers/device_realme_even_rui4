package com.realmeparts.settings;

import android.content.Context;
import android.util.AttributeSet;

import androidx.preference.TwoStatePreference;

import com.realmeparts.settings.util.Utils;

public class OTGModeSwitch extends TwoStatePreference {

    private static final String FILE = "/sys/devices/virtual/oplus_chg/usb/otg_switch";

    public OTGModeSwitch(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public static boolean isSupported() {
        return Utils.fileWritable(FILE);
    }

    public static boolean isCurrentlyEnabled() {
        return Utils.getFileValue(FILE, "0").equals("1");
    }

    public static String getFile() {
        return FILE;
    }
}
