package com.realmeparts.settings;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.util.Log;

import androidx.preference.PreferenceManager;

import com.realmeparts.settings.vibration.VibratorStrengthPreference;

public class BootCompletedReceiver extends BroadcastReceiver {

    private static final String TAG = "RealmeParts";

    @Override
    public void onReceive(final Context context, Intent intent) {
        VibratorStrengthPreference.restore(context);

        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
        if (prefs.getBoolean("otg", false)) {
            FileUtils.setValue("/sys/devices/virtual/oplus_chg/usb/otg_switch", "1");
        }
        if (prefs.getBoolean("hbm", false)) {
            FileUtils.setValue("/sys/kernel/oplus_display/hbm", "1");
        }
        if (prefs.getBoolean("dc_dimming", false)) {
            FileUtils.setValue("/sys/kernel/oplus_display/dim_dc_alpha", "1");
            FileUtils.setValue("/sys/kernel/oplus_display/dimlayer_bl_en", "1");
        }
    }
}
