package com.realmeparts.settings.speaker;

import android.app.Activity;
import android.content.Context;
import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.realmeparts.settings.R;

public class ClearSpeakerActivity extends Activity {

    private Button mButton;
    private TextView mStatus;
    private AudioTrack mAudioTrack;
    private boolean mPlaying = false;
    private Handler mHandler = new Handler();

    private static final int DURATION_SECONDS = 60;
    private static final int SAMPLE_RATE = 44100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.clear_speaker_settings);

        mButton = findViewById(R.id.clear_speaker_button);
        mStatus = findViewById(R.id.clear_speaker_status);

        mButton.setOnClickListener(v -> {
            if (mPlaying) {
                stop();
            } else {
                start();
            }
        });
    }

    private void start() {
        AudioManager audio = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
        int currentVolume = audio.getStreamVolume(AudioManager.STREAM_MUSIC);
        int maxVolume = audio.getStreamMaxVolume(AudioManager.STREAM_MUSIC);

        if (currentVolume < maxVolume) {
            mStatus.setText("Please set media volume to maximum");
            return;
        }

        int bufferSize = AudioTrack.getMinBufferSize(SAMPLE_RATE,
                AudioFormat.CHANNEL_OUT_MONO, AudioFormat.ENCODING_PCM_16BIT);

        mAudioTrack = new AudioTrack(AudioManager.STREAM_MUSIC, SAMPLE_RATE,
                AudioFormat.CHANNEL_OUT_MONO, AudioFormat.ENCODING_PCM_16BIT,
                bufferSize, AudioTrack.MODE_STREAM);

        // Generate a frequency sweep from 200Hz to 20kHz
        final short[] buffer = new short[bufferSize];
        final double duration = DURATION_SECONDS;
        final double startFreq = 200;
        final double endFreq = 20000;
        final long totalSamples = (long) (SAMPLE_RATE * duration);

        mAudioTrack.play();
        mPlaying = true;
        mButton.setText("Stop");
        mStatus.setText("Playing...");

        new Thread(() -> {
            for (long i = 0; i < totalSamples && mPlaying; i += buffer.length) {
                for (int j = 0; j < buffer.length && (i + j) < totalSamples; j++) {
                    double t = (double) (i + j) / SAMPLE_RATE;
                    double freq = startFreq + (endFreq - startFreq) * (t / duration);
                    buffer[j] = (short) (Math.sin(2 * Math.PI * freq * t) * Short.MAX_VALUE * 0.8);
                }
                if (mAudioTrack != null) {
                    mAudioTrack.write(buffer, 0, Math.min(buffer.length, (int) (totalSamples - i)));
                }
            }
            mHandler.post(this::stop);
        }).start();
    }

    private void stop() {
        mPlaying = false;
        if (mAudioTrack != null) {
            mAudioTrack.stop();
            mAudioTrack.release();
            mAudioTrack = null;
        }
        mButton.setText(R.string.clear_speaker_title);
        mStatus.setText("Done");
    }

    @Override
    protected void onDestroy() {
        stop();
        super.onDestroy();
    }
}
