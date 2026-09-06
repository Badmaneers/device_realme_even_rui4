package com.realmeparts.settings;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.util.AttributeSet;

import androidx.preference.ListPreference;
import androidx.preference.PreferenceManager;

import com.realmeparts.settings.util.Utils;

public class ChargeLimitPreference extends ListPreference {

    private static final String STOP_CHARGING_PATH = "/sys/class/oplus_chg/battery/stop_charging_enable";

    public ChargeLimitPreference(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public static boolean isSupported() {
        return Utils.fileWritable(STOP_CHARGING_PATH);
    }

    public static String loadValue() {
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(
                android.app.ActivityThread.currentApplication());
        return prefs.getString("charge_limit", "100");
    }

    public static void restore(Context context) {
        if (!isSupported()) {
            return;
        }
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
        String limit = prefs.getString("charge_limit", "100");
        if (!limit.equals("100")) {
            startService(context);
        }
    }

    public static void startService(Context context) {
        Intent intent = new Intent(context, ChargeLimitService.class);
        context.startForegroundService(intent);
        PreferenceManager.getDefaultSharedPreferences(context)
                .edit().putBoolean("charge_limit_service_running", true).apply();
    }

    public static void stopService(Context context) {
        Intent intent = new Intent(context, ChargeLimitService.class);
        context.stopService(intent);
        PreferenceManager.getDefaultSharedPreferences(context)
                .edit().putBoolean("charge_limit_service_running", false).apply();
        FileUtils.setValue(STOP_CHARGING_PATH, "0");
    }
}
