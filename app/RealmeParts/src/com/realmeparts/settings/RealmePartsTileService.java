package com.realmeparts.settings;

import android.content.Intent;
import android.service.quicksettings.Tile;
import android.service.quicksettings.TileService;

public class RealmePartsTileService extends TileService {

    @Override
    public void onStartListening() {
        super.onStartListening();
        updateTile();
    }

    @Override
    public void onClick() {
        Intent intent = new Intent(this, RealmePartsActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivityAndCollapse(intent);
    }

    private void updateTile() {
        Tile tile = getQsTile();
        tile.setState(Tile.STATE_ACTIVE);
        tile.updateTile();
    }
}
