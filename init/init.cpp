/*
 * Copyright (C) 2020 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <cstdlib>
#include <cstring>
#include <string>

#include <android-base/properties.h>
#include <android-base/logging.h>
#define _REALLY_INCLUDE_SYS__SYSTEM_PROPERTIES_H_
#include <sys/_system_properties.h>

#include "vendor_init.h"
#include "property_service.h"

void property_override(char const prop[], char const value[])
{
    auto pi = (prop_info *) __system_property_find(prop);

    if (pi != nullptr) {
        __system_property_update(pi, value, strlen(value));
    } else {
        __system_property_add(prop, strlen(prop), value, strlen(value));
    }
}

void vendor_load_properties() {
    std::string prjname = android::base::GetProperty("ro.boot.prjname", "");

    if (prjname == "20761") {
        property_override("ro.product.model", "RMX3191");
        property_override("ro.product.name", "RMX3191");
        property_override("ro.product.device", "RMX3191");
        property_override("ro.build.product", "RMX3191");
    } else if (prjname == "2167A") {
        property_override("ro.product.model", "RMX3195");
        property_override("ro.product.name", "RMX3195");
        property_override("ro.product.device", "RMX3195");
        property_override("ro.build.product", "RMX3195");
    } else if (prjname == "216AF") {
        property_override("ro.product.model", "RMX3430");
        property_override("ro.product.name", "RMX3430");
        property_override("ro.product.device", "RMX3430");
        property_override("ro.build.product", "RMX3430");
    }
}
