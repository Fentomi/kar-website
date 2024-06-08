/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import router from '../router'
import { AutoCompletePlugin } from "@syncfusion/ej2-vue-dropdowns";
import VueTippy from "vue-tippy";
import 'tippy.js/dist/tippy.css';

export function registerPlugins (app) {
  app
    .use(AutoCompletePlugin)
    .use(vuetify)
    .use(router)
    .use(VueTippy)
}
