package com.realmeparts.settings;

import android.app.ActionBar;
import android.os.Bundle;

import androidx.preference.Preference;
import androidx.preference.SwitchPreferenceCompat;

import com.android.settingslib.widget.SettingsBasePreferenceFragment;
import com.realmeparts.settings.util.Utils;
import com.realmeparts.settings.vibration.VibratorStrengthPreference;

public class RealmeParts extends SettingsBasePreferenceFragment {

    @Override
    public void onActivityCreated(Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        final ActionBar actionBar = getActivity().getActionBar();
        if (actionBar != null) {
            actionBar.setDisplayHomeAsUpEnabled(true);
        }
    }

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.realmeparts, rootKey);

        initVibrator();
        initOTG();
        initHBMToggle();
        initDcDimming();
        initStopCharging();
    }

    private void initVibrator() {
        VibratorStrengthPreference vib = findPreference("vib_strength");
        if (vib != null) {
            vib.setEnabled(VibratorStrengthPreference.isSupported());
        }
    }

    private void initOTG() {
        SwitchPreferenceCompat sw = findPreference("otg");
        if (sw != null) {
            String path = "/sys/devices/virtual/oplus_chg/usb/otg_switch";
            sw.setEnabled(Utils.fileWritable(path));
            if (Utils.fileWritable(path)) {
                sw.setChecked(Utils.getFileValue(path, "0").equals("1"));
                sw.setOnPreferenceChangeListener((p, v) -> {
                    FileUtils.setValue(path, (Boolean) v ? "1" : "0");
                    return true;
                });
            }
        }
    }

    private void initHBMToggle() {
        SwitchPreferenceCompat sw = findPreference("hbm");
        if (sw != null) {
            String path = "/sys/kernel/oplus_display/hbm";
            sw.setEnabled(Utils.fileWritable(path));
            if (Utils.fileWritable(path)) {
                sw.setChecked(Utils.getFileValue(path, "0").equals("1"));
                sw.setOnPreferenceChangeListener((p, v) -> {
                    FileUtils.setValue(path, (Boolean) v ? "1" : "0");
                    return true;
                });
            }
        }
    }

    private void initDcDimming() {
        SwitchPreferenceCompat sw = findPreference("dc_dimming");
        if (sw != null) {
            String path = "/sys/kernel/oplus_display/dim_dc_alpha";
            String pathBl = "/sys/kernel/oplus_display/dimlayer_bl_en";
            boolean supported = Utils.fileWritable(path) && Utils.fileWritable(pathBl);
            sw.setEnabled(supported);
            if (supported) {
                sw.setChecked(Utils.getFileValue(path, "0").equals("1"));
                sw.setOnPreferenceChangeListener((p, v) -> {
                    String val = (Boolean) v ? "1" : "0";
                    FileUtils.setValue(path, val);
                    FileUtils.setValue(pathBl, val);
                    return true;
                });
            }
        }
    }

    private void initStopCharging() {
        SwitchPreferenceCompat sw = findPreference("stop_charging");
        if (sw != null) {
            String path = "/sys/class/oplus_chg/battery/stop_charging_enable";
            sw.setEnabled(Utils.fileWritable(path));
            if (Utils.fileWritable(path)) {
                boolean enabled = Utils.getFileValue(path, "0").equals("1");
                sw.setChecked(enabled);
                sw.setOnPreferenceChangeListener((p, v) -> {
                    FileUtils.setValue(path, (Boolean) v ? "0" : "1");
                    return true;
                });
            }
        }
    }
}
