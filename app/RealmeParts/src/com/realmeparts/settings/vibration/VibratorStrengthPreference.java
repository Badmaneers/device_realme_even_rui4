package com.realmeparts.settings.vibration;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.AttributeSet;
import android.os.Vibrator;
import androidx.preference.PreferenceManager;

import com.realmeparts.settings.R;
import com.realmeparts.settings.preference.CustomSeekBarPreference;
import com.realmeparts.settings.util.Utils;

public class VibratorStrengthPreference extends CustomSeekBarPreference {

    private static int mMinVal = 1;
    private static int mMaxVal = 9;
    private static int mDefVal = 5;
    private Vibrator mVibrator;

    private static final String FILE_LEVEL = "/sys/class/leds/vibrator/vmax";
    private static final long[] testVibrationPattern = {0,250};

    public VibratorStrengthPreference(Context context, AttributeSet attrs) {
        super(context, attrs);

        mInterval = 1;
        mShowSign = false;
        mUnits = "";
        mContinuousUpdates = false;
        mMinValue = mMinVal;
        mMaxValue = mMaxVal;
        mDefaultValueExists = true;
        mDefaultValue = mDefVal;
        mValue = Integer.parseInt(loadValue());

        setPersistent(false);
        mVibrator = (Vibrator) context.getSystemService(Context.VIBRATOR_SERVICE);
    }

    public static boolean isSupported() {
        return Utils.fileWritable(FILE_LEVEL);
    }

    public static String loadValue() {
        return Utils.getFileValue(FILE_LEVEL, String.valueOf(mDefVal));
    }

    private void setValue(String newValue) {
        Utils.writeValue(FILE_LEVEL, newValue);
        SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(getContext()).edit();
        editor.putString("vib_strength", newValue);
        editor.commit();
        mVibrator.vibrate(testVibrationPattern, -1);
    }

    public static void restore(Context context) {
        if (!isSupported()) {
            return;
        }

        String storedValue = PreferenceManager.getDefaultSharedPreferences(context).getString("vib_strength", String.valueOf(mDefVal));
        Utils.writeValue(FILE_LEVEL, storedValue);
    }

    @Override
    protected void changeValue(int newValue) {
        setValue(String.valueOf(newValue));
    }
}
