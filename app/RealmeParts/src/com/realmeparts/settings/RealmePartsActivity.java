package com.realmeparts.settings;

import android.os.Bundle;

import androidx.fragment.app.FragmentActivity;

public class RealmePartsActivity extends FragmentActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportFragmentManager().beginTransaction()
                .replace(android.R.id.content, new RealmeParts())
                .commit();
    }
}
