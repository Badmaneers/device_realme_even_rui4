package com.realmeparts.settings;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.content.pm.ServiceInfo;
import android.os.BatteryManager;
import android.os.IBinder;
import android.util.Log;

import androidx.preference.PreferenceManager;

public class ChargeLimitService extends Service {

    private static final String TAG = "ChargeLimitService";
    private static final String CHANNEL_ID = "charge_limit_channel";
    private static final int NOTIFICATION_ID = 1;
    private static final String STOP_CHARGING_PATH = "/sys/class/oplus_chg/battery/stop_charging_enable";
    private static final int HYSTERESIS = 3;

    private SharedPreferences prefs;
    private int chargeLimit = 100;
    private boolean isChargingStopped = false;

    private final BroadcastReceiver batteryReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            if (intent == null || intent.getAction() == null) return;

            if (Intent.ACTION_BATTERY_CHANGED.equals(intent.getAction())) {
                int level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1);
                int scale = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1);
                int percentage = (level * 100) / scale;

                chargeLimit = Integer.parseInt(prefs.getString("charge_limit", "100"));
                handleChargeLimit(percentage);
            }
        }
    };

    private void handleChargeLimit(int percentage) {
        if (chargeLimit >= 100) {
            if (isChargingStopped) {
                FileUtils.setValue(STOP_CHARGING_PATH, "0");
                isChargingStopped = false;
            }
            return;
        }

        if (percentage >= chargeLimit && !isChargingStopped) {
            FileUtils.setValue(STOP_CHARGING_PATH, "1");
            isChargingStopped = true;
            Log.d(TAG, "Charge limit reached: " + percentage + "% >= " + chargeLimit + "%");
        } else if (percentage < (chargeLimit - HYSTERESIS) && isChargingStopped) {
            FileUtils.setValue(STOP_CHARGING_PATH, "0");
            isChargingStopped = false;
            Log.d(TAG, "Resuming charge: " + percentage + "% < " + (chargeLimit - HYSTERESIS) + "%");
        }
    }

    @Override
    public void onCreate() {
        super.onCreate();
        prefs = PreferenceManager.getDefaultSharedPreferences(this);
        createNotificationChannel();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        IntentFilter filter = new IntentFilter(Intent.ACTION_BATTERY_CHANGED);
        registerReceiver(batteryReceiver, filter, Context.RECEIVER_NOT_EXPORTED);

        Notification notification = new Notification.Builder(this, CHANNEL_ID)
                .setContentTitle("Charge Limit Active")
                .setContentText("Limiting charge to " + prefs.getString("charge_limit", "100") + "%")
                .setSmallIcon(android.R.drawable.ic_lock_idle_charging)
                .build();

        startForeground(NOTIFICATION_ID, notification,
                ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE);
        return START_STICKY;
    }

    @Override
    public void onDestroy() {
        unregisterReceiver(batteryReceiver);
        FileUtils.setValue(STOP_CHARGING_PATH, "0");
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    private void createNotificationChannel() {
        NotificationChannel channel = new NotificationChannel(
                CHANNEL_ID,
                "Charge Limit",
                NotificationManager.IMPORTANCE_LOW);
        channel.setDescription("Shows when charge limit is active");
        NotificationManager manager = getSystemService(NotificationManager.class);
        if (manager != null) {
            manager.createNotificationChannel(channel);
        }
    }

    public static boolean isRunning(Context context) {
        // Check if service is running by checking shared preferences
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
        return prefs.getBoolean("charge_limit_service_running", false);
    }
}
