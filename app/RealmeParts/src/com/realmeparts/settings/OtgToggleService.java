package com.realmeparts.settings;

import android.content.Intent;
import android.service.quicksettings.Tile;
import android.service.quicksettings.TileService;

public class OtgToggleService extends TileService {

    @Override
    public void onStartListening() {
        super.onStartListening();
        updateTile();
    }

    @Override
    public void onClick() {
        if (OTGModeSwitch.isCurrentlyEnabled()) {
            FileUtils.setValue(OTGModeSwitch.getFile(), "0");
        } else {
            FileUtils.setValue(OTGModeSwitch.getFile(), "1");
        }
        updateTile();
    }

    private void updateTile() {
        Tile tile = getQsTile();
        if (OTGModeSwitch.isCurrentlyEnabled()) {
            tile.setState(Tile.STATE_ACTIVE);
        } else {
            tile.setState(Tile.STATE_INACTIVE);
        }
        tile.updateTile();
    }
}
